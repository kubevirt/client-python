# V1VirtualMachineMemoryDumpRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**claim_name** | **str** | ClaimName is the name of the pvc that will contain the memory dump | 
**end_timestamp** | [**K8sIoApimachineryPkgApisMetaV1Time**](K8sIoApimachineryPkgApisMetaV1Time.md) | EndTimestamp represents the time the memory dump was completed | [optional] 
**file_name** | **str** | FileName represents the name of the output file | [optional] 
**message** | **str** | Message is a detailed message about failure of the memory dump | [optional] 
**phase** | **str** | Phase represents the memory dump phase | 
**start_timestamp** | [**K8sIoApimachineryPkgApisMetaV1Time**](K8sIoApimachineryPkgApisMetaV1Time.md) | StartTimestamp represents the time the memory dump started | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


