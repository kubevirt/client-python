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


class V1alpha1VirtualMachineCloneSpec(object):
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
        'annotation_filters': 'list[str]',
        'label_filters': 'list[str]',
        'new_mac_addresses': 'dict(str, str)',
        'new_sm_bios_serial': 'str',
        'source': 'K8sIoApiCoreV1TypedLocalObjectReference',
        'target': 'K8sIoApiCoreV1TypedLocalObjectReference'
    }

    attribute_map = {
        'annotation_filters': 'annotationFilters',
        'label_filters': 'labelFilters',
        'new_mac_addresses': 'newMacAddresses',
        'new_sm_bios_serial': 'newSMBiosSerial',
        'source': 'source',
        'target': 'target'
    }

    def __init__(self, annotation_filters=None, label_filters=None, new_mac_addresses=None, new_sm_bios_serial=None, source=None, target=None):
        """
        V1alpha1VirtualMachineCloneSpec - a model defined in Swagger
        """

        self._annotation_filters = None
        self._label_filters = None
        self._new_mac_addresses = None
        self._new_sm_bios_serial = None
        self._source = None
        self._target = None

        if annotation_filters is not None:
          self.annotation_filters = annotation_filters
        if label_filters is not None:
          self.label_filters = label_filters
        if new_mac_addresses is not None:
          self.new_mac_addresses = new_mac_addresses
        if new_sm_bios_serial is not None:
          self.new_sm_bios_serial = new_sm_bios_serial
        self.source = source
        if target is not None:
          self.target = target

    @property
    def annotation_filters(self):
        """
        Gets the annotation_filters of this V1alpha1VirtualMachineCloneSpec.

        :return: The annotation_filters of this V1alpha1VirtualMachineCloneSpec.
        :rtype: list[str]
        """
        return self._annotation_filters

    @annotation_filters.setter
    def annotation_filters(self, annotation_filters):
        """
        Sets the annotation_filters of this V1alpha1VirtualMachineCloneSpec.

        :param annotation_filters: The annotation_filters of this V1alpha1VirtualMachineCloneSpec.
        :type: list[str]
        """

        self._annotation_filters = annotation_filters

    @property
    def label_filters(self):
        """
        Gets the label_filters of this V1alpha1VirtualMachineCloneSpec.

        :return: The label_filters of this V1alpha1VirtualMachineCloneSpec.
        :rtype: list[str]
        """
        return self._label_filters

    @label_filters.setter
    def label_filters(self, label_filters):
        """
        Sets the label_filters of this V1alpha1VirtualMachineCloneSpec.

        :param label_filters: The label_filters of this V1alpha1VirtualMachineCloneSpec.
        :type: list[str]
        """

        self._label_filters = label_filters

    @property
    def new_mac_addresses(self):
        """
        Gets the new_mac_addresses of this V1alpha1VirtualMachineCloneSpec.
        NewMacAddresses manually sets that target interfaces' mac addresses. The key is the interface name and the value is the new mac address. If this field is not specified, a new MAC address will be generated automatically, as for any interface that is not included in this map.

        :return: The new_mac_addresses of this V1alpha1VirtualMachineCloneSpec.
        :rtype: dict(str, str)
        """
        return self._new_mac_addresses

    @new_mac_addresses.setter
    def new_mac_addresses(self, new_mac_addresses):
        """
        Sets the new_mac_addresses of this V1alpha1VirtualMachineCloneSpec.
        NewMacAddresses manually sets that target interfaces' mac addresses. The key is the interface name and the value is the new mac address. If this field is not specified, a new MAC address will be generated automatically, as for any interface that is not included in this map.

        :param new_mac_addresses: The new_mac_addresses of this V1alpha1VirtualMachineCloneSpec.
        :type: dict(str, str)
        """

        self._new_mac_addresses = new_mac_addresses

    @property
    def new_sm_bios_serial(self):
        """
        Gets the new_sm_bios_serial of this V1alpha1VirtualMachineCloneSpec.
        NewSMBiosSerial manually sets that target's SMbios serial. If this field is not specified, a new serial will be generated automatically.

        :return: The new_sm_bios_serial of this V1alpha1VirtualMachineCloneSpec.
        :rtype: str
        """
        return self._new_sm_bios_serial

    @new_sm_bios_serial.setter
    def new_sm_bios_serial(self, new_sm_bios_serial):
        """
        Sets the new_sm_bios_serial of this V1alpha1VirtualMachineCloneSpec.
        NewSMBiosSerial manually sets that target's SMbios serial. If this field is not specified, a new serial will be generated automatically.

        :param new_sm_bios_serial: The new_sm_bios_serial of this V1alpha1VirtualMachineCloneSpec.
        :type: str
        """

        self._new_sm_bios_serial = new_sm_bios_serial

    @property
    def source(self):
        """
        Gets the source of this V1alpha1VirtualMachineCloneSpec.

        :return: The source of this V1alpha1VirtualMachineCloneSpec.
        :rtype: K8sIoApiCoreV1TypedLocalObjectReference
        """
        return self._source

    @source.setter
    def source(self, source):
        """
        Sets the source of this V1alpha1VirtualMachineCloneSpec.

        :param source: The source of this V1alpha1VirtualMachineCloneSpec.
        :type: K8sIoApiCoreV1TypedLocalObjectReference
        """
        if source is None:
            raise ValueError("Invalid value for `source`, must not be `None`")

        self._source = source

    @property
    def target(self):
        """
        Gets the target of this V1alpha1VirtualMachineCloneSpec.
        If the target is not provided, a random name would be generated for the target. The target's name can be viewed by inspecting status \"TargetName\" field below.

        :return: The target of this V1alpha1VirtualMachineCloneSpec.
        :rtype: K8sIoApiCoreV1TypedLocalObjectReference
        """
        return self._target

    @target.setter
    def target(self, target):
        """
        Sets the target of this V1alpha1VirtualMachineCloneSpec.
        If the target is not provided, a random name would be generated for the target. The target's name can be viewed by inspecting status \"TargetName\" field below.

        :param target: The target of this V1alpha1VirtualMachineCloneSpec.
        :type: K8sIoApiCoreV1TypedLocalObjectReference
        """

        self._target = target

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
        if not isinstance(other, V1alpha1VirtualMachineCloneSpec):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
