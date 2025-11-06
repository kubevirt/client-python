# V1beta1VirtualMachinePoolUpdateStrategy

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**opportunistic** | [**V1beta1VirtualMachineOpportunisticUpdateStrategy**](V1beta1VirtualMachineOpportunisticUpdateStrategy.md) | Opportunistic update only gets applied to the VM, VMI is updated naturally upon the restart. Whereas proactive it applies both the VM and VMI right away. | [optional] 
**proactive** | [**V1beta1VirtualMachinePoolProactiveUpdateStrategy**](V1beta1VirtualMachinePoolProactiveUpdateStrategy.md) | Proactive update by forcing the VMs to restart during update | [optional] 
**unmanaged** | [**V1beta1VirtualMachinePoolUnmanagedStrategy**](V1beta1VirtualMachinePoolUnmanagedStrategy.md) | Unmanaged indicates that no automatic update of VMs within a VMPool is performed. When this is set, the VMPool controller will not update the VMs within the pool. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


