# V1alpha1VirtualMachineBackupSpec

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**force_full_backup** | **bool** | ForceFullBackup indicates that a full backup is desired | [optional] 
**mode** | **str** | Mode specifies the way the backup output will be recieved | [optional] 
**pvc_name** | **str** | PvcName required in push mode. Specifies the name of the PVC where the backup output will be stored | [optional] 
**skip_quiesce** | **bool** | SkipQuiesce indicates whether the VM&#39;s filesystem shoule not be quiesced before the backup | [optional] 
**source** | [**K8sIoApiCoreV1TypedLocalObjectReference**](K8sIoApiCoreV1TypedLocalObjectReference.md) | Source specifies the backup source - either a VirtualMachine or a VirtualMachineBackupTracker. When Kind is VirtualMachine: performs a backup of the specified VM. When Kind is VirtualMachineBackupTracker: uses the tracker to get the source VM and the base checkpoint for incremental backup. The tracker will be updated with the new checkpoint after backup completion. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


