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


class V1alpha1VirtualMachinePoolNameGeneration(object):
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
        'append_index_to_config_map_refs': 'bool',
        'append_index_to_secret_refs': 'bool'
    }

    attribute_map = {
        'append_index_to_config_map_refs': 'appendIndexToConfigMapRefs',
        'append_index_to_secret_refs': 'appendIndexToSecretRefs'
    }

    def __init__(self, append_index_to_config_map_refs=None, append_index_to_secret_refs=None):
        """
        V1alpha1VirtualMachinePoolNameGeneration - a model defined in Swagger
        """

        self._append_index_to_config_map_refs = None
        self._append_index_to_secret_refs = None

        if append_index_to_config_map_refs is not None:
          self.append_index_to_config_map_refs = append_index_to_config_map_refs
        if append_index_to_secret_refs is not None:
          self.append_index_to_secret_refs = append_index_to_secret_refs

    @property
    def append_index_to_config_map_refs(self):
        """
        Gets the append_index_to_config_map_refs of this V1alpha1VirtualMachinePoolNameGeneration.

        :return: The append_index_to_config_map_refs of this V1alpha1VirtualMachinePoolNameGeneration.
        :rtype: bool
        """
        return self._append_index_to_config_map_refs

    @append_index_to_config_map_refs.setter
    def append_index_to_config_map_refs(self, append_index_to_config_map_refs):
        """
        Sets the append_index_to_config_map_refs of this V1alpha1VirtualMachinePoolNameGeneration.

        :param append_index_to_config_map_refs: The append_index_to_config_map_refs of this V1alpha1VirtualMachinePoolNameGeneration.
        :type: bool
        """

        self._append_index_to_config_map_refs = append_index_to_config_map_refs

    @property
    def append_index_to_secret_refs(self):
        """
        Gets the append_index_to_secret_refs of this V1alpha1VirtualMachinePoolNameGeneration.

        :return: The append_index_to_secret_refs of this V1alpha1VirtualMachinePoolNameGeneration.
        :rtype: bool
        """
        return self._append_index_to_secret_refs

    @append_index_to_secret_refs.setter
    def append_index_to_secret_refs(self, append_index_to_secret_refs):
        """
        Sets the append_index_to_secret_refs of this V1alpha1VirtualMachinePoolNameGeneration.

        :param append_index_to_secret_refs: The append_index_to_secret_refs of this V1alpha1VirtualMachinePoolNameGeneration.
        :type: bool
        """

        self._append_index_to_secret_refs = append_index_to_secret_refs

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
        if not isinstance(other, V1alpha1VirtualMachinePoolNameGeneration):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
