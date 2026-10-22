# IoK8sApiCoreV1PersistentVolumeClaimTemplate

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metadata** | [**IoK8sApimachineryPkgApisMetaV1ObjectMeta**](IoK8sApimachineryPkgApisMetaV1ObjectMeta.md) | May contain labels and annotations that will be copied into the PVC when creating it. No other fields are allowed and will be rejected during validation. | [optional] 
**spec** | [**IoK8sApiCoreV1PersistentVolumeClaimSpec**](IoK8sApiCoreV1PersistentVolumeClaimSpec.md) | The specification for the PersistentVolumeClaim. The entire content is copied unchanged into the PVC that gets created from this template. The same fields as in a PersistentVolumeClaim are also valid here. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


