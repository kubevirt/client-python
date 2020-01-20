# V1RestartOptions

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_version** | **str** | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources | [optional] 
**grace_period_seconds** | **int** | The duration in seconds before the object should be force-restared. Value must be non-negative integer. The value zero indicates, restart immediately. If this value is nil, the default grace period for deletion of the corresponding VMI for the specified type will be used to determine on how much time to give the VMI to restart. Defaults to a per object value if not specified. zero means restart immediately. Allowed Values: nil and 0 +optional | [optional] 
**kind** | **str** | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


