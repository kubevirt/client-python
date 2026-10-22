# V1VirtualMachineStateSpec

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source** | [**V1VirtualMachineStateSource**](V1VirtualMachineStateSource.md) | Source is an existing PVC to adopt as the starting VirtualMachineState. The controller does not take ownership of a PVC referenced this way. | [optional] 
**volume_claim_template** | [**IoK8sApiCoreV1PersistentVolumeClaimTemplate**](IoK8sApiCoreV1PersistentVolumeClaimTemplate.md) | VolumeClaimTemplate is the template the controller uses to create PVCs it owns. It is used for the initial PVC when Source is unset, and for every new PVC the controller creates later for operations like live migration. The controller owns the PVC name via GenerateName, so volumeClaimTemplate.metadata.name must not be set. The referenced volume mode must be Filesystem. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


