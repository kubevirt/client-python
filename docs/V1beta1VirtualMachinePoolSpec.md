# V1beta1VirtualMachinePoolSpec

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**autohealing** | [**V1beta1VirtualMachinePoolAutohealingStrategy**](V1beta1VirtualMachinePoolAutohealingStrategy.md) | Autohealing specifies when a VMpool should replace a failing VM with a reprovisioned instance | [optional] 
**max_unavailable** | [**K8sIoApimachineryPkgUtilIntstrIntOrString**](K8sIoApimachineryPkgUtilIntstrIntOrString.md) | (Defaults to 100%) Integer or string pointer, that when set represents either a percentage or number of VMs in a pool that can be unavailable (ready condition false) at a time during automated update. | [optional] 
**name_generation** | [**V1beta1VirtualMachinePoolNameGeneration**](V1beta1VirtualMachinePoolNameGeneration.md) | Options for the name generation in a pool. | [optional] 
**paused** | **bool** | Indicates that the pool is paused. | [optional] 
**replicas** | **int** | Number of desired pods. This is a pointer to distinguish between explicit zero and not specified. Defaults to 1. | [optional] 
**scale_in_strategy** | [**V1beta1VirtualMachinePoolScaleInStrategy**](V1beta1VirtualMachinePoolScaleInStrategy.md) | ScaleInStrategy specifies how the VMPool controller manages scaling in VMs within a VMPool | [optional] 
**selector** | [**K8sIoApimachineryPkgApisMetaV1LabelSelector**](K8sIoApimachineryPkgApisMetaV1LabelSelector.md) | Label selector for pods. Existing Poolss whose pods are selected by this will be the ones affected by this deployment. | 
**update_strategy** | [**V1beta1VirtualMachinePoolUpdateStrategy**](V1beta1VirtualMachinePoolUpdateStrategy.md) | UpdateStrategy specifies how the VMPool controller manages updating VMs within a VMPool | [optional] 
**virtual_machine_template** | [**V1beta1VirtualMachineTemplateSpec**](V1beta1VirtualMachineTemplateSpec.md) | Template describes the VM that will be created. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


