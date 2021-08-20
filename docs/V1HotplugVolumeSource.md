# V1HotplugVolumeSource

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data_volume** | [**V1DataVolumeSource**](V1DataVolumeSource.md) | DataVolume represents the dynamic creation a PVC for this volume as well as the process of populating that PVC with a disk image. | [optional] 
**persistent_volume_claim** | [**V1PersistentVolumeClaimVolumeSource**](V1PersistentVolumeClaimVolumeSource.md) | PersistentVolumeClaimVolumeSource represents a reference to a PersistentVolumeClaim in the same namespace. Directly attached to the vmi via qemu. More info: https://kubernetes.io/docs/concepts/storage/persistent-volumes#persistentvolumeclaims | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


