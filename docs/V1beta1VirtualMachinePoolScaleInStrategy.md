# V1beta1VirtualMachinePoolScaleInStrategy

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**opportunistic** | [**V1beta1VirtualMachinePoolOpportunisticScaleInStrategy**](V1beta1VirtualMachinePoolOpportunisticScaleInStrategy.md) | Opportunistic scale-in is a strategy when vms are deleted by some other means than the scale-in action. For example, when the VM is deleted by the user or when the VM is deleted by the node that is hosting the VM. | [optional] 
**proactive** | [**V1beta1VirtualMachinePoolProactiveScaleInStrategy**](V1beta1VirtualMachinePoolProactiveScaleInStrategy.md) | Proactive scale-in by forcing VMs to shutdown during scale-in (Default) | [optional] 
**unmanaged** | [**V1beta1VirtualMachinePoolUnmanagedStrategy**](V1beta1VirtualMachinePoolUnmanagedStrategy.md) | The VM is never touched after creation. Users are responsible for scaling in the pool manually. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


