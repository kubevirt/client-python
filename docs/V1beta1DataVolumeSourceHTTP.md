# V1beta1DataVolumeSourceHTTP

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cert_config_map** | **str** | CertConfigMap is a configmap reference, containing a Certificate Authority(CA) public key, and a base64 encoded pem certificate | [optional] 
**extra_headers** | **list[str]** | ExtraHeaders is a list of strings containing extra headers to include with HTTP transfer requests | [optional] 
**secret_extra_headers** | **list[str]** | SecretExtraHeaders is a list of Secret references, each containing an extra HTTP header that may include sensitive information | [optional] 
**secret_ref** | **str** | SecretRef A Secret reference, the secret should contain accessKeyId (user name) base64 encoded, and secretKey (password) also base64 encoded | [optional] 
**url** | **str** | URL is the URL of the http(s) endpoint | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


