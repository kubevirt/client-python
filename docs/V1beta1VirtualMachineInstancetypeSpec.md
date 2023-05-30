# V1beta1VirtualMachineInstancetypeSpec

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cpu** | [**V1beta1CPUInstancetype**](V1beta1CPUInstancetype.md) | Required CPU related attributes of the instancetype. | 
**gpus** | [**list[V1GPU]**](V1GPU.md) | Optionally defines any GPU devices associated with the instancetype. | [optional] 
**host_devices** | [**list[V1HostDevice]**](V1HostDevice.md) | Optionally defines any HostDevices associated with the instancetype. | [optional] 
**io_threads_policy** | **str** | Optionally defines the IOThreadsPolicy to be used by the instancetype. | [optional] 
**launch_security** | [**V1LaunchSecurity**](V1LaunchSecurity.md) | Optionally defines the LaunchSecurity to be used by the instancetype. | [optional] 
**memory** | [**V1beta1MemoryInstancetype**](V1beta1MemoryInstancetype.md) | Required Memory related attributes of the instancetype. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


