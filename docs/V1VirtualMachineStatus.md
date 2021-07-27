# V1VirtualMachineStatus

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**conditions** | [**list[V1VirtualMachineCondition]**](V1VirtualMachineCondition.md) | Hold the state information of the VirtualMachine and its VirtualMachineInstance | [optional] 
**created** | **bool** | Created indicates if the virtual machine is created in the cluster | [optional] 
**printable_status** | **str** | PrintableStatus is a human readable, high-level representation of the status of the virtual machine | [optional] 
**ready** | **bool** | Ready indicates if the virtual machine is running and ready | [optional] 
**snapshot_in_progress** | **str** | SnapshotInProgress is the name of the VirtualMachineSnapshot currently executing | [optional] 
**start_failure** | [**V1VirtualMachineStartFailure**](V1VirtualMachineStartFailure.md) | StartFailure tracks consecutive VMI startup failures for the purposes of crash loop backoffs | [optional] 
**state_change_requests** | [**list[V1VirtualMachineStateChangeRequest]**](V1VirtualMachineStateChangeRequest.md) | StateChangeRequests indicates a list of actions that should be taken on a VMI e.g. stop a specific VMI then start a new one. | [optional] 
**volume_requests** | [**list[V1VirtualMachineVolumeRequest]**](V1VirtualMachineVolumeRequest.md) | VolumeRequests indicates a list of volumes add or remove from the VMI template and hotplug on an active running VMI. | [optional] 
**volume_snapshot_statuses** | [**list[V1VolumeSnapshotStatus]**](V1VolumeSnapshotStatus.md) | VolumeSnapshotStatuses indicates a list of statuses whether snapshotting is supported by each volume. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


