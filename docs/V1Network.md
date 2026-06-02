# V1Network

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**multus** | [**V1MultusNetwork**](V1MultusNetwork.md) |  | [optional] 
**name** | **str** | Network name. Must be a DNS_LABEL and unique within the vm. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names | [default to '']
**pod** | [**V1PodNetwork**](V1PodNetwork.md) |  | [optional] 
**resource_claim** | [**V1ClaimRequest**](V1ClaimRequest.md) | ResourceClaim represents a network resource requested via a VMI spec.resourceClaims[] entry, backed by either a Kubernetes ResourceClaim or ResourceClaimTemplate. This field should only be configured if the NetworkDevicesWithDRA feature-gate is enabled. This feature is in alpha. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


