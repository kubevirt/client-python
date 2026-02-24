# V1ContainerPathVolumeSource

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**path** | **str** | Path is the absolute path within the virt-launcher container to expose to the VM. The path must correspond to an existing volumeMount in the compute container. | [default to '']
**read_only** | **bool** | ReadOnly controls whether the volume is exposed as read-only to the VM. Defaults to true. Write access is not currently supported. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


