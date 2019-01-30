# V1CloudInitNoCloudSource

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**network_data** | **str** | NetworkData contains NoCloud inline cloud-init networkdata. + optional | [optional] 
**network_data_base64** | **str** | NetworkDataBase64 contains NoCloud cloud-init networkdata as a base64 encoded string. + optional | [optional] 
**network_data_secret_ref** | [**V1LocalObjectReference**](V1LocalObjectReference.md) | NetworkDataSecretRef references a k8s secret that contains NoCloud networkdata. + optional | [optional] 
**secret_ref** | [**V1LocalObjectReference**](V1LocalObjectReference.md) | UserDataSecretRef references a k8s secret that contains NoCloud userdata. + optional | [optional] 
**user_data** | **str** | UserData contains NoCloud inline cloud-init userdata. + optional | [optional] 
**user_data_base64** | **str** | UserDataBase64 contains NoCloud cloud-init userdata as a base64 encoded string. + optional | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


