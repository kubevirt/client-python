# V1InterfaceBindingPlugin

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**domain_attachment_type** | **str** | DomainAttachmentType is a standard domain network attachment method kubevirt supports. Supported values: \&quot;tap\&quot;. The standard domain attachment can be used instead or in addition to the sidecarImage. version: 1alphav1 | [optional] 
**network_attachment_definition** | **str** | NetworkAttachmentDefinition references to a NetworkAttachmentDefinition CR object. Format: &lt;name&gt;, &lt;namespace&gt;/&lt;name&gt;. If namespace is not specified, VMI namespace is assumed. version: 1alphav1 | [optional] 
**sidecar_image** | **str** | SidecarImage references a container image that runs in the virt-launcher pod. The sidecar handles (libvirt) domain configuration and optional services. version: 1alphav1 | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


