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


class V1DeviceStatus(object):
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
        'gpu_statuses': 'list[V1DeviceStatusInfo]',
        'host_device_statuses': 'list[V1DeviceStatusInfo]'
    }

    attribute_map = {
        'gpu_statuses': 'gpuStatuses',
        'host_device_statuses': 'hostDeviceStatuses'
    }

    def __init__(self, gpu_statuses=None, host_device_statuses=None):
        """
        V1DeviceStatus - a model defined in Swagger
        """

        self._gpu_statuses = None
        self._host_device_statuses = None

        if gpu_statuses is not None:
          self.gpu_statuses = gpu_statuses
        if host_device_statuses is not None:
          self.host_device_statuses = host_device_statuses

    @property
    def gpu_statuses(self):
        """
        Gets the gpu_statuses of this V1DeviceStatus.
        GPUStatuses reflects the state of GPUs requested in spec.domain.devices.gpus

        :return: The gpu_statuses of this V1DeviceStatus.
        :rtype: list[V1DeviceStatusInfo]
        """
        return self._gpu_statuses

    @gpu_statuses.setter
    def gpu_statuses(self, gpu_statuses):
        """
        Sets the gpu_statuses of this V1DeviceStatus.
        GPUStatuses reflects the state of GPUs requested in spec.domain.devices.gpus

        :param gpu_statuses: The gpu_statuses of this V1DeviceStatus.
        :type: list[V1DeviceStatusInfo]
        """

        self._gpu_statuses = gpu_statuses

    @property
    def host_device_statuses(self):
        """
        Gets the host_device_statuses of this V1DeviceStatus.
        HostDeviceStatuses reflects the state of GPUs requested in spec.domain.devices.hostDevices DRA

        :return: The host_device_statuses of this V1DeviceStatus.
        :rtype: list[V1DeviceStatusInfo]
        """
        return self._host_device_statuses

    @host_device_statuses.setter
    def host_device_statuses(self, host_device_statuses):
        """
        Sets the host_device_statuses of this V1DeviceStatus.
        HostDeviceStatuses reflects the state of GPUs requested in spec.domain.devices.hostDevices DRA

        :param host_device_statuses: The host_device_statuses of this V1DeviceStatus.
        :type: list[V1DeviceStatusInfo]
        """

        self._host_device_statuses = host_device_statuses

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
        if not isinstance(other, V1DeviceStatus):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
