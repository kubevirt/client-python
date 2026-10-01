# V1alpha1VirtualMachineBackupStatus

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**checkpoint_name** | **str** | CheckpointName the name of the checkpoint created for the current backup | [optional] 
**conditions** | [**list[IoK8sApimachineryPkgApisMetaV1Condition]**](IoK8sApimachineryPkgApisMetaV1Condition.md) |  | [optional] 
**export_uid** | **str** | ExportUID tracks the UID of the associated VMExport for pull-mode backups used to detect VMExport recreation and re-initiate the export handshake | [optional] 
**included_volumes** | [**list[V1alpha1BackupVolumeInfo]**](V1alpha1BackupVolumeInfo.md) | IncludedVolumes lists the volumes that were included in the backup | [optional] 
**links** | [**V1alpha1BackupLinks**](V1alpha1BackupLinks.md) | Links exposes internal (in-cluster) and external (Ingress/Route) endpoints for pull-mode backups, each with a CA certificate and per-volume URLs. Contains per-volume data and map endpoint URLs for each network path. | [optional] 
**type** | **str** | Type indicates if the backup was full or incremental | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


