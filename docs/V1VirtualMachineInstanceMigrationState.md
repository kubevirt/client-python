# V1VirtualMachineInstanceMigrationState

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**completed** | **bool** | Indicates the migration completed | [optional] 
**end_timestamp** | **str** | The time the migration action ended | [optional] 
**failed** | **bool** | Indicates that the migration failed | [optional] 
**migration_uid** | **str** | The VirtualMachineInstanceMigration object associated with this migration | [optional] 
**source_node** | **str** | The source node that the VMI originated on | [optional] 
**start_timestamp** | **str** | The time the migration action began | [optional] 
**target_direct_migration_node_ports** | **object** | The list of ports opened for live migration on the destination node | [optional] 
**target_node** | **str** | The target node that the VMI is moving to | [optional] 
**target_node_address** | **str** | The address of the target node to use for the migration | [optional] 
**target_node_domain_detected** | **bool** | The Target Node has seen the Domain Start Event | [optional] 
**target_pod** | **str** | The target pod that the VMI is moving to | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


