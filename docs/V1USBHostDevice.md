# V1USBHostDevice

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**external_resource_provider** | **bool** | If true, KubeVirt will leave the allocation and monitoring to an external device plugin | [optional] 
**resource_name** | **str** | Identifies the list of USB host devices. e.g: kubevirt.io/storage, kubevirt.io/bootable-usb, etc | [default to '']
**selectors** | [**list[V1USBSelector]**](V1USBSelector.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


