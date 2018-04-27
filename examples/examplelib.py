import os
import yaml

from kubernetes import config
import kubevirt


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
