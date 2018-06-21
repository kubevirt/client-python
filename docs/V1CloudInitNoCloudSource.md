# V1CloudInitNoCloudSource

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**secret_ref** | [**V1LocalObjectReference**](V1LocalObjectReference.md) | UserDataSecretRef references a k8s secret that contains NoCloud userdata. + optional | [optional] 
**user_data** | **str** | UserData contains NoCloud inline cloud-init userdata. + optional | [optional] 
**user_data_base64** | **str** | UserDataBase64 contains NoCloud cloud-init userdata as a base64 encoded string. + optional | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


