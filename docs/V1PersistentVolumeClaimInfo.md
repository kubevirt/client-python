# V1PersistentVolumeClaimInfo

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_modes** | **list[str]** | AccessModes contains the desired access modes the volume should have. More info: https://kubernetes.io/docs/concepts/storage/persistent-volumes#access-modes-1 | [optional] 
**capacity** | [**dict(str, K8sIoApimachineryPkgApiResourceQuantity)**](K8sIoApimachineryPkgApiResourceQuantity.md) | Capacity represents the capacity set on the corresponding PVC spec | [optional] 
**preallocated** | **bool** | Preallocated indicates if the PVC&#39;s storage is preallocated or not | [optional] 
**volume_mode** | **str** | VolumeMode defines what type of volume is required by the claim. Value of Filesystem is implied when not included in claim spec. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


