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


class V1VirtualMachineInstanceProfile(object):
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
        'custom_profile': 'V1CustomProfile'
    }

    attribute_map = {
        'custom_profile': 'customProfile'
    }

    def __init__(self, custom_profile=None):
        """
        V1VirtualMachineInstanceProfile - a model defined in Swagger
        """

        self._custom_profile = None

        if custom_profile is not None:
          self.custom_profile = custom_profile

    @property
    def custom_profile(self):
        """
        Gets the custom_profile of this V1VirtualMachineInstanceProfile.
        CustomProfile allows to request arbitrary profile for virt-launcher

        :return: The custom_profile of this V1VirtualMachineInstanceProfile.
        :rtype: V1CustomProfile
        """
        return self._custom_profile

    @custom_profile.setter
    def custom_profile(self, custom_profile):
        """
        Sets the custom_profile of this V1VirtualMachineInstanceProfile.
        CustomProfile allows to request arbitrary profile for virt-launcher

        :param custom_profile: The custom_profile of this V1VirtualMachineInstanceProfile.
        :type: V1CustomProfile
        """

        self._custom_profile = custom_profile

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
        if not isinstance(other, V1VirtualMachineInstanceProfile):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
