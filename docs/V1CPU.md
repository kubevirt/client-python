# V1CPU

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cores** | **int** | Cores specifies the number of cores inside the vmi. Must be a value greater or equal 1. | [optional] 
**model** | **str** | Model specifies the CPU model inside the VMI. List of available models https://github.com/libvirt/libvirt/blob/master/src/cpu/cpu_map.xml. It is possible to specify special cases like \&quot;host-passthrough\&quot; to get the same CPU as the node and \&quot;host-model\&quot; to get CPU closest to the node one. For more information see https://libvirt.org/formatdomain.html#elementsCPU. Defaults to host-model. +optional | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


