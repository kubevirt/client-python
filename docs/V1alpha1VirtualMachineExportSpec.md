# V1alpha1VirtualMachineExportSpec

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source** | [**K8sIoApiCoreV1TypedLocalObjectReference**](K8sIoApiCoreV1TypedLocalObjectReference.md) |  | 
**token_secret_ref** | **str** | TokenSecretRef is the name of the custom-defined secret that contains the token used by the export server pod | [optional] 
**ttl_duration** | [**K8sIoApimachineryPkgApisMetaV1Duration**](K8sIoApimachineryPkgApisMetaV1Duration.md) | ttlDuration limits the lifetime of an export If this field is set, after this duration has passed from counting from CreationTimestamp, the export is eligible to be automatically deleted. If this field is omitted, a reasonable default is applied. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


