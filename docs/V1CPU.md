# V1CPU

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cores** | **int** | Cores specifies the number of cores inside the vmi. Must be a value greater or equal 1. | [optional] 
**dedicated_cpu_placement** | **bool** | DedicatedCPUPlacement requests the scheduler to place the VirtualMachineInstance on a node with enough dedicated pCPUs and pin the vCPUs to it. +optional | [optional] 
**features** | [**list[V1CPUFeature]**](V1CPUFeature.md) | Features specifies the CPU features list inside the VMI. +optional | [optional] 
**model** | **str** | Model specifies the CPU model inside the VMI. List of available models https://github.com/libvirt/libvirt/tree/master/src/cpu_map. It is possible to specify special cases like \&quot;host-passthrough\&quot; to get the same CPU as the node and \&quot;host-model\&quot; to get CPU closest to the node one. Defaults to host-model. +optional | [optional] 
**sockets** | **int** | Sockets specifies the number of sockets inside the vmi. Must be a value greater or equal 1. | [optional] 
**threads** | **int** | Threads specifies the number of threads inside the vmi. Must be a value greater or equal 1. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


