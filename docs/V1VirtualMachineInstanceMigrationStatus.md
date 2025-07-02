# V1VirtualMachineInstanceMigrationStatus

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**conditions** | [**list[V1VirtualMachineInstanceMigrationCondition]**](V1VirtualMachineInstanceMigrationCondition.md) |  | [optional] 
**migration_state** | [**V1VirtualMachineInstanceMigrationState**](V1VirtualMachineInstanceMigrationState.md) | Represents the status of a live migration | [optional] 
**phase** | **str** |  | [optional] 
**phase_transition_timestamps** | [**list[V1VirtualMachineInstanceMigrationPhaseTransitionTimestamp]**](V1VirtualMachineInstanceMigrationPhaseTransitionTimestamp.md) | PhaseTransitionTimestamp is the timestamp of when the last phase change occurred | [optional] 
**synchronization_addresses** | **list[str]** | The synchronization addresses one can use to connect to the synchronization controller, includes the port, if multiple addresses are available, the first one is reported in the synchronizationAddress field. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


