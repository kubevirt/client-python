# V1VMReplicaSetSpec

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**replicas** | **int** | Number of desired pods. This is a pointer to distinguish between explicit zero and not specified. Defaults to 1. +optional | [optional]
**selector** | [**V1LabelSelector**](V1LabelSelector.md) | Label selector for pods. Existing ReplicaSets whose pods are selected by this will be the ones affected by this deployment. +optional | [optional]
**template** | [**V1VMTemplateSpec**](V1VMTemplateSpec.md) | Template describes the pods that will be created. |
**paused** | **bool** | Indicates that the replica set is paused. +optional | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


