# V1SecretVolumeSource

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**optional** | **bool** | Specify whether the Secret or it&#39;s keys must be defined | [optional] 
**secret_name** | **str** | Name of the secret in the pod&#39;s namespace to use. More info: https://kubernetes.io/docs/concepts/storage/volumes#secret | [optional] 
**volume_label** | **str** | The volume label of the resulting disk inside the VMI. Different bootstrapping mechanisms require different values. Typical values are \&quot;cidata\&quot; (cloud-init), \&quot;config-2\&quot; (cloud-init) or \&quot;OEMDRV\&quot; (kickstart). | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


