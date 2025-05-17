# V1VirtualMachineInstanceMigrationSourceState

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**domain_name** | **str** | The name of the domain on the source libvirt domain | [optional] 
**domain_namespace** | **str** | Namespace used in the name of the source libvirt domain. Can be used to find and modify paths in the domain | [optional] 
**migration_uid** | **str** | The Source VirtualMachineInstanceMigration object associated with this migration | [optional] 
**node** | **str** | The source node that the VMI originated on | [optional] 
**node_selectors** | **dict(str, str)** | Node selectors needed by the target to start the receiving pod. | [optional] 
**persistent_state_pvc_name** | **str** | If the VMI being migrated uses persistent features (backend-storage), its source PVC name is saved here | [optional] 
**pod** | **str** | The source pod that the VMI is originated on | [optional] 
**sync_address** | **str** | The ip address/fqdn:port combination to use to synchronize the VMI with the target. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


