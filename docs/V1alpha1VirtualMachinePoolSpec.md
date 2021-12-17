# V1alpha1VirtualMachinePoolSpec

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**paused** | **bool** | Indicates that the pool is paused. | [optional] 
**replicas** | **int** | Number of desired pods. This is a pointer to distinguish between explicit zero and not specified. Defaults to 1. | [optional] 
**selector** | [**K8sIoApimachineryPkgApisMetaV1LabelSelector**](K8sIoApimachineryPkgApisMetaV1LabelSelector.md) | Label selector for pods. Existing Poolss whose pods are selected by this will be the ones affected by this deployment. | 
**virtual_machine_template** | [**V1alpha1VirtualMachineTemplateSpec**](V1alpha1VirtualMachineTemplateSpec.md) | Template describes the VM that will be created. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


