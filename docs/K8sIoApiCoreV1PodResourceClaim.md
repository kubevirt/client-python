# K8sIoApiCoreV1PodResourceClaim

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name uniquely identifies this resource claim inside the pod. This must be a DNS_LABEL. | [default to '']
**resource_claim_name** | **str** | ResourceClaimName is the name of a ResourceClaim object in the same namespace as this pod.  Exactly one of ResourceClaimName and ResourceClaimTemplateName must be set. | [optional] 
**resource_claim_template_name** | **str** | ResourceClaimTemplateName is the name of a ResourceClaimTemplate object in the same namespace as this pod.  The template will be used to create a new ResourceClaim, which will be bound to this pod. When this pod is deleted, the ResourceClaim will also be deleted. The pod name and resource name, along with a generated component, will be used to form a unique name for the ResourceClaim, which will be recorded in pod.status.resourceClaimStatuses.  This field is immutable and no changes will be made to the corresponding ResourceClaim by the control plane after creating the ResourceClaim.  Exactly one of ResourceClaimName and ResourceClaimTemplateName must be set. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


