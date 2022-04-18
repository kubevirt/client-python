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


class V1alpha1VirtualMachinePoolSpec(object):
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
        'paused': 'bool',
        'replicas': 'int',
        'selector': 'K8sIoApimachineryPkgApisMetaV1LabelSelector',
        'virtual_machine_template': 'V1alpha1VirtualMachineTemplateSpec'
    }

    attribute_map = {
        'paused': 'paused',
        'replicas': 'replicas',
        'selector': 'selector',
        'virtual_machine_template': 'virtualMachineTemplate'
    }

    def __init__(self, paused=None, replicas=None, selector=None, virtual_machine_template=None):
        """
        V1alpha1VirtualMachinePoolSpec - a model defined in Swagger
        """

        self._paused = None
        self._replicas = None
        self._selector = None
        self._virtual_machine_template = None

        if paused is not None:
          self.paused = paused
        if replicas is not None:
          self.replicas = replicas
        self.selector = selector
        self.virtual_machine_template = virtual_machine_template

    @property
    def paused(self):
        """
        Gets the paused of this V1alpha1VirtualMachinePoolSpec.
        Indicates that the pool is paused.

        :return: The paused of this V1alpha1VirtualMachinePoolSpec.
        :rtype: bool
        """
        return self._paused

    @paused.setter
    def paused(self, paused):
        """
        Sets the paused of this V1alpha1VirtualMachinePoolSpec.
        Indicates that the pool is paused.

        :param paused: The paused of this V1alpha1VirtualMachinePoolSpec.
        :type: bool
        """

        self._paused = paused

    @property
    def replicas(self):
        """
        Gets the replicas of this V1alpha1VirtualMachinePoolSpec.
        Number of desired pods. This is a pointer to distinguish between explicit zero and not specified. Defaults to 1.

        :return: The replicas of this V1alpha1VirtualMachinePoolSpec.
        :rtype: int
        """
        return self._replicas

    @replicas.setter
    def replicas(self, replicas):
        """
        Sets the replicas of this V1alpha1VirtualMachinePoolSpec.
        Number of desired pods. This is a pointer to distinguish between explicit zero and not specified. Defaults to 1.

        :param replicas: The replicas of this V1alpha1VirtualMachinePoolSpec.
        :type: int
        """

        self._replicas = replicas

    @property
    def selector(self):
        """
        Gets the selector of this V1alpha1VirtualMachinePoolSpec.
        Label selector for pods. Existing Poolss whose pods are selected by this will be the ones affected by this deployment.

        :return: The selector of this V1alpha1VirtualMachinePoolSpec.
        :rtype: K8sIoApimachineryPkgApisMetaV1LabelSelector
        """
        return self._selector

    @selector.setter
    def selector(self, selector):
        """
        Sets the selector of this V1alpha1VirtualMachinePoolSpec.
        Label selector for pods. Existing Poolss whose pods are selected by this will be the ones affected by this deployment.

        :param selector: The selector of this V1alpha1VirtualMachinePoolSpec.
        :type: K8sIoApimachineryPkgApisMetaV1LabelSelector
        """
        if selector is None:
            raise ValueError("Invalid value for `selector`, must not be `None`")

        self._selector = selector

    @property
    def virtual_machine_template(self):
        """
        Gets the virtual_machine_template of this V1alpha1VirtualMachinePoolSpec.
        Template describes the VM that will be created.

        :return: The virtual_machine_template of this V1alpha1VirtualMachinePoolSpec.
        :rtype: V1alpha1VirtualMachineTemplateSpec
        """
        return self._virtual_machine_template

    @virtual_machine_template.setter
    def virtual_machine_template(self, virtual_machine_template):
        """
        Sets the virtual_machine_template of this V1alpha1VirtualMachinePoolSpec.
        Template describes the VM that will be created.

        :param virtual_machine_template: The virtual_machine_template of this V1alpha1VirtualMachinePoolSpec.
        :type: V1alpha1VirtualMachineTemplateSpec
        """
        if virtual_machine_template is None:
            raise ValueError("Invalid value for `virtual_machine_template`, must not be `None`")

        self._virtual_machine_template = virtual_machine_template

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
        if not isinstance(other, V1alpha1VirtualMachinePoolSpec):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other