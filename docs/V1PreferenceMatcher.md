# V1PreferenceMatcher

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**infer_from_volume** | **str** | InferFromVolume lists the name of a volume that should be used to infer or discover the preference to be used through known annotations on the underlying resource. Once applied to the PreferenceMatcher this field is removed. | [optional] 
**infer_from_volume_failure_policy** | **str** | InferFromVolumeFailurePolicy controls what should happen on failure when preference the instancetype. Allowed values are: \&quot;RejectInferFromVolumeFailure\&quot; and \&quot;IgnoreInferFromVolumeFailure\&quot;. If not specified, \&quot;RejectInferFromVolumeFailure\&quot; is used by default. | [optional] 
**kind** | **str** | Kind specifies which preference resource is referenced. Allowed values are: \&quot;VirtualMachinePreference\&quot; and \&quot;VirtualMachineClusterPreference\&quot;. If not specified, \&quot;VirtualMachineClusterPreference\&quot; is used by default. | [optional] 
**name** | **str** | Name is the name of the VirtualMachinePreference or VirtualMachineClusterPreference | [optional] 
**revision_name** | **str** | RevisionName specifies a ControllerRevision containing a specific copy of the VirtualMachinePreference or VirtualMachineClusterPreference to be used. This is initially captured the first time the instancetype is applied to the VirtualMachineInstance. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


