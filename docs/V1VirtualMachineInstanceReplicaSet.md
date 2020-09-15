# V1VirtualMachineInstanceReplicaSet

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_version** | **str** | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources | [optional] 
**kind** | **str** | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds | [optional] 
**metadata** | [**K8sIoApimachineryPkgApisMetaV1ObjectMeta**](K8sIoApimachineryPkgApisMetaV1ObjectMeta.md) |  | [optional] 
**spec** | [**V1VirtualMachineInstanceReplicaSetSpec**](V1VirtualMachineInstanceReplicaSetSpec.md) | VirtualMachineInstance Spec contains the VirtualMachineInstance specification. | 
**status** | [**V1VirtualMachineInstanceReplicaSetStatus**](V1VirtualMachineInstanceReplicaSetStatus.md) | Status is the high level overview of how the VirtualMachineInstance is doing. It contains information available to controllers and users. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


