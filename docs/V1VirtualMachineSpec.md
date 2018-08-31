# V1VirtualMachineSpec

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data_volume_templates** | [**list[V1alpha1DataVolume]**](V1alpha1DataVolume.md) | dataVolumeTemplates is a list of dataVolumes that the VirtualMachineInstance template can reference. DataVolumes in this list are dynamically created for the VirtualMachine and are tied to the VirtualMachine&#39;s life-cycle. | [optional] 
**running** | **bool** | Running controls whether the associatied VirtualMachineInstance is created or not | 
**template** | [**V1VirtualMachineInstanceTemplateSpec**](V1VirtualMachineInstanceTemplateSpec.md) | Template is the direct specification of VirtualMachineInstance | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


