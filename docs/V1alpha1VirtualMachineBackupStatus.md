# V1alpha1VirtualMachineBackupStatus

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**checkpoint_name** | **str** | CheckpointName the name of the checkpoint created for the current backup | [optional] 
**conditions** | [**list[V1alpha1Condition]**](V1alpha1Condition.md) |  | [optional] 
**included_volumes** | [**list[V1alpha1BackupVolumeInfo]**](V1alpha1BackupVolumeInfo.md) | IncludedVolumes lists the volumes that were included in the backup | [optional] 
**type** | **str** | Type indicates if the backup was full or incremental | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


