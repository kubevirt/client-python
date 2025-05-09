# V1beta1VirtualMachineCloneSpec

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**annotation_filters** | **list[str]** | Example use: \&quot;!some/key*\&quot;. For a detailed description, please refer to https://kubevirt.io/user-guide/operations/clone_api/#label-annotation-filters. | [optional] 
**label_filters** | **list[str]** | Example use: \&quot;!some/key*\&quot;. For a detailed description, please refer to https://kubevirt.io/user-guide/operations/clone_api/#label-annotation-filters. | [optional] 
**new_mac_addresses** | **dict(str, str)** | NewMacAddresses manually sets that target interfaces&#39; mac addresses. The key is the interface name and the value is the new mac address. If this field is not specified, a new MAC address will be generated automatically, as for any interface that is not included in this map. | [optional] 
**new_sm_bios_serial** | **str** | NewSMBiosSerial manually sets that target&#39;s SMbios serial. If this field is not specified, a new serial will be generated automatically. | [optional] 
**patches** | **list[str]** | Patches holds JSON patches to apply to target. Patches should fit the target&#39;s Kind. Example: &#39;{\&quot;op\&quot;: \&quot;add\&quot;, \&quot;path\&quot;: \&quot;/spec/template/metadata/labels/example\&quot;, \&quot;value\&quot;: \&quot;new-label\&quot;}&#39; | [optional] 
**source** | [**K8sIoApiCoreV1TypedLocalObjectReference**](K8sIoApiCoreV1TypedLocalObjectReference.md) | Source is the object that would be cloned. Currently supported source types are: VirtualMachine of kubevirt.io API group, VirtualMachineSnapshot of snapshot.kubevirt.io API group | 
**target** | [**K8sIoApiCoreV1TypedLocalObjectReference**](K8sIoApiCoreV1TypedLocalObjectReference.md) | Target is the outcome of the cloning process. Currently supported source types are: - VirtualMachine of kubevirt.io API group - Empty (nil). If the target is not provided, the target type would default to VirtualMachine and a random name would be generated for the target. The target&#39;s name can be viewed by inspecting status \&quot;TargetName\&quot; field below. | [optional] 
**template** | [**V1beta1VirtualMachineCloneTemplateFilters**](V1beta1VirtualMachineCloneTemplateFilters.md) | For a detailed description, please refer to https://kubevirt.io/user-guide/operations/clone_api/#label-annotation-filters. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


