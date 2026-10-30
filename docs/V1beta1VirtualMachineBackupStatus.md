# V1beta1VirtualMachineBackupStatus

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**checkpoint_name** | **str** | CheckpointName the name of the checkpoint created for the current backup | [optional] 
**conditions** | [**list[IoK8sApimachineryPkgApisMetaV1Condition]**](IoK8sApimachineryPkgApisMetaV1Condition.md) |  | [optional] 
**included_volumes** | [**list[V1beta1BackupVolumeInfo]**](V1beta1BackupVolumeInfo.md) | IncludedVolumes lists the volumes that were included in the backup | [optional] 
**links** | [**V1beta1BackupLinks**](V1beta1BackupLinks.md) | Links exposes internal (in-cluster) and external (Ingress/Route) endpoints for pull-mode backups, each with a CA certificate and per-volume URLs. Contains per-volume data and map endpoint URLs for each network path. | [optional] 
**start_timestamp** | [**IoK8sApimachineryPkgApisMetaV1Time**](IoK8sApimachineryPkgApisMetaV1Time.md) | StartTimestamp is the timestamp when the backup started | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


