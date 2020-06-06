# V1VirtualMachineStatus

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**conditions** | [**list[V1VirtualMachineCondition]**](V1VirtualMachineCondition.md) | Hold the state information of the VirtualMachine and its VirtualMachineInstance | [optional] 
**created** | **bool** | Created indicates if the virtual machine is created in the cluster | [optional] 
**ready** | **bool** | Ready indicates if the virtual machine is running and ready | [optional] 
**snapshot_in_progress** | **str** | SnapshotInProgress is the name of the VirtualMachineSnapshot currently executing | [optional] 
**state_change_requests** | [**list[V1VirtualMachineStateChangeRequest]**](V1VirtualMachineStateChangeRequest.md) | StateChangeRequests indicates a list of actions that should be taken on a VMI e.g. stop a specific VMI then start a new one. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


