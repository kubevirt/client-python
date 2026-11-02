# V1beta1BackupOptions

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**abort_reason** | **str** | AbortReason is set when Cmd is Abort. Cancel marks the backup Failed (TTL expiry, or deleting a push-mode backup). Finalize marks a pull-mode backup Complete after the client finished pulling. | [optional] 
**backup_name** | **str** |  | [optional] 
**backup_start_time** | [**IoK8sApimachineryPkgApisMetaV1Time**](IoK8sApimachineryPkgApisMetaV1Time.md) |  | [optional] 
**cmd** | **str** |  | [optional] 
**incremental** | **str** |  | [optional] 
**incremental_creation_time** | [**IoK8sApimachineryPkgApisMetaV1Time**](IoK8sApimachineryPkgApisMetaV1Time.md) |  | [optional] 
**mode** | **str** |  | [optional] 
**skip_quiesce** | **bool** |  | [optional] 
**target_path** | **str** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


