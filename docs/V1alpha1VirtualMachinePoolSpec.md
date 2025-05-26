# V1alpha1VirtualMachinePoolSpec

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**max_unavailable** | [**K8sIoApimachineryPkgUtilIntstrIntOrString**](K8sIoApimachineryPkgUtilIntstrIntOrString.md) | (Defaults to 100%) Integer or string pointer, that when set represents either a percentage or number of VMs in a pool that can be unavailable (ready condition false) at a time during automated update. | [optional] 
**name_generation** | [**V1alpha1VirtualMachinePoolNameGeneration**](V1alpha1VirtualMachinePoolNameGeneration.md) | Options for the name generation in a pool. | [optional] 
**paused** | **bool** | Indicates that the pool is paused. | [optional] 
**replicas** | **int** | Number of desired pods. This is a pointer to distinguish between explicit zero and not specified. Defaults to 1. | [optional] 
**selector** | [**K8sIoApimachineryPkgApisMetaV1LabelSelector**](K8sIoApimachineryPkgApisMetaV1LabelSelector.md) | Label selector for pods. Existing Poolss whose pods are selected by this will be the ones affected by this deployment. | 
**virtual_machine_template** | [**V1alpha1VirtualMachineTemplateSpec**](V1alpha1VirtualMachineTemplateSpec.md) | Template describes the VM that will be created. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


