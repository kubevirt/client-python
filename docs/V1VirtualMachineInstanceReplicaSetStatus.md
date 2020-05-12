# V1VirtualMachineInstanceReplicaSetStatus

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**conditions** | [**list[V1VirtualMachineInstanceReplicaSetCondition]**](V1VirtualMachineInstanceReplicaSetCondition.md) |  | [optional] 
**label_selector** | **str** | Canonical form of the label selector for HPA which consumes it through the scale subresource. | [optional] 
**ready_replicas** | **int** | The number of ready replicas for this replica set. | [optional] 
**replicas** | **int** | Total number of non-terminated pods targeted by this deployment (their labels match the selector). | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


