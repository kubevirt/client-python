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


class V1VirtualMachineOptions(object):
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
        'disable_free_page_reporting': 'V1DisableFreePageReporting',
        'disable_serial_console_log': 'V1DisableSerialConsoleLog'
    }

    attribute_map = {
        'disable_free_page_reporting': 'disableFreePageReporting',
        'disable_serial_console_log': 'disableSerialConsoleLog'
    }

    def __init__(self, disable_free_page_reporting=None, disable_serial_console_log=None):
        """
        V1VirtualMachineOptions - a model defined in Swagger
        """

        self._disable_free_page_reporting = None
        self._disable_serial_console_log = None

        if disable_free_page_reporting is not None:
          self.disable_free_page_reporting = disable_free_page_reporting
        if disable_serial_console_log is not None:
          self.disable_serial_console_log = disable_serial_console_log

    @property
    def disable_free_page_reporting(self):
        """
        Gets the disable_free_page_reporting of this V1VirtualMachineOptions.
        DisableFreePageReporting disable the free page reporting of memory balloon device https://libvirt.org/formatdomain.html#memory-balloon-device. This will have effect only if AutoattachMemBalloon is not false and the vmi is not requesting any high performance feature (dedicatedCPU/realtime/hugePages), in which free page reporting is always disabled.

        :return: The disable_free_page_reporting of this V1VirtualMachineOptions.
        :rtype: V1DisableFreePageReporting
        """
        return self._disable_free_page_reporting

    @disable_free_page_reporting.setter
    def disable_free_page_reporting(self, disable_free_page_reporting):
        """
        Sets the disable_free_page_reporting of this V1VirtualMachineOptions.
        DisableFreePageReporting disable the free page reporting of memory balloon device https://libvirt.org/formatdomain.html#memory-balloon-device. This will have effect only if AutoattachMemBalloon is not false and the vmi is not requesting any high performance feature (dedicatedCPU/realtime/hugePages), in which free page reporting is always disabled.

        :param disable_free_page_reporting: The disable_free_page_reporting of this V1VirtualMachineOptions.
        :type: V1DisableFreePageReporting
        """

        self._disable_free_page_reporting = disable_free_page_reporting

    @property
    def disable_serial_console_log(self):
        """
        Gets the disable_serial_console_log of this V1VirtualMachineOptions.
        DisableSerialConsoleLog disables logging the auto-attached default serial console. If not set, serial console logs will be written to a file and then streamed from a container named `guest-console-log`. The value can be individually overridden for each VM, not relevant if AutoattachSerialConsole is disabled.

        :return: The disable_serial_console_log of this V1VirtualMachineOptions.
        :rtype: V1DisableSerialConsoleLog
        """
        return self._disable_serial_console_log

    @disable_serial_console_log.setter
    def disable_serial_console_log(self, disable_serial_console_log):
        """
        Sets the disable_serial_console_log of this V1VirtualMachineOptions.
        DisableSerialConsoleLog disables logging the auto-attached default serial console. If not set, serial console logs will be written to a file and then streamed from a container named `guest-console-log`. The value can be individually overridden for each VM, not relevant if AutoattachSerialConsole is disabled.

        :param disable_serial_console_log: The disable_serial_console_log of this V1VirtualMachineOptions.
        :type: V1DisableSerialConsoleLog
        """

        self._disable_serial_console_log = disable_serial_console_log

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
        if not isinstance(other, V1VirtualMachineOptions):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
