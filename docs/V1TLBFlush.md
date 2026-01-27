# V1TLBFlush

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**direct** | [**V1FeatureState**](V1FeatureState.md) | Direct allows sending the TLB flush command directly to the hypervisor. It can be useful to optimize performance in nested virtualization cases, such as Windows VBS. | [optional] 
**enabled** | **bool** | Enabled determines if the feature should be enabled or disabled on the guest. Defaults to true. | [optional] 
**extended** | [**V1FeatureState**](V1FeatureState.md) | Extended allows the guest to execute partial TLB flushes. It can be helpful for general purpose workloads. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


