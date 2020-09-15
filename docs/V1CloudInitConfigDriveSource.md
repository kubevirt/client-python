# V1CloudInitConfigDriveSource

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**network_data** | **str** | NetworkData contains config drive inline cloud-init networkdata. | [optional] 
**network_data_base64** | **str** | NetworkDataBase64 contains config drive cloud-init networkdata as a base64 encoded string. | [optional] 
**network_data_secret_ref** | [**K8sIoApiCoreV1LocalObjectReference**](K8sIoApiCoreV1LocalObjectReference.md) | NetworkDataSecretRef references a k8s secret that contains config drive networkdata. | [optional] 
**secret_ref** | [**K8sIoApiCoreV1LocalObjectReference**](K8sIoApiCoreV1LocalObjectReference.md) | UserDataSecretRef references a k8s secret that contains config drive userdata. | [optional] 
**user_data** | **str** | UserData contains config drive inline cloud-init userdata. | [optional] 
**user_data_base64** | **str** | UserDataBase64 contains config drive cloud-init userdata as a base64 encoded string. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


