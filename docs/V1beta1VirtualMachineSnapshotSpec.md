# V1beta1VirtualMachineSnapshotSpec

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**deletion_policy** | **str** |  | [optional] 
**failure_deadline** | [**IoK8sApimachineryPkgApisMetaV1Duration**](IoK8sApimachineryPkgApisMetaV1Duration.md) | This time represents the number of seconds we permit the vm snapshot to take. In case we pass this deadline we mark this snapshot as failed. Defaults to DefaultFailureDeadline - 5min | [optional] 
**overlay_scratch_size** | [**IoK8sApimachineryPkgApiResourceQuantity**](IoK8sApimachineryPkgApiResourceQuantity.md) | OverlayScratchSize overrides the size of the scratch volume holding the copy-on-write overlays for the duration of an External mode snapshot. When not set, the size is derived from FailureDeadline, capped by the size of the snapshotted disks. This field can only be set when SnapshotMode is External | [optional] 
**snapshot_mode** | **str** | SnapshotMode selects the flow used to snapshot a running VM. Only meaningful for online snapshots; offline snapshots are unaffected. External requires the ExternalVMSnapshot feature gate. Defaults to Direct | [optional] 
**source** | [**IoK8sApiCoreV1TypedLocalObjectReference**](IoK8sApiCoreV1TypedLocalObjectReference.md) |  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


