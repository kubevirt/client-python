# V1ComponentConfig

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**node_placement** | [**V1NodePlacement**](V1NodePlacement.md) | nodePlacement describes scheduling configuration for specific KubeVirt components | [optional] 
**replicas** | **int** | replicas indicates how many replicas should be created for each KubeVirt infrastructure component (like virt-api or virt-controller). Defaults to 2. WARNING: this is an advanced feature that prevents auto-scaling for core kubevirt components. Please use with caution! | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


