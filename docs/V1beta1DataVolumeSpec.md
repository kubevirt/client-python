# V1beta1DataVolumeSpec

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**checkpoints** | [**list[V1beta1DataVolumeCheckpoint]**](V1beta1DataVolumeCheckpoint.md) | Checkpoints is a list of DataVolumeCheckpoints, representing stages in a multistage import. | [optional] 
**content_type** | **str** | DataVolumeContentType options: \&quot;kubevirt\&quot;, \&quot;archive\&quot; | [optional] 
**final_checkpoint** | **bool** | FinalCheckpoint indicates whether the current DataVolumeCheckpoint is the final checkpoint. | [optional] 
**preallocation** | **bool** | Preallocation controls whether storage for DataVolumes should be allocated in advance. | [optional] 
**priority_class_name** | **str** | PriorityClassName for Importer, Cloner and Uploader pod | [optional] 
**pvc** | [**K8sIoApiCoreV1PersistentVolumeClaimSpec**](K8sIoApiCoreV1PersistentVolumeClaimSpec.md) | PVC is the PVC specification | [optional] 
**source** | [**V1beta1DataVolumeSource**](V1beta1DataVolumeSource.md) | Source is the src of the data for the requested DataVolume | [optional] 
**source_ref** | [**V1beta1DataVolumeSourceRef**](V1beta1DataVolumeSourceRef.md) | SourceRef is an indirect reference to the source of data for the requested DataVolume | [optional] 
**storage** | [**V1beta1StorageSpec**](V1beta1StorageSpec.md) | Storage is the requested storage specification | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


