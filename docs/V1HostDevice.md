# V1HostDevice

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**claim_name** | **str** | ClaimName references the name of an entry in the VMI&#39;s spec.resourceClaims[] array. The referenced entry may use either resourceClaimName or resourceClaimTemplateName. | [optional] 
**device_name** | **str** | DeviceName is the name of the device provisioned by device-plugins | [optional] 
**name** | **str** |  | [default to '']
**request_name** | **str** | RequestName specifies which request from the ResourceClaim/ResourceClaimTemplate spec.devices.requests array this claim request corresponds to. | [optional] 
**tag** | **str** | If specified, the virtual network interface address and its tag will be provided to the guest via config drive | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


