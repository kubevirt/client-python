# V1Interface

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bridge** | [**V1InterfaceBridge**](V1InterfaceBridge.md) |  | [optional] 
**mac_address** | **str** | Interface MAC address. For example: de:ad:00:00:be:af or DE-AD-00-00-BE-AF. | [optional] 
**model** | **str** | Interface model. One of: e1000, e1000e, ne2k_pci, pcnet, rtl8139, virtio. Defaults to virtio. | [optional] 
**name** | **str** | Logical name of the interface as well as a reference to the associated networks. Must match the Name of a Network. | 
**slirp** | [**V1InterfaceSlirp**](V1InterfaceSlirp.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


