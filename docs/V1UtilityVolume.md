# V1UtilityVolume

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**claim_name** | **str** | claimName is the name of a PersistentVolumeClaim in the same namespace as the pod using this volume. More info: https://kubernetes.io/docs/concepts/storage/persistent-volumes#persistentvolumeclaims | [default to '']
**name** | **str** | UtilityVolume&#39;s name. Must be unique within the vmi, including regular Volumes. | [default to '']
**read_only** | **bool** | readOnly Will force the ReadOnly setting in VolumeMounts. Default false. | [optional] 
**type** | **str** | Type represents the type of the utility volume. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


