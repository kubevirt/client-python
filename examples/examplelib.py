import os
import time
import yaml
from urllib3.exceptions import ReadTimeoutError

from kubernetes import config, watch
import kubevirt


class ExampleLibException(Exception):
    pass


class WaitForException(ExampleLibException):
    pass


class WaitForFailureMatch(WaitForException):
    def __init__(self, event):
        self.event = event
        self.event = event

    def __str__(self):
        return "Failure condition satisfied with item: %s" % self.event


class WaitForTimeout(WaitForException):
    def __init__(self, source, timeout):
        self.source = source
        self.timeout = timeout

    def __str__(self):
        return "Waiting for events from %s reached timeout: %ss" % (
            self.source, self.timeout
        )


class Watch(object):
    """
    Watch collection on changes.
    """
    def __init__(self, event_source, *args, **kwargs):
        """
        Create instance of Watch object

        Args:
            event_source (func): API call to get objects collection
            args (tuple), kwargs(dict): Prameters for `event_source` function
        """
        self._es = event_source
        self._args = args
        self._kw = kwargs

    def _event_source(self, **kwargs):
        kw = self._kw.copy()
        kw.update(kwargs)
        return self._es(*self._args, **kw)

    def watch(self, request_timeout=None):
        """
        Generator returning events from `event_source`

        Args:
            request_timeout (int): Timeout for request (seconds)

        Returns:
            Generator: Event objects
        """
        kw = dict()
        if request_timeout:
            kw['_request_timeout'] = request_timeout
        w = watch.Watch()
        try:
            for e in w.stream(self._event_source, **kw):
                yield e
        except GeneratorExit:
            w.stop()
            raise

    def _wait_for_x(
        self, timeout, filter_condition, success_condition,
        failure_condition
    ):
        step = 5  # 5s
        endtime = timeout + time.time()
        while timeout < endtime:
            try:
                for e in self.watch(request_timeout=step):
                    if not filter_condition(e):
                        continue
                    if success_condition(e):
                        return e['object']
                    if failure_condition(e):
                        raise WaitForFailureMatch(e)
            except ReadTimeoutError:
                continue
        raise WaitForTimeout(self._es, self.timeout)

    def wait_for_item(
        self, name, timeout, success_condition,
        failure_condition=lambda e: False
    ):
        """
        Wait for change on specific object by name.

        Args:
            name (str): Name of object
            timeout (int): Timeout for request (seconds)
            success_condition (func): Predicate for success and exit loop,
                taking event as argument
            failure_condition (func): Predicate to fail loop,
                taking event as argument
        Returns:
            Event: Event which matches `success_condition`
        Raises:
            WaitForTimeout: On request_timeout
            WaitForFailureMatch: On `failure_condition`
        """
        return self._wait_for_x(
            timeout,
            lambda e: get_name(e['object']) == name,
            success_condition, failure_condition
        )

    def wait_for(
        self, timeout, success_condition,
        failure_condition=lambda e: False
    ):
        """
        Wait for any change on given `event_source`.

        Args:
            timeout (int): Timeout for request (seconds)
            success_condition (func): Predicate for success and exit loop,
                taking event as argument
            failure_condition (func): Predicate to fail loop,
                taking event as argument
        Returns:
            Event: Event which matches `success_condition`
        Raises:
            WaitForTimeout: On request_timeout
            WaitForFailureMatch: On `failure_condition`
        """
        return self._wait_for_x(
            timeout, lambda e: True, success_condition,
            failure_condition
        )


def get_client(kubeconfig=None):
    """
    This function loads kubeconfig and return kubevirt.DefaultApi() object.

    Args:
        kubeconfig (str): Path to kubeconfig

    Returns:
        kubevirt.DefaultApi: Instance of KubeVirt client
    """
    if kubeconfig is None:
        kubeconfig = os.environ.get("KUBECONFIG")
        if kubeconfig is None:
            kubeconfig = os.path.expanduser("~/.kube/config")
    cl = config.kube_config._get_kube_config_loader_for_yaml_file(kubeconfig)
    cl.load_and_set(kubevirt.configuration)

    return kubevirt.DefaultApi()


def read_yaml_file(path):
    """
    Read and parse YAML from given file.

    Args:
        path (str): Path to YAML file

    Returns:
        dict: content of file
    """
    path = os.path.join(os.path.dirname(__file__), path)
    with open(path) as fh:
        return yaml.load(fh)


def get_name(obj):
    if isinstance(obj, dict):
        return obj.get('metadata', dict()).get('name')
    return obj.metadata.name


def get_status(obj):
    if isinstance(obj, dict):
        return obj.get('status', dict()).get('phase')
    return obj.status.phase
