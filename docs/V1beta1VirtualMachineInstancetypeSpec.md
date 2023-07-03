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
**node_selector** | **dict(str, str)** | NodeSelector is a selector which must be true for the vmi to fit on a node. Selector which must match a node&#39;s labels for the vmi to be scheduled on that node. More info: https://kubernetes.io/docs/concepts/configuration/assign-pod-node/  NodeSelector is the name of the custom node selector for the instancetype. | [optional] 
**scheduler_name** | **str** | If specified, the VMI will be dispatched by specified scheduler. If not specified, the VMI will be dispatched by default scheduler.  SchedulerName is the name of the custom K8s scheduler for the instancetype. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


