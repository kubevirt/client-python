# V1KernelBootContainer

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**image** | **str** | Image that container initrd / kernel files. | 
**image_pull_policy** | **str** | Image pull policy. One of Always, Never, IfNotPresent. Defaults to Always if :latest tag is specified, or IfNotPresent otherwise. Cannot be updated. More info: https://kubernetes.io/docs/concepts/containers/images#updating-images | [optional] 
**image_pull_secret** | **str** | ImagePullSecret is the name of the Docker registry secret required to pull the image. The secret must already exist. | [optional] 
**initrd_path** | **str** | the fully-qualified path to the ramdisk image in the host OS | [optional] 
**kernel_path** | **str** | The fully-qualified path to the kernel image in the host OS | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


