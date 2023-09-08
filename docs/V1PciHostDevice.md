# V1PciHostDevice

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**external_resource_provider** | **bool** | If true, KubeVirt will leave the allocation and monitoring to an external device plugin | [optional] 
**pci_vendor_selector** | **str** | The vendor_id:product_id tuple of the PCI device | [default to '']
**resource_name** | **str** | The name of the resource that is representing the device. Exposed by a device plugin and requested by VMs. Typically of the form vendor.com/product_name | [default to '']

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


