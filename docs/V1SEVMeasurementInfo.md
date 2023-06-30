# V1SEVMeasurementInfo

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_major** | **int** | API major version of the SEV host. | [optional] 
**api_minor** | **int** | API minor version of the SEV host. | [optional] 
**api_version** | **str** | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources | [optional] 
**build_id** | **int** | Build ID of the SEV host. | [optional] 
**kind** | **str** | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds | [optional] 
**loader_sha** | **str** | SHA256 of the loader binary | [optional] 
**measurement** | **str** | Base64 encoded launch measurement of the SEV guest. | [optional] 
**policy** | **int** | Policy of the SEV guest. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


