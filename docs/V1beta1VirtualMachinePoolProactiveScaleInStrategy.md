# V1beta1VirtualMachinePoolProactiveScaleInStrategy

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**selection_policy** | [**V1beta1VirtualMachinePoolSelectionPolicy**](V1beta1VirtualMachinePoolSelectionPolicy.md) | SelectionPolicy defines the priority in which VM instances are selected for proactive scale-in Defaults to \&quot;Random\&quot; base policy when no SelectionPolicy is configured | [optional] 
**state_preservation** | **str** | Specifies if and how to preserve the state of the VMs selected during scale-in. Disabled - (Default) all state for VMs selected for scale-in will be deleted. Offline - PVCs for VMs selected for scale-in will be preserved and reused on scale-out (decreases provisioning time during scale out). Online - PVCs and memory for VMs selected for scale-in will be preserved and reused on scale-out (decreases provisioning and boot time during scale out). | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


