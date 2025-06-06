# coding: utf-8

"""
    KubeVirt API

    This is KubeVirt API an add-on for Kubernetes.

    OpenAPI spec version: 1.0.0
    Contact: kubevirt-dev@googlegroups.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class V1KubeVirtSpec(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """


    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'certificate_rotate_strategy': 'V1KubeVirtCertificateRotateStrategy',
        'configuration': 'V1KubeVirtConfiguration',
        'customize_components': 'V1CustomizeComponents',
        'image_pull_policy': 'str',
        'image_pull_secrets': 'list[K8sIoApiCoreV1LocalObjectReference]',
        'image_registry': 'str',
        'image_tag': 'str',
        'infra': 'V1ComponentConfig',
        'monitor_account': 'str',
        'monitor_namespace': 'str',
        'product_component': 'str',
        'product_name': 'str',
        'product_version': 'str',
        'service_monitor_namespace': 'str',
        'synchronization_port': 'str',
        'uninstall_strategy': 'str',
        'workload_update_strategy': 'V1KubeVirtWorkloadUpdateStrategy',
        'workloads': 'V1ComponentConfig'
    }

    attribute_map = {
        'certificate_rotate_strategy': 'certificateRotateStrategy',
        'configuration': 'configuration',
        'customize_components': 'customizeComponents',
        'image_pull_policy': 'imagePullPolicy',
        'image_pull_secrets': 'imagePullSecrets',
        'image_registry': 'imageRegistry',
        'image_tag': 'imageTag',
        'infra': 'infra',
        'monitor_account': 'monitorAccount',
        'monitor_namespace': 'monitorNamespace',
        'product_component': 'productComponent',
        'product_name': 'productName',
        'product_version': 'productVersion',
        'service_monitor_namespace': 'serviceMonitorNamespace',
        'synchronization_port': 'synchronizationPort',
        'uninstall_strategy': 'uninstallStrategy',
        'workload_update_strategy': 'workloadUpdateStrategy',
        'workloads': 'workloads'
    }

    def __init__(self, certificate_rotate_strategy=None, configuration=None, customize_components=None, image_pull_policy=None, image_pull_secrets=None, image_registry=None, image_tag=None, infra=None, monitor_account=None, monitor_namespace=None, product_component=None, product_name=None, product_version=None, service_monitor_namespace=None, synchronization_port=None, uninstall_strategy=None, workload_update_strategy=None, workloads=None):
        """
        V1KubeVirtSpec - a model defined in Swagger
        """

        self._certificate_rotate_strategy = None
        self._configuration = None
        self._customize_components = None
        self._image_pull_policy = None
        self._image_pull_secrets = None
        self._image_registry = None
        self._image_tag = None
        self._infra = None
        self._monitor_account = None
        self._monitor_namespace = None
        self._product_component = None
        self._product_name = None
        self._product_version = None
        self._service_monitor_namespace = None
        self._synchronization_port = None
        self._uninstall_strategy = None
        self._workload_update_strategy = None
        self._workloads = None

        if certificate_rotate_strategy is not None:
          self.certificate_rotate_strategy = certificate_rotate_strategy
        if configuration is not None:
          self.configuration = configuration
        if customize_components is not None:
          self.customize_components = customize_components
        if image_pull_policy is not None:
          self.image_pull_policy = image_pull_policy
        if image_pull_secrets is not None:
          self.image_pull_secrets = image_pull_secrets
        if image_registry is not None:
          self.image_registry = image_registry
        if image_tag is not None:
          self.image_tag = image_tag
        if infra is not None:
          self.infra = infra
        if monitor_account is not None:
          self.monitor_account = monitor_account
        if monitor_namespace is not None:
          self.monitor_namespace = monitor_namespace
        if product_component is not None:
          self.product_component = product_component
        if product_name is not None:
          self.product_name = product_name
        if product_version is not None:
          self.product_version = product_version
        if service_monitor_namespace is not None:
          self.service_monitor_namespace = service_monitor_namespace
        if synchronization_port is not None:
          self.synchronization_port = synchronization_port
        if uninstall_strategy is not None:
          self.uninstall_strategy = uninstall_strategy
        if workload_update_strategy is not None:
          self.workload_update_strategy = workload_update_strategy
        if workloads is not None:
          self.workloads = workloads

    @property
    def certificate_rotate_strategy(self):
        """
        Gets the certificate_rotate_strategy of this V1KubeVirtSpec.

        :return: The certificate_rotate_strategy of this V1KubeVirtSpec.
        :rtype: V1KubeVirtCertificateRotateStrategy
        """
        return self._certificate_rotate_strategy

    @certificate_rotate_strategy.setter
    def certificate_rotate_strategy(self, certificate_rotate_strategy):
        """
        Sets the certificate_rotate_strategy of this V1KubeVirtSpec.

        :param certificate_rotate_strategy: The certificate_rotate_strategy of this V1KubeVirtSpec.
        :type: V1KubeVirtCertificateRotateStrategy
        """

        self._certificate_rotate_strategy = certificate_rotate_strategy

    @property
    def configuration(self):
        """
        Gets the configuration of this V1KubeVirtSpec.
        holds kubevirt configurations. same as the virt-configMap

        :return: The configuration of this V1KubeVirtSpec.
        :rtype: V1KubeVirtConfiguration
        """
        return self._configuration

    @configuration.setter
    def configuration(self, configuration):
        """
        Sets the configuration of this V1KubeVirtSpec.
        holds kubevirt configurations. same as the virt-configMap

        :param configuration: The configuration of this V1KubeVirtSpec.
        :type: V1KubeVirtConfiguration
        """

        self._configuration = configuration

    @property
    def customize_components(self):
        """
        Gets the customize_components of this V1KubeVirtSpec.

        :return: The customize_components of this V1KubeVirtSpec.
        :rtype: V1CustomizeComponents
        """
        return self._customize_components

    @customize_components.setter
    def customize_components(self, customize_components):
        """
        Sets the customize_components of this V1KubeVirtSpec.

        :param customize_components: The customize_components of this V1KubeVirtSpec.
        :type: V1CustomizeComponents
        """

        self._customize_components = customize_components

    @property
    def image_pull_policy(self):
        """
        Gets the image_pull_policy of this V1KubeVirtSpec.
        The ImagePullPolicy to use.  Possible enum values:  - `\"Always\"` means that kubelet always attempts to pull the latest image. Container will fail If the pull fails.  - `\"IfNotPresent\"` means that kubelet pulls if the image isn't present on disk. Container will fail if the image isn't present and the pull fails.  - `\"Never\"` means that kubelet never pulls an image, but only uses a local image. Container will fail if the image isn't present

        :return: The image_pull_policy of this V1KubeVirtSpec.
        :rtype: str
        """
        return self._image_pull_policy

    @image_pull_policy.setter
    def image_pull_policy(self, image_pull_policy):
        """
        Sets the image_pull_policy of this V1KubeVirtSpec.
        The ImagePullPolicy to use.  Possible enum values:  - `\"Always\"` means that kubelet always attempts to pull the latest image. Container will fail If the pull fails.  - `\"IfNotPresent\"` means that kubelet pulls if the image isn't present on disk. Container will fail if the image isn't present and the pull fails.  - `\"Never\"` means that kubelet never pulls an image, but only uses a local image. Container will fail if the image isn't present

        :param image_pull_policy: The image_pull_policy of this V1KubeVirtSpec.
        :type: str
        """
        allowed_values = ["Always", "IfNotPresent", "Never"]
        if image_pull_policy not in allowed_values:
            raise ValueError(
                "Invalid value for `image_pull_policy` ({0}), must be one of {1}"
                .format(image_pull_policy, allowed_values)
            )

        self._image_pull_policy = image_pull_policy

    @property
    def image_pull_secrets(self):
        """
        Gets the image_pull_secrets of this V1KubeVirtSpec.
        The imagePullSecrets to pull the container images from Defaults to none

        :return: The image_pull_secrets of this V1KubeVirtSpec.
        :rtype: list[K8sIoApiCoreV1LocalObjectReference]
        """
        return self._image_pull_secrets

    @image_pull_secrets.setter
    def image_pull_secrets(self, image_pull_secrets):
        """
        Sets the image_pull_secrets of this V1KubeVirtSpec.
        The imagePullSecrets to pull the container images from Defaults to none

        :param image_pull_secrets: The image_pull_secrets of this V1KubeVirtSpec.
        :type: list[K8sIoApiCoreV1LocalObjectReference]
        """

        self._image_pull_secrets = image_pull_secrets

    @property
    def image_registry(self):
        """
        Gets the image_registry of this V1KubeVirtSpec.
        The image registry to pull the container images from Defaults to the same registry the operator's container image is pulled from.

        :return: The image_registry of this V1KubeVirtSpec.
        :rtype: str
        """
        return self._image_registry

    @image_registry.setter
    def image_registry(self, image_registry):
        """
        Sets the image_registry of this V1KubeVirtSpec.
        The image registry to pull the container images from Defaults to the same registry the operator's container image is pulled from.

        :param image_registry: The image_registry of this V1KubeVirtSpec.
        :type: str
        """

        self._image_registry = image_registry

    @property
    def image_tag(self):
        """
        Gets the image_tag of this V1KubeVirtSpec.
        The image tag to use for the continer images installed. Defaults to the same tag as the operator's container image.

        :return: The image_tag of this V1KubeVirtSpec.
        :rtype: str
        """
        return self._image_tag

    @image_tag.setter
    def image_tag(self, image_tag):
        """
        Sets the image_tag of this V1KubeVirtSpec.
        The image tag to use for the continer images installed. Defaults to the same tag as the operator's container image.

        :param image_tag: The image_tag of this V1KubeVirtSpec.
        :type: str
        """

        self._image_tag = image_tag

    @property
    def infra(self):
        """
        Gets the infra of this V1KubeVirtSpec.
        selectors and tolerations that should apply to KubeVirt infrastructure components

        :return: The infra of this V1KubeVirtSpec.
        :rtype: V1ComponentConfig
        """
        return self._infra

    @infra.setter
    def infra(self, infra):
        """
        Sets the infra of this V1KubeVirtSpec.
        selectors and tolerations that should apply to KubeVirt infrastructure components

        :param infra: The infra of this V1KubeVirtSpec.
        :type: V1ComponentConfig
        """

        self._infra = infra

    @property
    def monitor_account(self):
        """
        Gets the monitor_account of this V1KubeVirtSpec.
        The name of the Prometheus service account that needs read-access to KubeVirt endpoints Defaults to prometheus-k8s

        :return: The monitor_account of this V1KubeVirtSpec.
        :rtype: str
        """
        return self._monitor_account

    @monitor_account.setter
    def monitor_account(self, monitor_account):
        """
        Sets the monitor_account of this V1KubeVirtSpec.
        The name of the Prometheus service account that needs read-access to KubeVirt endpoints Defaults to prometheus-k8s

        :param monitor_account: The monitor_account of this V1KubeVirtSpec.
        :type: str
        """

        self._monitor_account = monitor_account

    @property
    def monitor_namespace(self):
        """
        Gets the monitor_namespace of this V1KubeVirtSpec.
        The namespace Prometheus is deployed in Defaults to openshift-monitor

        :return: The monitor_namespace of this V1KubeVirtSpec.
        :rtype: str
        """
        return self._monitor_namespace

    @monitor_namespace.setter
    def monitor_namespace(self, monitor_namespace):
        """
        Sets the monitor_namespace of this V1KubeVirtSpec.
        The namespace Prometheus is deployed in Defaults to openshift-monitor

        :param monitor_namespace: The monitor_namespace of this V1KubeVirtSpec.
        :type: str
        """

        self._monitor_namespace = monitor_namespace

    @property
    def product_component(self):
        """
        Gets the product_component of this V1KubeVirtSpec.
        Designate the apps.kubevirt.io/component label for KubeVirt components. Useful if KubeVirt is included as part of a product. If ProductComponent is not specified, the component label default value is kubevirt.

        :return: The product_component of this V1KubeVirtSpec.
        :rtype: str
        """
        return self._product_component

    @product_component.setter
    def product_component(self, product_component):
        """
        Sets the product_component of this V1KubeVirtSpec.
        Designate the apps.kubevirt.io/component label for KubeVirt components. Useful if KubeVirt is included as part of a product. If ProductComponent is not specified, the component label default value is kubevirt.

        :param product_component: The product_component of this V1KubeVirtSpec.
        :type: str
        """

        self._product_component = product_component

    @property
    def product_name(self):
        """
        Gets the product_name of this V1KubeVirtSpec.
        Designate the apps.kubevirt.io/part-of label for KubeVirt components. Useful if KubeVirt is included as part of a product. If ProductName is not specified, the part-of label will be omitted.

        :return: The product_name of this V1KubeVirtSpec.
        :rtype: str
        """
        return self._product_name

    @product_name.setter
    def product_name(self, product_name):
        """
        Sets the product_name of this V1KubeVirtSpec.
        Designate the apps.kubevirt.io/part-of label for KubeVirt components. Useful if KubeVirt is included as part of a product. If ProductName is not specified, the part-of label will be omitted.

        :param product_name: The product_name of this V1KubeVirtSpec.
        :type: str
        """

        self._product_name = product_name

    @property
    def product_version(self):
        """
        Gets the product_version of this V1KubeVirtSpec.
        Designate the apps.kubevirt.io/version label for KubeVirt components. Useful if KubeVirt is included as part of a product. If ProductVersion is not specified, KubeVirt's version will be used.

        :return: The product_version of this V1KubeVirtSpec.
        :rtype: str
        """
        return self._product_version

    @product_version.setter
    def product_version(self, product_version):
        """
        Sets the product_version of this V1KubeVirtSpec.
        Designate the apps.kubevirt.io/version label for KubeVirt components. Useful if KubeVirt is included as part of a product. If ProductVersion is not specified, KubeVirt's version will be used.

        :param product_version: The product_version of this V1KubeVirtSpec.
        :type: str
        """

        self._product_version = product_version

    @property
    def service_monitor_namespace(self):
        """
        Gets the service_monitor_namespace of this V1KubeVirtSpec.
        The namespace the service monitor will be deployed  When ServiceMonitorNamespace is set, then we'll install the service monitor object in that namespace otherwise we will use the monitoring namespace.

        :return: The service_monitor_namespace of this V1KubeVirtSpec.
        :rtype: str
        """
        return self._service_monitor_namespace

    @service_monitor_namespace.setter
    def service_monitor_namespace(self, service_monitor_namespace):
        """
        Sets the service_monitor_namespace of this V1KubeVirtSpec.
        The namespace the service monitor will be deployed  When ServiceMonitorNamespace is set, then we'll install the service monitor object in that namespace otherwise we will use the monitoring namespace.

        :param service_monitor_namespace: The service_monitor_namespace of this V1KubeVirtSpec.
        :type: str
        """

        self._service_monitor_namespace = service_monitor_namespace

    @property
    def synchronization_port(self):
        """
        Gets the synchronization_port of this V1KubeVirtSpec.
        Specify the port to listen on for VMI status synchronization traffic. Default is 9185

        :return: The synchronization_port of this V1KubeVirtSpec.
        :rtype: str
        """
        return self._synchronization_port

    @synchronization_port.setter
    def synchronization_port(self, synchronization_port):
        """
        Sets the synchronization_port of this V1KubeVirtSpec.
        Specify the port to listen on for VMI status synchronization traffic. Default is 9185

        :param synchronization_port: The synchronization_port of this V1KubeVirtSpec.
        :type: str
        """

        self._synchronization_port = synchronization_port

    @property
    def uninstall_strategy(self):
        """
        Gets the uninstall_strategy of this V1KubeVirtSpec.
        Specifies if kubevirt can be deleted if workloads are still present. This is mainly a precaution to avoid accidental data loss

        :return: The uninstall_strategy of this V1KubeVirtSpec.
        :rtype: str
        """
        return self._uninstall_strategy

    @uninstall_strategy.setter
    def uninstall_strategy(self, uninstall_strategy):
        """
        Sets the uninstall_strategy of this V1KubeVirtSpec.
        Specifies if kubevirt can be deleted if workloads are still present. This is mainly a precaution to avoid accidental data loss

        :param uninstall_strategy: The uninstall_strategy of this V1KubeVirtSpec.
        :type: str
        """

        self._uninstall_strategy = uninstall_strategy

    @property
    def workload_update_strategy(self):
        """
        Gets the workload_update_strategy of this V1KubeVirtSpec.
        WorkloadUpdateStrategy defines at the cluster level how to handle automated workload updates

        :return: The workload_update_strategy of this V1KubeVirtSpec.
        :rtype: V1KubeVirtWorkloadUpdateStrategy
        """
        return self._workload_update_strategy

    @workload_update_strategy.setter
    def workload_update_strategy(self, workload_update_strategy):
        """
        Sets the workload_update_strategy of this V1KubeVirtSpec.
        WorkloadUpdateStrategy defines at the cluster level how to handle automated workload updates

        :param workload_update_strategy: The workload_update_strategy of this V1KubeVirtSpec.
        :type: V1KubeVirtWorkloadUpdateStrategy
        """

        self._workload_update_strategy = workload_update_strategy

    @property
    def workloads(self):
        """
        Gets the workloads of this V1KubeVirtSpec.
        selectors and tolerations that should apply to KubeVirt workloads

        :return: The workloads of this V1KubeVirtSpec.
        :rtype: V1ComponentConfig
        """
        return self._workloads

    @workloads.setter
    def workloads(self, workloads):
        """
        Sets the workloads of this V1KubeVirtSpec.
        selectors and tolerations that should apply to KubeVirt workloads

        :param workloads: The workloads of this V1KubeVirtSpec.
        :type: V1ComponentConfig
        """

        self._workloads = workloads

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, V1KubeVirtSpec):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
