# V1VirtualMachineInstanceMigrationState

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**abort_requested** | **bool** | Indicates that the migration has been requested to abort | [optional] 
**abort_status** | **str** | Indicates the final status of the live migration abortion | [optional] 
**completed** | **bool** | Indicates the migration completed | [optional] 
**end_timestamp** | [**K8sIoApimachineryPkgApisMetaV1Time**](K8sIoApimachineryPkgApisMetaV1Time.md) | The time the migration action ended | [optional] 
**failed** | **bool** | Indicates that the migration failed | [optional] 
**failure_reason** | **str** | Contains the reason why the migration failed | [optional] 
**migration_configuration** | [**V1MigrationConfiguration**](V1MigrationConfiguration.md) | Migration configurations to apply | [optional] 
**migration_policy_name** | **str** | Name of the migration policy. If string is empty, no policy is matched | [optional] 
**migration_uid** | **str** | The VirtualMachineInstanceMigration object associated with this migration | [optional] 
**mode** | **str** | Lets us know if the vmi is currently running pre or post copy migration | [optional] 
**source_node** | **str** | The source node that the VMI originated on | [optional] 
**source_persistent_state_pvc_name** | **str** | If the VMI being migrated uses persistent features (backend-storage), its source PVC name is saved here | [optional] 
**source_pod** | **str** |  | [optional] 
**start_timestamp** | [**K8sIoApimachineryPkgApisMetaV1Time**](K8sIoApimachineryPkgApisMetaV1Time.md) | The time the migration action began | [optional] 
**target_attachment_pod_uid** | **str** | The UID of the target attachment pod for hotplug volumes | [optional] 
**target_cpu_set** | **list[int]** | If the VMI requires dedicated CPUs, this field will hold the dedicated CPU set on the target node | [optional] 
**target_direct_migration_node_ports** | **dict(str, int)** | The list of ports opened for live migration on the destination node | [optional] 
**target_node** | **str** | The target node that the VMI is moving to | [optional] 
**target_node_address** | **str** | The address of the target node to use for the migration | [optional] 
**target_node_domain_detected** | **bool** | The Target Node has seen the Domain Start Event | [optional] 
**target_node_domain_ready_timestamp** | [**K8sIoApimachineryPkgApisMetaV1Time**](K8sIoApimachineryPkgApisMetaV1Time.md) | The timestamp at which the target node detects the domain is active | [optional] 
**target_node_topology** | **str** | If the VMI requires dedicated CPUs, this field will hold the numa topology on the target node | [optional] 
**target_persistent_state_pvc_name** | **str** | If the VMI being migrated uses persistent features (backend-storage), its target PVC name is saved here | [optional] 
**target_pod** | **str** | The target pod that the VMI is moving to | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


