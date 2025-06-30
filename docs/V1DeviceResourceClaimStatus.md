# V1DeviceResourceClaimStatus

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attributes** | [**V1DeviceAttribute**](V1DeviceAttribute.md) | Attributes are properties of the device that could be used by kubevirt and other copmonents to learn more about the device, like pciAddress or mdevUUID | [optional] 
**name** | **str** | Name is the name of actual device on the host provisioned by the driver as reflected in resourceclaim.status | [optional] 
**resource_claim_name** | **str** | ResourceClaimName is the name of the resource claims object used to provision this resource | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


