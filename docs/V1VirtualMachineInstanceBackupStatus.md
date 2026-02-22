# V1VirtualMachineInstanceBackupStatus

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**backup_msg** | **str** | BackupMsg resturns any relevant information like failure reason unfreeze failed etc... | [optional] 
**backup_name** | **str** | BackupName is the name of the executed backup | [optional] 
**checkpoint_name** | **str** | CheckpointName is the name of the checkpoint created for the backup | [optional] 
**completed** | **bool** | Completed indicates the backup completed | [optional] 
**end_timestamp** | [**K8sIoApimachineryPkgApisMetaV1Time**](K8sIoApimachineryPkgApisMetaV1Time.md) | EndTimestamp is the timestamp when the backup ended | [optional] 
**failed** | **bool** | Failed indicates that the backup failed | [optional] 
**start_timestamp** | [**K8sIoApimachineryPkgApisMetaV1Time**](K8sIoApimachineryPkgApisMetaV1Time.md) | StartTimestamp is the timestamp when the backup started | [optional] 
**volumes** | [**list[V1alpha1BackupVolumeInfo]**](V1alpha1BackupVolumeInfo.md) | Volumes lists the volumes included in the backup | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


