from time import sleep
from typing import Dict, Tuple, Optional, List

from clearml_agent.backend_api.session import Request
from clearml_agent.glue.utilities import get_bash_output

from clearml_agent.helper.process import stringify_bash_output

from .daemon import K8sDaemon
from .utilities import get_path
from .errors import GetPodsError


class PendingPodsDaemon(K8sDaemon):
    def __init__(self, polling_interval: float, agent):
        super(PendingPodsDaemon, self).__init__(agent=agent)
        self._polling_interval = polling_interval
        self._last_tasks_msgs = {}  # last msg updated for every task

    def get_pods(self):
        if self._agent.using_jobs:
            return self._agent.get_pods_for_jobs(
                job_condition="status.active=1",
                pod_filters=["status.phase=Pending"],
                debug_msg="Detecting pending pods: {cmd}"
            )
        return self._agent.get_pods(
            filters=["status.phase=Pending"],
            debug_msg="Detecting pending pods: {cmd}"
        )

    def _get_pod_name(self, pod: dict):
        return get_path(pod, "metadata", "name")

    def _get_kind_name(self, pod: dict):
        if self._agent.using_jobs:
            return get_path(pod, "metadata", "labels", "job-name")
        return get_path(pod, "metadata", "name")

    def _get_task_id(self, pod: dict):
        return self._get_kind_name(pod).rpartition('-')[-1]

    @staticmethod
    def _get_pod_namespace(pod: dict):
        return pod.get('metadata', {}).get('namespace', None)

    def delete_pod(self, pod: dict, msg: str = None):
        name = self._get_kind_name(pod)
        delete_cmd = 'kubectl delete {} {} -n {}'.format(
            self._agent.kind, name, self._get_pod_namespace(pod)
        )
        self.log.debug(" - deleting {} {}: {}".format(self._agent.kind, (" " + msg) if msg else "", delete_cmd))
        return get_bash_output(delete_cmd)

    def target(self):
        """
        For Jobs, we need to:
            - Get a list of all related Jobs
              * Get "spec.selector.matchLabels.controller-uid"
            - Get a list of all pods belonging to those Jobs
              * Use label "controller-uid=..."
            - Do the same check for the pods
            - If we want to delete, we delete the job, not the pod
        """
        while True:
            # noinspection PyBroadException
            try:
                pods = self.get_pods()
                if pods is None:
                    raise GetPodsError()

                task_id_to_details = dict()

                for pod in pods:
                    pod_name = self._get_pod_name(pod)
                    if not pod_name:
                        continue

                    task_id = self._get_task_id(pod)
                    if not task_id:
                        continue

                    namespace = self._get_pod_namespace(pod)
                    if not namespace:
                        continue

                    task_id_to_details[task_id] = (pod_name, namespace)

                    msg = None

                    waiting = get_path(pod, 'status', 'containerStatuses', 0, 'state', 'waiting')
                    if not waiting:
                        condition = get_path(pod, 'status', 'conditions', 0)
                        if condition:
                            reason = condition.get('reason')
                            if reason == 'Unschedulable':
                                message = condition.get('message')
                                msg = reason + (" ({})".format(message) if message else "")
                    else:
                        reason = waiting.get("reason", None)
                        message = waiting.get("message", None)

                        msg = reason + (" ({})".format(message) if message else "")
                        tags = []

                        if reason == 'ImagePullBackOff':
                            self.delete_pod(pod)
                            try:
                                self._session.api_client.tasks.failed(
                                    task=task_id,
                                    status_reason="K8S glue error: {}".format(msg),
                                    status_message="Changed by K8S glue",
                                    force=True
                                )
                            except Exception as ex:
                                self.log.warning(
                                    'K8S Glue pods monitor: Failed deleting task "{}"\nEX: {}'.format(task_id, ex)
                                )

                            # clean up any msg for this task
                            self._last_tasks_msgs.pop(task_id, None)
                            continue

                    self._update_pending_task_msg(task_id, msg, tags)

                if task_id_to_details:
                    self._process_tasks_for_pending_pods(task_id_to_details)

                # clean up any last message for a task that wasn't seen as a pod
                self._last_tasks_msgs = {k: v for k, v in self._last_tasks_msgs.items() if k in task_id_to_details}
            except GetPodsError:
                pass
            except Exception:
                self.log.exception("Hanging pods daemon loop")

            sleep(self._polling_interval)

    def _process_tasks_for_pending_pods(self, task_id_to_details: Dict[str, Tuple[str, Optional[str]]]):
        self._handle_aborted_tasks(task_id_to_details)

    def _handle_aborted_tasks(self, pending_tasks_details: Dict[str, Tuple[str, Optional[str]]]):
        try:
            result = self._session.get(
                service='tasks',
                action='get_all',
                json={"id": list(pending_tasks_details), "status": ["stopped"], "only_fields": ["id"]},
                method=Request.def_method,
                async_enable=False,
            )
            aborted_task_ids = list(filter(None, (task.get("id") for task in result["tasks"])))

            for task_id in aborted_task_ids:
                pod_name, namespace = pending_tasks_details.get(task_id)
                if not pod_name:
                    self.log.error("Failed locating aborted task {} in pending pods list".format(task_id))
                    continue
                self.log.info(
                    "K8S Glue pods monitor: task {} was aborted by its pod {} is still pending, "
                    "deleting pod".format(task_id, pod_name)
                )

                kubectl_cmd = "kubectl delete pod {pod_name} --output name {namespace}".format(
                    namespace=f"--namespace={namespace}" if namespace else "", pod_name=pod_name,
                ).strip()
                self.log.debug("Deleting aborted task pending pod: {}".format(kubectl_cmd))
                output = stringify_bash_output(get_bash_output(kubectl_cmd))
                if not output:
                    self.log.warning("K8S Glue pods monitor: failed deleting pod {}".format(pod_name))
        except Exception as ex:
            self.log.warning(
                'K8S Glue pods monitor: failed checking aborted tasks for hanging pods: {}'.format(ex)
            )

    def _update_pending_task_msg(self, task_id: str, msg: str, tags: List[str] = None):
        if not msg or self._last_tasks_msgs.get(task_id, None) == (msg, tags):
            return
        try:
            # Make sure the task is queued
            result = self._session.send_request(
                service='tasks',
                action='get_all',
                json={"id": task_id, "only_fields": ["status"]},
                method=Request.def_method,
                async_enable=False,
            )
            if result.ok:
                status = get_path(result.json(), 'data', 'tasks', 0, 'status')
                # if task is in progress, change its status to enqueued
                if status == "in_progress":
                    result = self._session.send_request(
                        service='tasks', action='enqueue',
                        json={
                            "id": task_id, "force": True, "queue": self._agent.k8s_pending_queue_id
                        },
                        method=Request.def_method,
                        async_enable=False,
                    )
                    if not result.ok:
                        result_msg = get_path(result.json(), 'meta', 'result_msg')
                        self.log.debug(
                            "K8S Glue pods monitor: failed forcing task status change"
                            " for pending task {}: {}".format(task_id, result_msg)
                        )

            # Update task status message
            payload = {"task": task_id, "status_message": "K8S glue status: {}".format(msg)}
            if tags:
                payload["tags"] = tags
            result = self._session.send_request('tasks', 'update', json=payload, method=Request.def_method)
            if not result.ok:
                result_msg = get_path(result.json(), 'meta', 'result_msg')
                raise Exception(result_msg or result.text)

            # update last msg for this task
            self._last_tasks_msgs[task_id] = msg
        except Exception as ex:
            self.log.warning(
                'K8S Glue pods monitor: Failed setting status message for task "{}"\nMSG: {}\nEX: {}'.format(
                    task_id, msg, ex
                )
            )
