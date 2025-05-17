# V1VirtualMachineInstanceMigrationTargetState

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attachment_pod_uid** | **str** | The UID of the target attachment pod for hotplug volumes | [optional] 
**cpu_set** | **list[int]** | If the VMI requires dedicated CPUs, this field will hold the dedicated CPU set on the target node | [optional] 
**direct_migration_node_ports** | **dict(str, int)** | The list of ports opened for live migration on the destination node | [optional] 
**domain_detected** | **bool** | The Target Node has seen the Domain Start Event | [optional] 
**domain_name** | **str** | The name of the domain on the source libvirt domain | [optional] 
**domain_namespace** | **str** | Namespace used in the name of the source libvirt domain. Can be used to find and modify paths in the domain | [optional] 
**domain_ready_timestamp** | [**K8sIoApimachineryPkgApisMetaV1Time**](K8sIoApimachineryPkgApisMetaV1Time.md) | The timestamp at which the target node detects the domain is active | [optional] 
**migration_uid** | **str** | The Source VirtualMachineInstanceMigration object associated with this migration | [optional] 
**node** | **str** | The source node that the VMI originated on | [optional] 
**node_address** | **str** | The address of the target node to use for the migration | [optional] 
**node_topology** | **str** | If the VMI requires dedicated CPUs, this field will hold the numa topology on the target node | [optional] 
**persistent_state_pvc_name** | **str** | If the VMI being migrated uses persistent features (backend-storage), its source PVC name is saved here | [optional] 
**pod** | **str** | The source pod that the VMI is originated on | [optional] 
**sync_address** | **str** | The ip address/fqdn:port combination to use to synchronize the VMI with the target. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


