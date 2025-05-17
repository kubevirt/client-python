# V1VirtualMachineInstanceMigrationSpec

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**added_node_selector** | **dict(str, str)** | AddedNodeSelector is an additional selector that can be used to complement a NodeSelector or NodeAffinity as set on the VM to restrict the set of allowed target nodes for a migration. In case of key collisions, values set on the VM objects are going to be preserved to ensure that addedNodeSelector can only restrict but not bypass constraints already set on the VM object. | [optional] 
**receive** | [**V1VirtualMachineInstanceMigrationTarget**](V1VirtualMachineInstanceMigrationTarget.md) | If receieve is specified, this VirtualMachineInstanceMigration will be considered the target | [optional] 
**send_to** | [**V1VirtualMachineInstanceMigrationSource**](V1VirtualMachineInstanceMigrationSource.md) | If sendTo is specified, this VirtualMachineInstanceMigration will be considered the source | [optional] 
**vmi_name** | **str** | The name of the VMI to perform the migration on. VMI must exist in the migration objects namespace | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


