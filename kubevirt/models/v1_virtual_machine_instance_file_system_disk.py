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


class V1VirtualMachineInstanceFileSystemDisk(object):
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
        'bus_type': 'str',
        'serial': 'str'
    }

    attribute_map = {
        'bus_type': 'bus-type',
        'serial': 'serial'
    }

    def __init__(self, bus_type='', serial=''):
        """
        V1VirtualMachineInstanceFileSystemDisk - a model defined in Swagger
        """

        self._bus_type = None
        self._serial = None

        self.bus_type = bus_type
        self.serial = serial

    @property
    def bus_type(self):
        """
        Gets the bus_type of this V1VirtualMachineInstanceFileSystemDisk.

        :return: The bus_type of this V1VirtualMachineInstanceFileSystemDisk.
        :rtype: str
        """
        return self._bus_type

    @bus_type.setter
    def bus_type(self, bus_type):
        """
        Sets the bus_type of this V1VirtualMachineInstanceFileSystemDisk.

        :param bus_type: The bus_type of this V1VirtualMachineInstanceFileSystemDisk.
        :type: str
        """
        if bus_type is None:
            raise ValueError("Invalid value for `bus_type`, must not be `None`")

        self._bus_type = bus_type

    @property
    def serial(self):
        """
        Gets the serial of this V1VirtualMachineInstanceFileSystemDisk.

        :return: The serial of this V1VirtualMachineInstanceFileSystemDisk.
        :rtype: str
        """
        return self._serial

    @serial.setter
    def serial(self, serial):
        """
        Sets the serial of this V1VirtualMachineInstanceFileSystemDisk.

        :param serial: The serial of this V1VirtualMachineInstanceFileSystemDisk.
        :type: str
        """
        if serial is None:
            raise ValueError("Invalid value for `serial`, must not be `None`")

        self._serial = serial

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
        if not isinstance(other, V1VirtualMachineInstanceFileSystemDisk):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other