# V1alpha1VirtualMachineFlavorSpec

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cpu** | [**V1alpha1CPUFlavor**](V1alpha1CPUFlavor.md) | Required CPU related attributes of the flavor. | 
**gpus** | [**list[V1GPU]**](V1GPU.md) | Optionally defines any GPU devices associated with the flavor. | [optional] 
**host_devices** | [**list[V1HostDevice]**](V1HostDevice.md) | Optionally defines any HostDevices associated with the flavor. | [optional] 
**io_threads_policy** | **str** | Optionally defines the IOThreadsPolicy to be used by the flavor. | [optional] 
**launch_security** | [**V1LaunchSecurity**](V1LaunchSecurity.md) | Optionally defines the LaunchSecurity to be used by the flavor. | [optional] 
**memory** | [**V1alpha1MemoryFlavor**](V1alpha1MemoryFlavor.md) | Required Memory related attributes of the flavor. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


