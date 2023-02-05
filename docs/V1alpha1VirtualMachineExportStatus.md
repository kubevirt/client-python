# V1alpha1VirtualMachineExportStatus

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**conditions** | [**list[V1alpha1Condition]**](V1alpha1Condition.md) |  | [optional] 
**links** | [**V1alpha1VirtualMachineExportLinks**](V1alpha1VirtualMachineExportLinks.md) |  | [optional] 
**phase** | **str** |  | [optional] 
**service_name** | **str** | ServiceName is the name of the service created associated with the Virtual Machine export. It will be used to create the internal URLs for downloading the images | [optional] 
**token_secret_ref** | **str** | TokenSecretRef is the name of the secret that contains the token used by the export server pod | [optional] 
**ttl_expiration_time** | [**K8sIoApimachineryPkgApisMetaV1Time**](K8sIoApimachineryPkgApisMetaV1Time.md) | The time at which the VM Export will be completely removed according to specified TTL Formula is CreationTimestamp + TTL | [optional] 
**virtual_machine_name** | **str** | VirtualMachineName shows the name of the source virtual machine if the source is either a VirtualMachine or a VirtualMachineSnapshot. This is mainly to easily identify the source VirtualMachine in case of a VirtualMachineSnapshot | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


