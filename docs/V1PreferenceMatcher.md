# V1PreferenceMatcher

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kind** | **str** | Kind specifies which preference resource is referenced. Allowed values are: \&quot;VirtualMachinePreference\&quot; and \&quot;VirtualMachineClusterPreference\&quot;. If not specified, \&quot;VirtualMachineClusterPreference\&quot; is used by default. | [optional] 
**name** | **str** | Name is the name of the VirtualMachinePreference or VirtualMachineClusterPreference | 
**revision_name** | **str** | RevisionName specifies a ControllerRevision containing a specific copy of the VirtualMachinePreference or VirtualMachineClusterPreference to be used. This is initially captured the first time the instancetype is applied to the VirtualMachineInstance. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


