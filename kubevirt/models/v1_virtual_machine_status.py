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


class V1VirtualMachineStatus(object):
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
        'conditions': 'list[V1VirtualMachineCondition]',
        'created': 'bool',
        'desired_generation': 'int',
        'memory_dump_request': 'V1VirtualMachineMemoryDumpRequest',
        'observed_generation': 'int',
        'printable_status': 'str',
        'ready': 'bool',
        'restore_in_progress': 'str',
        'run_strategy': 'str',
        'snapshot_in_progress': 'str',
        'start_failure': 'V1VirtualMachineStartFailure',
        'state_change_requests': 'list[V1VirtualMachineStateChangeRequest]',
        'volume_requests': 'list[V1VirtualMachineVolumeRequest]',
        'volume_snapshot_statuses': 'list[V1VolumeSnapshotStatus]',
        'volume_update_state': 'V1VolumeUpdateState'
    }

    attribute_map = {
        'conditions': 'conditions',
        'created': 'created',
        'desired_generation': 'desiredGeneration',
        'memory_dump_request': 'memoryDumpRequest',
        'observed_generation': 'observedGeneration',
        'printable_status': 'printableStatus',
        'ready': 'ready',
        'restore_in_progress': 'restoreInProgress',
        'run_strategy': 'runStrategy',
        'snapshot_in_progress': 'snapshotInProgress',
        'start_failure': 'startFailure',
        'state_change_requests': 'stateChangeRequests',
        'volume_requests': 'volumeRequests',
        'volume_snapshot_statuses': 'volumeSnapshotStatuses',
        'volume_update_state': 'volumeUpdateState'
    }

    def __init__(self, conditions=None, created=None, desired_generation=None, memory_dump_request=None, observed_generation=None, printable_status=None, ready=None, restore_in_progress=None, run_strategy=None, snapshot_in_progress=None, start_failure=None, state_change_requests=None, volume_requests=None, volume_snapshot_statuses=None, volume_update_state=None):
        """
        V1VirtualMachineStatus - a model defined in Swagger
        """

        self._conditions = None
        self._created = None
        self._desired_generation = None
        self._memory_dump_request = None
        self._observed_generation = None
        self._printable_status = None
        self._ready = None
        self._restore_in_progress = None
        self._run_strategy = None
        self._snapshot_in_progress = None
        self._start_failure = None
        self._state_change_requests = None
        self._volume_requests = None
        self._volume_snapshot_statuses = None
        self._volume_update_state = None

        if conditions is not None:
          self.conditions = conditions
        if created is not None:
          self.created = created
        if desired_generation is not None:
          self.desired_generation = desired_generation
        if memory_dump_request is not None:
          self.memory_dump_request = memory_dump_request
        if observed_generation is not None:
          self.observed_generation = observed_generation
        if printable_status is not None:
          self.printable_status = printable_status
        if ready is not None:
          self.ready = ready
        if restore_in_progress is not None:
          self.restore_in_progress = restore_in_progress
        if run_strategy is not None:
          self.run_strategy = run_strategy
        if snapshot_in_progress is not None:
          self.snapshot_in_progress = snapshot_in_progress
        if start_failure is not None:
          self.start_failure = start_failure
        if state_change_requests is not None:
          self.state_change_requests = state_change_requests
        if volume_requests is not None:
          self.volume_requests = volume_requests
        if volume_snapshot_statuses is not None:
          self.volume_snapshot_statuses = volume_snapshot_statuses
        if volume_update_state is not None:
          self.volume_update_state = volume_update_state

    @property
    def conditions(self):
        """
        Gets the conditions of this V1VirtualMachineStatus.
        Hold the state information of the VirtualMachine and its VirtualMachineInstance

        :return: The conditions of this V1VirtualMachineStatus.
        :rtype: list[V1VirtualMachineCondition]
        """
        return self._conditions

    @conditions.setter
    def conditions(self, conditions):
        """
        Sets the conditions of this V1VirtualMachineStatus.
        Hold the state information of the VirtualMachine and its VirtualMachineInstance

        :param conditions: The conditions of this V1VirtualMachineStatus.
        :type: list[V1VirtualMachineCondition]
        """

        self._conditions = conditions

    @property
    def created(self):
        """
        Gets the created of this V1VirtualMachineStatus.
        Created indicates if the virtual machine is created in the cluster

        :return: The created of this V1VirtualMachineStatus.
        :rtype: bool
        """
        return self._created

    @created.setter
    def created(self, created):
        """
        Sets the created of this V1VirtualMachineStatus.
        Created indicates if the virtual machine is created in the cluster

        :param created: The created of this V1VirtualMachineStatus.
        :type: bool
        """

        self._created = created

    @property
    def desired_generation(self):
        """
        Gets the desired_generation of this V1VirtualMachineStatus.
        DesiredGeneration is the generation which is desired for the VMI. This will be used in comparisons with ObservedGeneration to understand when the VMI is out of sync. This will be changed at the same time as ObservedGeneration to remove errors which could occur if Generation is updated through an Update() before ObservedGeneration in Status.

        :return: The desired_generation of this V1VirtualMachineStatus.
        :rtype: int
        """
        return self._desired_generation

    @desired_generation.setter
    def desired_generation(self, desired_generation):
        """
        Sets the desired_generation of this V1VirtualMachineStatus.
        DesiredGeneration is the generation which is desired for the VMI. This will be used in comparisons with ObservedGeneration to understand when the VMI is out of sync. This will be changed at the same time as ObservedGeneration to remove errors which could occur if Generation is updated through an Update() before ObservedGeneration in Status.

        :param desired_generation: The desired_generation of this V1VirtualMachineStatus.
        :type: int
        """

        self._desired_generation = desired_generation

    @property
    def memory_dump_request(self):
        """
        Gets the memory_dump_request of this V1VirtualMachineStatus.
        MemoryDumpRequest tracks memory dump request phase and info of getting a memory dump to the given pvc

        :return: The memory_dump_request of this V1VirtualMachineStatus.
        :rtype: V1VirtualMachineMemoryDumpRequest
        """
        return self._memory_dump_request

    @memory_dump_request.setter
    def memory_dump_request(self, memory_dump_request):
        """
        Sets the memory_dump_request of this V1VirtualMachineStatus.
        MemoryDumpRequest tracks memory dump request phase and info of getting a memory dump to the given pvc

        :param memory_dump_request: The memory_dump_request of this V1VirtualMachineStatus.
        :type: V1VirtualMachineMemoryDumpRequest
        """

        self._memory_dump_request = memory_dump_request

    @property
    def observed_generation(self):
        """
        Gets the observed_generation of this V1VirtualMachineStatus.
        ObservedGeneration is the generation observed by the vmi when started.

        :return: The observed_generation of this V1VirtualMachineStatus.
        :rtype: int
        """
        return self._observed_generation

    @observed_generation.setter
    def observed_generation(self, observed_generation):
        """
        Sets the observed_generation of this V1VirtualMachineStatus.
        ObservedGeneration is the generation observed by the vmi when started.

        :param observed_generation: The observed_generation of this V1VirtualMachineStatus.
        :type: int
        """

        self._observed_generation = observed_generation

    @property
    def printable_status(self):
        """
        Gets the printable_status of this V1VirtualMachineStatus.
        PrintableStatus is a human readable, high-level representation of the status of the virtual machine

        :return: The printable_status of this V1VirtualMachineStatus.
        :rtype: str
        """
        return self._printable_status

    @printable_status.setter
    def printable_status(self, printable_status):
        """
        Sets the printable_status of this V1VirtualMachineStatus.
        PrintableStatus is a human readable, high-level representation of the status of the virtual machine

        :param printable_status: The printable_status of this V1VirtualMachineStatus.
        :type: str
        """

        self._printable_status = printable_status

    @property
    def ready(self):
        """
        Gets the ready of this V1VirtualMachineStatus.
        Ready indicates if the virtual machine is running and ready

        :return: The ready of this V1VirtualMachineStatus.
        :rtype: bool
        """
        return self._ready

    @ready.setter
    def ready(self, ready):
        """
        Sets the ready of this V1VirtualMachineStatus.
        Ready indicates if the virtual machine is running and ready

        :param ready: The ready of this V1VirtualMachineStatus.
        :type: bool
        """

        self._ready = ready

    @property
    def restore_in_progress(self):
        """
        Gets the restore_in_progress of this V1VirtualMachineStatus.
        RestoreInProgress is the name of the VirtualMachineRestore currently executing

        :return: The restore_in_progress of this V1VirtualMachineStatus.
        :rtype: str
        """
        return self._restore_in_progress

    @restore_in_progress.setter
    def restore_in_progress(self, restore_in_progress):
        """
        Sets the restore_in_progress of this V1VirtualMachineStatus.
        RestoreInProgress is the name of the VirtualMachineRestore currently executing

        :param restore_in_progress: The restore_in_progress of this V1VirtualMachineStatus.
        :type: str
        """

        self._restore_in_progress = restore_in_progress

    @property
    def run_strategy(self):
        """
        Gets the run_strategy of this V1VirtualMachineStatus.
        RunStrategy tracks the last recorded RunStrategy used by the VM. This is needed to correctly process the next strategy (for now only the RerunOnFailure)

        :return: The run_strategy of this V1VirtualMachineStatus.
        :rtype: str
        """
        return self._run_strategy

    @run_strategy.setter
    def run_strategy(self, run_strategy):
        """
        Sets the run_strategy of this V1VirtualMachineStatus.
        RunStrategy tracks the last recorded RunStrategy used by the VM. This is needed to correctly process the next strategy (for now only the RerunOnFailure)

        :param run_strategy: The run_strategy of this V1VirtualMachineStatus.
        :type: str
        """

        self._run_strategy = run_strategy

    @property
    def snapshot_in_progress(self):
        """
        Gets the snapshot_in_progress of this V1VirtualMachineStatus.
        SnapshotInProgress is the name of the VirtualMachineSnapshot currently executing

        :return: The snapshot_in_progress of this V1VirtualMachineStatus.
        :rtype: str
        """
        return self._snapshot_in_progress

    @snapshot_in_progress.setter
    def snapshot_in_progress(self, snapshot_in_progress):
        """
        Sets the snapshot_in_progress of this V1VirtualMachineStatus.
        SnapshotInProgress is the name of the VirtualMachineSnapshot currently executing

        :param snapshot_in_progress: The snapshot_in_progress of this V1VirtualMachineStatus.
        :type: str
        """

        self._snapshot_in_progress = snapshot_in_progress

    @property
    def start_failure(self):
        """
        Gets the start_failure of this V1VirtualMachineStatus.
        StartFailure tracks consecutive VMI startup failures for the purposes of crash loop backoffs

        :return: The start_failure of this V1VirtualMachineStatus.
        :rtype: V1VirtualMachineStartFailure
        """
        return self._start_failure

    @start_failure.setter
    def start_failure(self, start_failure):
        """
        Sets the start_failure of this V1VirtualMachineStatus.
        StartFailure tracks consecutive VMI startup failures for the purposes of crash loop backoffs

        :param start_failure: The start_failure of this V1VirtualMachineStatus.
        :type: V1VirtualMachineStartFailure
        """

        self._start_failure = start_failure

    @property
    def state_change_requests(self):
        """
        Gets the state_change_requests of this V1VirtualMachineStatus.
        StateChangeRequests indicates a list of actions that should be taken on a VMI e.g. stop a specific VMI then start a new one.

        :return: The state_change_requests of this V1VirtualMachineStatus.
        :rtype: list[V1VirtualMachineStateChangeRequest]
        """
        return self._state_change_requests

    @state_change_requests.setter
    def state_change_requests(self, state_change_requests):
        """
        Sets the state_change_requests of this V1VirtualMachineStatus.
        StateChangeRequests indicates a list of actions that should be taken on a VMI e.g. stop a specific VMI then start a new one.

        :param state_change_requests: The state_change_requests of this V1VirtualMachineStatus.
        :type: list[V1VirtualMachineStateChangeRequest]
        """

        self._state_change_requests = state_change_requests

    @property
    def volume_requests(self):
        """
        Gets the volume_requests of this V1VirtualMachineStatus.
        VolumeRequests indicates a list of volumes add or remove from the VMI template and hotplug on an active running VMI.

        :return: The volume_requests of this V1VirtualMachineStatus.
        :rtype: list[V1VirtualMachineVolumeRequest]
        """
        return self._volume_requests

    @volume_requests.setter
    def volume_requests(self, volume_requests):
        """
        Sets the volume_requests of this V1VirtualMachineStatus.
        VolumeRequests indicates a list of volumes add or remove from the VMI template and hotplug on an active running VMI.

        :param volume_requests: The volume_requests of this V1VirtualMachineStatus.
        :type: list[V1VirtualMachineVolumeRequest]
        """

        self._volume_requests = volume_requests

    @property
    def volume_snapshot_statuses(self):
        """
        Gets the volume_snapshot_statuses of this V1VirtualMachineStatus.
        VolumeSnapshotStatuses indicates a list of statuses whether snapshotting is supported by each volume.

        :return: The volume_snapshot_statuses of this V1VirtualMachineStatus.
        :rtype: list[V1VolumeSnapshotStatus]
        """
        return self._volume_snapshot_statuses

    @volume_snapshot_statuses.setter
    def volume_snapshot_statuses(self, volume_snapshot_statuses):
        """
        Sets the volume_snapshot_statuses of this V1VirtualMachineStatus.
        VolumeSnapshotStatuses indicates a list of statuses whether snapshotting is supported by each volume.

        :param volume_snapshot_statuses: The volume_snapshot_statuses of this V1VirtualMachineStatus.
        :type: list[V1VolumeSnapshotStatus]
        """

        self._volume_snapshot_statuses = volume_snapshot_statuses

    @property
    def volume_update_state(self):
        """
        Gets the volume_update_state of this V1VirtualMachineStatus.
        VolumeUpdateState contains the information about the volumes set updates related to the volumeUpdateStrategy

        :return: The volume_update_state of this V1VirtualMachineStatus.
        :rtype: V1VolumeUpdateState
        """
        return self._volume_update_state

    @volume_update_state.setter
    def volume_update_state(self, volume_update_state):
        """
        Sets the volume_update_state of this V1VirtualMachineStatus.
        VolumeUpdateState contains the information about the volumes set updates related to the volumeUpdateStrategy

        :param volume_update_state: The volume_update_state of this V1VirtualMachineStatus.
        :type: V1VolumeUpdateState
        """

        self._volume_update_state = volume_update_state

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
        if not isinstance(other, V1VirtualMachineStatus):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
