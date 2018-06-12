# V1VirtualMachineInstanceStatus

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**conditions** | [**list[V1VirtualMachineInstanceCondition]**](V1VirtualMachineInstanceCondition.md) | Conditions are specific points in VirtualMachineInstance&#39;s pod runtime. | [optional] 
**interfaces** | [**list[V1VirtualMachineInstanceNetworkInterface]**](V1VirtualMachineInstanceNetworkInterface.md) | Interfaces represent the details of available network interfaces. | [optional] 
**node_name** | **str** | NodeName is the name where the VirtualMachineInstance is currently running. | [optional] 
**phase** | **str** | Phase is the status of the VirtualMachineInstance in kubernetes world. It is not the VirtualMachineInstance status, but partially correlates to it. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


