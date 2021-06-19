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


class V1VirtualMachineInstanceStatus(object):
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
        'active_pods': 'dict(str, str)',
        'conditions': 'list[V1VirtualMachineInstanceCondition]',
        'evacuation_node_name': 'str',
        'fs_freeze_status': 'str',
        'guest_os_info': 'V1VirtualMachineInstanceGuestOSInfo',
        'interfaces': 'list[V1VirtualMachineInstanceNetworkInterface]',
        'launcher_container_image_version': 'str',
        'migration_method': 'str',
        'migration_state': 'V1VirtualMachineInstanceMigrationState',
        'node_name': 'str',
        'phase': 'str',
        'phase_transition_timestamps': 'list[V1VirtualMachineInstancePhaseTransitionTimestamp]',
        'qos_class': 'str',
        'reason': 'str',
        'volume_status': 'list[V1VolumeStatus]'
    }

    attribute_map = {
        'active_pods': 'activePods',
        'conditions': 'conditions',
        'evacuation_node_name': 'evacuationNodeName',
        'fs_freeze_status': 'fsFreezeStatus',
        'guest_os_info': 'guestOSInfo',
        'interfaces': 'interfaces',
        'launcher_container_image_version': 'launcherContainerImageVersion',
        'migration_method': 'migrationMethod',
        'migration_state': 'migrationState',
        'node_name': 'nodeName',
        'phase': 'phase',
        'phase_transition_timestamps': 'phaseTransitionTimestamps',
        'qos_class': 'qosClass',
        'reason': 'reason',
        'volume_status': 'volumeStatus'
    }

    def __init__(self, active_pods=None, conditions=None, evacuation_node_name=None, fs_freeze_status=None, guest_os_info=None, interfaces=None, launcher_container_image_version=None, migration_method=None, migration_state=None, node_name=None, phase=None, phase_transition_timestamps=None, qos_class=None, reason=None, volume_status=None):
        """
        V1VirtualMachineInstanceStatus - a model defined in Swagger
        """

        self._active_pods = None
        self._conditions = None
        self._evacuation_node_name = None
        self._fs_freeze_status = None
        self._guest_os_info = None
        self._interfaces = None
        self._launcher_container_image_version = None
        self._migration_method = None
        self._migration_state = None
        self._node_name = None
        self._phase = None
        self._phase_transition_timestamps = None
        self._qos_class = None
        self._reason = None
        self._volume_status = None

        if active_pods is not None:
          self.active_pods = active_pods
        if conditions is not None:
          self.conditions = conditions
        if evacuation_node_name is not None:
          self.evacuation_node_name = evacuation_node_name
        if fs_freeze_status is not None:
          self.fs_freeze_status = fs_freeze_status
        if guest_os_info is not None:
          self.guest_os_info = guest_os_info
        if interfaces is not None:
          self.interfaces = interfaces
        if launcher_container_image_version is not None:
          self.launcher_container_image_version = launcher_container_image_version
        if migration_method is not None:
          self.migration_method = migration_method
        if migration_state is not None:
          self.migration_state = migration_state
        if node_name is not None:
          self.node_name = node_name
        if phase is not None:
          self.phase = phase
        if phase_transition_timestamps is not None:
          self.phase_transition_timestamps = phase_transition_timestamps
        if qos_class is not None:
          self.qos_class = qos_class
        if reason is not None:
          self.reason = reason
        if volume_status is not None:
          self.volume_status = volume_status

    @property
    def active_pods(self):
        """
        Gets the active_pods of this V1VirtualMachineInstanceStatus.
        ActivePods is a mapping of pod UID to node name. It is possible for multiple pods to be running for a single VMI during migration.

        :return: The active_pods of this V1VirtualMachineInstanceStatus.
        :rtype: dict(str, str)
        """
        return self._active_pods

    @active_pods.setter
    def active_pods(self, active_pods):
        """
        Sets the active_pods of this V1VirtualMachineInstanceStatus.
        ActivePods is a mapping of pod UID to node name. It is possible for multiple pods to be running for a single VMI during migration.

        :param active_pods: The active_pods of this V1VirtualMachineInstanceStatus.
        :type: dict(str, str)
        """

        self._active_pods = active_pods

    @property
    def conditions(self):
        """
        Gets the conditions of this V1VirtualMachineInstanceStatus.
        Conditions are specific points in VirtualMachineInstance's pod runtime.

        :return: The conditions of this V1VirtualMachineInstanceStatus.
        :rtype: list[V1VirtualMachineInstanceCondition]
        """
        return self._conditions

    @conditions.setter
    def conditions(self, conditions):
        """
        Sets the conditions of this V1VirtualMachineInstanceStatus.
        Conditions are specific points in VirtualMachineInstance's pod runtime.

        :param conditions: The conditions of this V1VirtualMachineInstanceStatus.
        :type: list[V1VirtualMachineInstanceCondition]
        """

        self._conditions = conditions

    @property
    def evacuation_node_name(self):
        """
        Gets the evacuation_node_name of this V1VirtualMachineInstanceStatus.
        EvacuationNodeName is used to track the eviction process of a VMI. It stores the name of the node that we want to evacuate. It is meant to be used by KubeVirt core components only and can't be set or modified by users.

        :return: The evacuation_node_name of this V1VirtualMachineInstanceStatus.
        :rtype: str
        """
        return self._evacuation_node_name

    @evacuation_node_name.setter
    def evacuation_node_name(self, evacuation_node_name):
        """
        Sets the evacuation_node_name of this V1VirtualMachineInstanceStatus.
        EvacuationNodeName is used to track the eviction process of a VMI. It stores the name of the node that we want to evacuate. It is meant to be used by KubeVirt core components only and can't be set or modified by users.

        :param evacuation_node_name: The evacuation_node_name of this V1VirtualMachineInstanceStatus.
        :type: str
        """

        self._evacuation_node_name = evacuation_node_name

    @property
    def fs_freeze_status(self):
        """
        Gets the fs_freeze_status of this V1VirtualMachineInstanceStatus.
        FSFreezeStatus is the state of the fs of the guest it can be either frozen or thawed

        :return: The fs_freeze_status of this V1VirtualMachineInstanceStatus.
        :rtype: str
        """
        return self._fs_freeze_status

    @fs_freeze_status.setter
    def fs_freeze_status(self, fs_freeze_status):
        """
        Sets the fs_freeze_status of this V1VirtualMachineInstanceStatus.
        FSFreezeStatus is the state of the fs of the guest it can be either frozen or thawed

        :param fs_freeze_status: The fs_freeze_status of this V1VirtualMachineInstanceStatus.
        :type: str
        """

        self._fs_freeze_status = fs_freeze_status

    @property
    def guest_os_info(self):
        """
        Gets the guest_os_info of this V1VirtualMachineInstanceStatus.
        Guest OS Information

        :return: The guest_os_info of this V1VirtualMachineInstanceStatus.
        :rtype: V1VirtualMachineInstanceGuestOSInfo
        """
        return self._guest_os_info

    @guest_os_info.setter
    def guest_os_info(self, guest_os_info):
        """
        Sets the guest_os_info of this V1VirtualMachineInstanceStatus.
        Guest OS Information

        :param guest_os_info: The guest_os_info of this V1VirtualMachineInstanceStatus.
        :type: V1VirtualMachineInstanceGuestOSInfo
        """

        self._guest_os_info = guest_os_info

    @property
    def interfaces(self):
        """
        Gets the interfaces of this V1VirtualMachineInstanceStatus.
        Interfaces represent the details of available network interfaces.

        :return: The interfaces of this V1VirtualMachineInstanceStatus.
        :rtype: list[V1VirtualMachineInstanceNetworkInterface]
        """
        return self._interfaces

    @interfaces.setter
    def interfaces(self, interfaces):
        """
        Sets the interfaces of this V1VirtualMachineInstanceStatus.
        Interfaces represent the details of available network interfaces.

        :param interfaces: The interfaces of this V1VirtualMachineInstanceStatus.
        :type: list[V1VirtualMachineInstanceNetworkInterface]
        """

        self._interfaces = interfaces

    @property
    def launcher_container_image_version(self):
        """
        Gets the launcher_container_image_version of this V1VirtualMachineInstanceStatus.
        LauncherContainerImageVersion indicates what container image is currently active for the vmi.

        :return: The launcher_container_image_version of this V1VirtualMachineInstanceStatus.
        :rtype: str
        """
        return self._launcher_container_image_version

    @launcher_container_image_version.setter
    def launcher_container_image_version(self, launcher_container_image_version):
        """
        Sets the launcher_container_image_version of this V1VirtualMachineInstanceStatus.
        LauncherContainerImageVersion indicates what container image is currently active for the vmi.

        :param launcher_container_image_version: The launcher_container_image_version of this V1VirtualMachineInstanceStatus.
        :type: str
        """

        self._launcher_container_image_version = launcher_container_image_version

    @property
    def migration_method(self):
        """
        Gets the migration_method of this V1VirtualMachineInstanceStatus.
        Represents the method using which the vmi can be migrated: live migration or block migration

        :return: The migration_method of this V1VirtualMachineInstanceStatus.
        :rtype: str
        """
        return self._migration_method

    @migration_method.setter
    def migration_method(self, migration_method):
        """
        Sets the migration_method of this V1VirtualMachineInstanceStatus.
        Represents the method using which the vmi can be migrated: live migration or block migration

        :param migration_method: The migration_method of this V1VirtualMachineInstanceStatus.
        :type: str
        """

        self._migration_method = migration_method

    @property
    def migration_state(self):
        """
        Gets the migration_state of this V1VirtualMachineInstanceStatus.
        Represents the status of a live migration

        :return: The migration_state of this V1VirtualMachineInstanceStatus.
        :rtype: V1VirtualMachineInstanceMigrationState
        """
        return self._migration_state

    @migration_state.setter
    def migration_state(self, migration_state):
        """
        Sets the migration_state of this V1VirtualMachineInstanceStatus.
        Represents the status of a live migration

        :param migration_state: The migration_state of this V1VirtualMachineInstanceStatus.
        :type: V1VirtualMachineInstanceMigrationState
        """

        self._migration_state = migration_state

    @property
    def node_name(self):
        """
        Gets the node_name of this V1VirtualMachineInstanceStatus.
        NodeName is the name where the VirtualMachineInstance is currently running.

        :return: The node_name of this V1VirtualMachineInstanceStatus.
        :rtype: str
        """
        return self._node_name

    @node_name.setter
    def node_name(self, node_name):
        """
        Sets the node_name of this V1VirtualMachineInstanceStatus.
        NodeName is the name where the VirtualMachineInstance is currently running.

        :param node_name: The node_name of this V1VirtualMachineInstanceStatus.
        :type: str
        """

        self._node_name = node_name

    @property
    def phase(self):
        """
        Gets the phase of this V1VirtualMachineInstanceStatus.
        Phase is the status of the VirtualMachineInstance in kubernetes world. It is not the VirtualMachineInstance status, but partially correlates to it.

        :return: The phase of this V1VirtualMachineInstanceStatus.
        :rtype: str
        """
        return self._phase

    @phase.setter
    def phase(self, phase):
        """
        Sets the phase of this V1VirtualMachineInstanceStatus.
        Phase is the status of the VirtualMachineInstance in kubernetes world. It is not the VirtualMachineInstance status, but partially correlates to it.

        :param phase: The phase of this V1VirtualMachineInstanceStatus.
        :type: str
        """

        self._phase = phase

    @property
    def phase_transition_timestamps(self):
        """
        Gets the phase_transition_timestamps of this V1VirtualMachineInstanceStatus.
        PhaseTransitionTimestamp is the timestamp of when the last phase change occurred

        :return: The phase_transition_timestamps of this V1VirtualMachineInstanceStatus.
        :rtype: list[V1VirtualMachineInstancePhaseTransitionTimestamp]
        """
        return self._phase_transition_timestamps

    @phase_transition_timestamps.setter
    def phase_transition_timestamps(self, phase_transition_timestamps):
        """
        Sets the phase_transition_timestamps of this V1VirtualMachineInstanceStatus.
        PhaseTransitionTimestamp is the timestamp of when the last phase change occurred

        :param phase_transition_timestamps: The phase_transition_timestamps of this V1VirtualMachineInstanceStatus.
        :type: list[V1VirtualMachineInstancePhaseTransitionTimestamp]
        """

        self._phase_transition_timestamps = phase_transition_timestamps

    @property
    def qos_class(self):
        """
        Gets the qos_class of this V1VirtualMachineInstanceStatus.
        The Quality of Service (QOS) classification assigned to the virtual machine instance based on resource requirements See PodQOSClass type for available QOS classes More info: https://git.k8s.io/community/contributors/design-proposals/node/resource-qos.md

        :return: The qos_class of this V1VirtualMachineInstanceStatus.
        :rtype: str
        """
        return self._qos_class

    @qos_class.setter
    def qos_class(self, qos_class):
        """
        Sets the qos_class of this V1VirtualMachineInstanceStatus.
        The Quality of Service (QOS) classification assigned to the virtual machine instance based on resource requirements See PodQOSClass type for available QOS classes More info: https://git.k8s.io/community/contributors/design-proposals/node/resource-qos.md

        :param qos_class: The qos_class of this V1VirtualMachineInstanceStatus.
        :type: str
        """

        self._qos_class = qos_class

    @property
    def reason(self):
        """
        Gets the reason of this V1VirtualMachineInstanceStatus.
        A brief CamelCase message indicating details about why the VMI is in this state. e.g. 'NodeUnresponsive'

        :return: The reason of this V1VirtualMachineInstanceStatus.
        :rtype: str
        """
        return self._reason

    @reason.setter
    def reason(self, reason):
        """
        Sets the reason of this V1VirtualMachineInstanceStatus.
        A brief CamelCase message indicating details about why the VMI is in this state. e.g. 'NodeUnresponsive'

        :param reason: The reason of this V1VirtualMachineInstanceStatus.
        :type: str
        """

        self._reason = reason

    @property
    def volume_status(self):
        """
        Gets the volume_status of this V1VirtualMachineInstanceStatus.
        VolumeStatus contains the statuses of all the volumes

        :return: The volume_status of this V1VirtualMachineInstanceStatus.
        :rtype: list[V1VolumeStatus]
        """
        return self._volume_status

    @volume_status.setter
    def volume_status(self, volume_status):
        """
        Sets the volume_status of this V1VirtualMachineInstanceStatus.
        VolumeStatus contains the statuses of all the volumes

        :param volume_status: The volume_status of this V1VirtualMachineInstanceStatus.
        :type: list[V1VolumeStatus]
        """

        self._volume_status = volume_status

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
        if not isinstance(other, V1VirtualMachineInstanceStatus):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
