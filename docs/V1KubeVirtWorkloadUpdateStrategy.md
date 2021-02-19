# V1KubeVirtWorkloadUpdateStrategy

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**batch_eviction_interval** | [**K8sIoApimachineryPkgApisMetaV1Duration**](K8sIoApimachineryPkgApisMetaV1Duration.md) | BatchEvictionInterval Represents the interval to wait before issuing the next batch of shutdowns  Defaults to 1 minute | [optional] 
**batch_eviction_size** | **int** | BatchEvictionSize Represents the number of VMIs that can be forced updated per the BatchShutdownInteral interval  Defaults to 10 | [optional] 
**workload_update_methods** | **list[str]** | WorkloadUpdateMethods defines the methods that can be used to disrupt workloads during automated workload updates. When multiple methods are present, the least disruptive method takes precedence over more disruptive methods. For example if both LiveMigrate and Shutdown methods are listed, only VMs which are not live migratable will be restarted/shutdown  An empty list defaults to no automated workload updating | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


