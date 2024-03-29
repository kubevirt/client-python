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


class V1CustomBlockSize(object):
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
        'logical': 'int',
        'physical': 'int'
    }

    attribute_map = {
        'logical': 'logical',
        'physical': 'physical'
    }

    def __init__(self, logical=0, physical=0):
        """
        V1CustomBlockSize - a model defined in Swagger
        """

        self._logical = None
        self._physical = None

        self.logical = logical
        self.physical = physical

    @property
    def logical(self):
        """
        Gets the logical of this V1CustomBlockSize.

        :return: The logical of this V1CustomBlockSize.
        :rtype: int
        """
        return self._logical

    @logical.setter
    def logical(self, logical):
        """
        Sets the logical of this V1CustomBlockSize.

        :param logical: The logical of this V1CustomBlockSize.
        :type: int
        """
        if logical is None:
            raise ValueError("Invalid value for `logical`, must not be `None`")

        self._logical = logical

    @property
    def physical(self):
        """
        Gets the physical of this V1CustomBlockSize.

        :return: The physical of this V1CustomBlockSize.
        :rtype: int
        """
        return self._physical

    @physical.setter
    def physical(self, physical):
        """
        Sets the physical of this V1CustomBlockSize.

        :param physical: The physical of this V1CustomBlockSize.
        :type: int
        """
        if physical is None:
            raise ValueError("Invalid value for `physical`, must not be `None`")

        self._physical = physical

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
        if not isinstance(other, V1CustomBlockSize):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
