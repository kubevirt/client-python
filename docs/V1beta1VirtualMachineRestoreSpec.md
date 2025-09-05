# V1beta1VirtualMachineRestoreSpec

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**patches** | **list[str]** | If the target for the restore does not exist, it will be created. Patches holds JSON patches that would be applied to the target manifest before it&#39;s created. Patches should fit the target&#39;s Kind.  Example for a patch: {\&quot;op\&quot;: \&quot;replace\&quot;, \&quot;path\&quot;: \&quot;/metadata/name\&quot;, \&quot;value\&quot;: \&quot;new-vm-name\&quot;} | [optional] 
**target** | [**K8sIoApiCoreV1TypedLocalObjectReference**](K8sIoApiCoreV1TypedLocalObjectReference.md) | initially only VirtualMachine type supported | 
**target_readiness_policy** | **str** |  | [optional] 
**virtual_machine_snapshot_name** | **str** |  | [default to '']
**volume_ownership_policy** | **str** |  | [optional] 
**volume_restore_overrides** | [**list[V1beta1VolumeRestoreOverride]**](V1beta1VolumeRestoreOverride.md) | VolumeRestoreOverrides gives the option to change properties of each restored volume For example, specifying the name of the restored volume, or adding labels/annotations to it | [optional] 
**volume_restore_policy** | **str** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


