# V1VirtualMachineStatus

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**conditions** | [**list[V1VirtualMachineCondition]**](V1VirtualMachineCondition.md) | Conditions are specific points in VM&#39;s pod runtime. | [optional] 
**interfaces** | [**list[V1VirtualMachineNetworkInterface]**](V1VirtualMachineNetworkInterface.md) | Interfaces represent the details of available network interfaces. | [optional] 
**node_name** | **str** | NodeName is the name where the VM is currently running. | [optional] 
**phase** | **str** | Phase is the status of the VM in kubernetes world. It is not the VM status, but partially correlates to it. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


