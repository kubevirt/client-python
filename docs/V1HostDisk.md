# V1HostDisk

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**capacity** | [**K8sIoApimachineryPkgApiResourceQuantity**](K8sIoApimachineryPkgApiResourceQuantity.md) | Capacity of the sparse disk | [optional] 
**path** | **str** | The path to HostDisk image located on the cluster | [default to '']
**shared** | **bool** | Shared indicate whether the path is shared between nodes | [optional] 
**type** | **str** | Contains information if disk.img exists or should be created allowed options are &#39;Disk&#39; and &#39;DiskOrCreate&#39; | [default to '']

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


