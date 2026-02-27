# V1ReservedOverhead

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**added_overhead** | [**K8sIoApimachineryPkgApiResourceQuantity**](K8sIoApimachineryPkgApiResourceQuantity.md) | AddedOverhead determines the memory overhead that will be reserved for the VM. It increases the virt-launcher pod memory limit. | [optional] 
**mem_lock** | **str** | RequiresLock determines whether the VM&#39;s and its overhead memory need to be locked or not. It is a common practice to enable this if vDPA, VFIO or any other specialized hardware that depends on DMA is being used by the VM. False - (Default) memory lock RLimits are not modified. True - Memory lock RLimits will be updated to consider VM memory        size and memory overhead | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


