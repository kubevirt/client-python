# V1beta1DataVolumeSourceRegistry

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cert_config_map** | **str** | CertConfigMap provides a reference to the Registry certs | [optional] 
**image_stream** | **str** | ImageStream is the name of image stream for import | [optional] 
**pull_method** | **str** | PullMethod can be either \&quot;pod\&quot; (default import), or \&quot;node\&quot; (node docker cache based import) | [optional] 
**secret_ref** | **str** | SecretRef provides the secret reference needed to access the Registry source | [optional] 
**url** | **str** | URL is the url of the registry source (starting with the scheme: docker, oci-archive) | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


