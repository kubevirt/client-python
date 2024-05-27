# V1beta1VirtualMachineSnapshotSpec

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**deletion_policy** | **str** |  | [optional] 
**failure_deadline** | [**K8sIoApimachineryPkgApisMetaV1Duration**](K8sIoApimachineryPkgApisMetaV1Duration.md) | This time represents the number of seconds we permit the vm snapshot to take. In case we pass this deadline we mark this snapshot as failed. Defaults to DefaultFailureDeadline - 5min | [optional] 
**source** | [**K8sIoApiCoreV1TypedLocalObjectReference**](K8sIoApiCoreV1TypedLocalObjectReference.md) |  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


