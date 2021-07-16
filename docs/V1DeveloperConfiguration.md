# V1DeveloperConfiguration

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cpu_allocation_ratio** | **int** |  | [optional] 
**disk_verification** | [**V1DiskVerification**](V1DiskVerification.md) |  | [optional] 
**feature_gates** | **list[str]** |  | [optional] 
**log_verbosity** | [**V1LogVerbosity**](V1LogVerbosity.md) |  | [optional] 
**memory_overcommit** | **int** |  | [optional] 
**minimum_cluster_tsc_frequency** | **int** | Allow overriding the automatically determined minimum TSC frequency of the cluster and fixate the minimum to this frequency. | [optional] 
**minimum_reserve_pvc_bytes** | **int** |  | [optional] 
**node_selectors** | **dict(str, str)** |  | [optional] 
**pvc_tolerate_less_space_up_to_percent** | **int** |  | [optional] 
**use_emulation** | **bool** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


