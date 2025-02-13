# V1VirtualMachineStatus

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**conditions** | [**list[V1VirtualMachineCondition]**](V1VirtualMachineCondition.md) | Hold the state information of the VirtualMachine and its VirtualMachineInstance | [optional] 
**created** | **bool** | Created indicates if the virtual machine is created in the cluster | [optional] 
**desired_generation** | **int** | DesiredGeneration is the generation which is desired for the VMI. This will be used in comparisons with ObservedGeneration to understand when the VMI is out of sync. This will be changed at the same time as ObservedGeneration to remove errors which could occur if Generation is updated through an Update() before ObservedGeneration in Status. | [optional] 
**instancetype_ref** | [**V1InstancetypeStatusRef**](V1InstancetypeStatusRef.md) | InstancetypeRef captures the state of any referenced instance type from the VirtualMachine | [optional] 
**memory_dump_request** | [**V1VirtualMachineMemoryDumpRequest**](V1VirtualMachineMemoryDumpRequest.md) | MemoryDumpRequest tracks memory dump request phase and info of getting a memory dump to the given pvc | [optional] 
**observed_generation** | **int** | ObservedGeneration is the generation observed by the vmi when started. | [optional] 
**preference_ref** | [**V1InstancetypeStatusRef**](V1InstancetypeStatusRef.md) | PreferenceRef captures the state of any referenced preference from the VirtualMachine | [optional] 
**printable_status** | **str** | PrintableStatus is a human readable, high-level representation of the status of the virtual machine | [optional] 
**ready** | **bool** | Ready indicates if the virtual machine is running and ready | [optional] 
**restore_in_progress** | **str** | RestoreInProgress is the name of the VirtualMachineRestore currently executing | [optional] 
**run_strategy** | **str** | RunStrategy tracks the last recorded RunStrategy used by the VM. This is needed to correctly process the next strategy (for now only the RerunOnFailure) | [optional] 
**snapshot_in_progress** | **str** | SnapshotInProgress is the name of the VirtualMachineSnapshot currently executing | [optional] 
**start_failure** | [**V1VirtualMachineStartFailure**](V1VirtualMachineStartFailure.md) | StartFailure tracks consecutive VMI startup failures for the purposes of crash loop backoffs | [optional] 
**state_change_requests** | [**list[V1VirtualMachineStateChangeRequest]**](V1VirtualMachineStateChangeRequest.md) | StateChangeRequests indicates a list of actions that should be taken on a VMI e.g. stop a specific VMI then start a new one. | [optional] 
**volume_requests** | [**list[V1VirtualMachineVolumeRequest]**](V1VirtualMachineVolumeRequest.md) | VolumeRequests indicates a list of volumes add or remove from the VMI template and hotplug on an active running VMI. | [optional] 
**volume_snapshot_statuses** | [**list[V1VolumeSnapshotStatus]**](V1VolumeSnapshotStatus.md) | VolumeSnapshotStatuses indicates a list of statuses whether snapshotting is supported by each volume. | [optional] 
**volume_update_state** | [**V1VolumeUpdateState**](V1VolumeUpdateState.md) | VolumeUpdateState contains the information about the volumes set updates related to the volumeUpdateStrategy | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


