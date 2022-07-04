# V1alpha1VirtualMachineCloneSpec

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**annotation_filters** | **list[str]** |  | [optional] 
**label_filters** | **list[str]** |  | [optional] 
**new_mac_addresses** | **dict(str, str)** | NewMacAddresses manually sets that target interfaces&#39; mac addresses. The key is the interface name and the value is the new mac address. If this field is not specified, a new MAC address will be generated automatically, as for any interface that is not included in this map. | [optional] 
**new_sm_bios_serial** | **str** | NewSMBiosSerial manually sets that target&#39;s SMbios serial. If this field is not specified, a new serial will be generated automatically. | [optional] 
**source** | [**K8sIoApiCoreV1TypedLocalObjectReference**](K8sIoApiCoreV1TypedLocalObjectReference.md) |  | 
**target** | [**K8sIoApiCoreV1TypedLocalObjectReference**](K8sIoApiCoreV1TypedLocalObjectReference.md) | If the target is not provided, a random name would be generated for the target. The target&#39;s name can be viewed by inspecting status \&quot;TargetName\&quot; field below. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


