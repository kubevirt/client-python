# V1DownwardAPIVolumeSource

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fields** | [**list[K8sIoApiCoreV1DownwardAPIVolumeFile]**](K8sIoApiCoreV1DownwardAPIVolumeFile.md) | Fields is a list of downward API volume file | [optional] 
**volume_label** | **str** | The volume label of the resulting disk inside the VMI. Different bootstrapping mechanisms require different values. Typical values are \&quot;cidata\&quot; (cloud-init), \&quot;config-2\&quot; (cloud-init) or \&quot;OEMDRV\&quot; (kickstart). | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


