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


class V1VirtualMachineInstanceMigrationSpec(object):
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
        'added_node_selector': 'dict(str, str)',
        'receive': 'V1VirtualMachineInstanceMigrationTarget',
        'send_to': 'V1VirtualMachineInstanceMigrationSource',
        'vmi_name': 'str'
    }

    attribute_map = {
        'added_node_selector': 'addedNodeSelector',
        'receive': 'receive',
        'send_to': 'sendTo',
        'vmi_name': 'vmiName'
    }

    def __init__(self, added_node_selector=None, receive=None, send_to=None, vmi_name=None):
        """
        V1VirtualMachineInstanceMigrationSpec - a model defined in Swagger
        """

        self._added_node_selector = None
        self._receive = None
        self._send_to = None
        self._vmi_name = None

        if added_node_selector is not None:
          self.added_node_selector = added_node_selector
        if receive is not None:
          self.receive = receive
        if send_to is not None:
          self.send_to = send_to
        if vmi_name is not None:
          self.vmi_name = vmi_name

    @property
    def added_node_selector(self):
        """
        Gets the added_node_selector of this V1VirtualMachineInstanceMigrationSpec.
        AddedNodeSelector is an additional selector that can be used to complement a NodeSelector or NodeAffinity as set on the VM to restrict the set of allowed target nodes for a migration. In case of key collisions, values set on the VM objects are going to be preserved to ensure that addedNodeSelector can only restrict but not bypass constraints already set on the VM object.

        :return: The added_node_selector of this V1VirtualMachineInstanceMigrationSpec.
        :rtype: dict(str, str)
        """
        return self._added_node_selector

    @added_node_selector.setter
    def added_node_selector(self, added_node_selector):
        """
        Sets the added_node_selector of this V1VirtualMachineInstanceMigrationSpec.
        AddedNodeSelector is an additional selector that can be used to complement a NodeSelector or NodeAffinity as set on the VM to restrict the set of allowed target nodes for a migration. In case of key collisions, values set on the VM objects are going to be preserved to ensure that addedNodeSelector can only restrict but not bypass constraints already set on the VM object.

        :param added_node_selector: The added_node_selector of this V1VirtualMachineInstanceMigrationSpec.
        :type: dict(str, str)
        """

        self._added_node_selector = added_node_selector

    @property
    def receive(self):
        """
        Gets the receive of this V1VirtualMachineInstanceMigrationSpec.
        If receieve is specified, this VirtualMachineInstanceMigration will be considered the target

        :return: The receive of this V1VirtualMachineInstanceMigrationSpec.
        :rtype: V1VirtualMachineInstanceMigrationTarget
        """
        return self._receive

    @receive.setter
    def receive(self, receive):
        """
        Sets the receive of this V1VirtualMachineInstanceMigrationSpec.
        If receieve is specified, this VirtualMachineInstanceMigration will be considered the target

        :param receive: The receive of this V1VirtualMachineInstanceMigrationSpec.
        :type: V1VirtualMachineInstanceMigrationTarget
        """

        self._receive = receive

    @property
    def send_to(self):
        """
        Gets the send_to of this V1VirtualMachineInstanceMigrationSpec.
        If sendTo is specified, this VirtualMachineInstanceMigration will be considered the source

        :return: The send_to of this V1VirtualMachineInstanceMigrationSpec.
        :rtype: V1VirtualMachineInstanceMigrationSource
        """
        return self._send_to

    @send_to.setter
    def send_to(self, send_to):
        """
        Sets the send_to of this V1VirtualMachineInstanceMigrationSpec.
        If sendTo is specified, this VirtualMachineInstanceMigration will be considered the source

        :param send_to: The send_to of this V1VirtualMachineInstanceMigrationSpec.
        :type: V1VirtualMachineInstanceMigrationSource
        """

        self._send_to = send_to

    @property
    def vmi_name(self):
        """
        Gets the vmi_name of this V1VirtualMachineInstanceMigrationSpec.
        The name of the VMI to perform the migration on. VMI must exist in the migration objects namespace

        :return: The vmi_name of this V1VirtualMachineInstanceMigrationSpec.
        :rtype: str
        """
        return self._vmi_name

    @vmi_name.setter
    def vmi_name(self, vmi_name):
        """
        Sets the vmi_name of this V1VirtualMachineInstanceMigrationSpec.
        The name of the VMI to perform the migration on. VMI must exist in the migration objects namespace

        :param vmi_name: The vmi_name of this V1VirtualMachineInstanceMigrationSpec.
        :type: str
        """

        self._vmi_name = vmi_name

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
        if not isinstance(other, V1VirtualMachineInstanceMigrationSpec):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
