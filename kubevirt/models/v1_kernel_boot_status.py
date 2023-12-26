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


class V1KernelBootStatus(object):
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
        'initrd_info': 'V1InitrdInfo',
        'kernel_info': 'V1KernelInfo'
    }

    attribute_map = {
        'initrd_info': 'initrdInfo',
        'kernel_info': 'kernelInfo'
    }

    def __init__(self, initrd_info=None, kernel_info=None):
        """
        V1KernelBootStatus - a model defined in Swagger
        """

        self._initrd_info = None
        self._kernel_info = None

        if initrd_info is not None:
          self.initrd_info = initrd_info
        if kernel_info is not None:
          self.kernel_info = kernel_info

    @property
    def initrd_info(self):
        """
        Gets the initrd_info of this V1KernelBootStatus.
        InitrdInfo show info about the initrd file

        :return: The initrd_info of this V1KernelBootStatus.
        :rtype: V1InitrdInfo
        """
        return self._initrd_info

    @initrd_info.setter
    def initrd_info(self, initrd_info):
        """
        Sets the initrd_info of this V1KernelBootStatus.
        InitrdInfo show info about the initrd file

        :param initrd_info: The initrd_info of this V1KernelBootStatus.
        :type: V1InitrdInfo
        """

        self._initrd_info = initrd_info

    @property
    def kernel_info(self):
        """
        Gets the kernel_info of this V1KernelBootStatus.
        KernelInfo show info about the kernel image

        :return: The kernel_info of this V1KernelBootStatus.
        :rtype: V1KernelInfo
        """
        return self._kernel_info

    @kernel_info.setter
    def kernel_info(self, kernel_info):
        """
        Sets the kernel_info of this V1KernelBootStatus.
        KernelInfo show info about the kernel image

        :param kernel_info: The kernel_info of this V1KernelBootStatus.
        :type: V1KernelInfo
        """

        self._kernel_info = kernel_info

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
        if not isinstance(other, V1KernelBootStatus):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other