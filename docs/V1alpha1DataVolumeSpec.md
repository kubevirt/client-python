# V1alpha1DataVolumeSpec

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**content_type** | **str** | DataVolumeContentType options: \&quot;kubevirt\&quot;, \&quot;archive\&quot; | [optional] 
**pvc** | [**K8sIoApiCoreV1PersistentVolumeClaimSpec**](K8sIoApiCoreV1PersistentVolumeClaimSpec.md) | PVC is the PVC specification | 
**source** | [**V1alpha1DataVolumeSource**](V1alpha1DataVolumeSource.md) | Source is the src of the data for the requested DataVolume | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


