# V1KubeVirtSelfSignConfiguration

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ca** | [**V1CertConfig**](V1CertConfig.md) | CA configuration CA certs are kept in the CA bundle as long as they are valid | [optional] 
**ca_overlap_interval** | [**K8sIoApimachineryPkgApisMetaV1Duration**](K8sIoApimachineryPkgApisMetaV1Duration.md) | Deprecated. Use CA.Duration and CA.RenewBefore instead | [optional] 
**ca_rotate_interval** | [**K8sIoApimachineryPkgApisMetaV1Duration**](K8sIoApimachineryPkgApisMetaV1Duration.md) | Deprecated. Use CA.Duration instead | [optional] 
**cert_rotate_interval** | [**K8sIoApimachineryPkgApisMetaV1Duration**](K8sIoApimachineryPkgApisMetaV1Duration.md) | Deprecated. Use Server.Duration instead | [optional] 
**server** | [**V1CertConfig**](V1CertConfig.md) | Server configuration Certs are rotated and discarded | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


