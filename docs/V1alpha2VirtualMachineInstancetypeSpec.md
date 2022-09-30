# V1alpha2VirtualMachineInstancetypeSpec

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cpu** | [**V1alpha2CPUInstancetype**](V1alpha2CPUInstancetype.md) | Required CPU related attributes of the instancetype. | 
**gpus** | [**list[V1GPU]**](V1GPU.md) | Optionally defines any GPU devices associated with the instancetype. | [optional] 
**host_devices** | [**list[V1HostDevice]**](V1HostDevice.md) | Optionally defines any HostDevices associated with the instancetype. | [optional] 
**io_threads_policy** | **str** | Optionally defines the IOThreadsPolicy to be used by the instancetype. | [optional] 
**launch_security** | [**V1LaunchSecurity**](V1LaunchSecurity.md) | Optionally defines the LaunchSecurity to be used by the instancetype. | [optional] 
**memory** | [**V1alpha2MemoryInstancetype**](V1alpha2MemoryInstancetype.md) | Required Memory related attributes of the instancetype. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


