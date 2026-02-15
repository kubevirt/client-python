# V1Interface

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**acpi_index** | **int** | If specified, the ACPI index is used to provide network interface device naming, that is stable across changes in PCI addresses assigned to the device. This value is required to be unique across all devices and be between 1 and (16*1024-1). | [optional] 
**binding** | [**V1PluginBinding**](V1PluginBinding.md) | Binding specifies the binding plugin that will be used to connect the interface to the guest. It provides an alternative to InterfaceBindingMethod. version: 1alphav1 | [optional] 
**boot_order** | **int** | BootOrder is an integer value &gt; 0, used to determine ordering of boot devices. Lower values take precedence. Each interface or disk that has a boot order must have a unique value. Interfaces without a boot order are not tried. | [optional] 
**bridge** | [**V1InterfaceBridge**](V1InterfaceBridge.md) |  | [optional] 
**dhcp_options** | [**V1DHCPOptions**](V1DHCPOptions.md) | If specified the network interface will pass additional DHCP options to the VMI | [optional] 
**mac_address** | **str** | Interface MAC address. For example: de:ad:00:00:be:af or DE-AD-00-00-BE-AF. | [optional] 
**macvtap** | [**V1DeprecatedInterfaceMacvtap**](V1DeprecatedInterfaceMacvtap.md) | DeprecatedMacvtap is an alias to the deprecated Macvtap interface, please refer to Kubevirt user guide for alternatives. Deprecated: Removed in v1.3 | [optional] 
**masquerade** | [**V1InterfaceMasquerade**](V1InterfaceMasquerade.md) |  | [optional] 
**model** | **str** | Interface model. One of: e1000, e1000e, igb, ne2k_pci, pcnet, rtl8139, virtio. Defaults to virtio. | [optional] 
**name** | **str** | Logical name of the interface as well as a reference to the associated networks. Must match the Name of a Network. | [default to '']
**passt** | [**V1DeprecatedInterfacePasst**](V1DeprecatedInterfacePasst.md) | DeprecatedPasst is an alias to the deprecated Passt interface, please refer to Kubevirt user guide for alternatives. Deprecated: Removed in v1.3 | [optional] 
**passt_binding** | [**V1InterfacePasstBinding**](V1InterfacePasstBinding.md) |  | [optional] 
**pci_address** | **str** | If specified, the virtual network interface will be placed on the guests pci address with the specified PCI address. For example: 0000:81:01.10 | [optional] 
**ports** | [**list[V1Port]**](V1Port.md) | List of ports to be forwarded to the virtual machine. | [optional] 
**slirp** | [**V1DeprecatedInterfaceSlirp**](V1DeprecatedInterfaceSlirp.md) | DeprecatedSlirp is an alias to the deprecated Slirp interface Deprecated: Removed in v1.3 | [optional] 
**sriov** | [**V1InterfaceSRIOV**](V1InterfaceSRIOV.md) |  | [optional] 
**state** | **str** | State represents the requested operational state of the interface. The supported values are: &#x60;absent&#x60;, expressing a request to remove the interface. &#x60;down&#x60;, expressing a request to set the link down. &#x60;up&#x60;, expressing a request to set the link up. Empty value functions as &#x60;up&#x60;. | [optional] 
**tag** | **str** | If specified, the virtual network interface address and its tag will be provided to the guest via config drive | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


