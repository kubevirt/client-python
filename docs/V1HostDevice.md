# V1HostDevice

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**claim_name** | **str** | ClaimName needs to be provided from the list vmi.spec.resourceClaims[].name where this device is allocated | [optional] 
**device_name** | **str** | DeviceName is the name of the device provisioned by device-plugins | [optional] 
**name** | **str** |  | [default to '']
**request_name** | **str** | RequestName needs to be provided from resourceClaim.spec.devices.requests[].name where this device is requested | [optional] 
**tag** | **str** | If specified, the virtual network interface address and its tag will be provided to the guest via config drive | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


