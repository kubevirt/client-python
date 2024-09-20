# V1LiveUpdateConfiguration

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**max_cpu_sockets** | **int** | MaxCpuSockets provides a MaxSockets value for VMs that do not provide their own. For VMs with more sockets than maximum the MaxSockets will be set to equal number of sockets. | [optional] 
**max_guest** | [**K8sIoApimachineryPkgApiResourceQuantity**](K8sIoApimachineryPkgApiResourceQuantity.md) | MaxGuest defines the maximum amount memory that can be allocated to the guest using hotplug. | [optional] 
**max_hotplug_ratio** | **int** | MaxHotplugRatio is the ratio used to define the max amount of a hotplug resource that can be made available to a VM when the specific Max* setting is not defined (MaxCpuSockets, MaxGuest) Example: VM is configured with 512Mi of guest memory, if MaxGuest is not defined and MaxHotplugRatio is 2 then MaxGuest &#x3D; 1Gi defaults to 4 | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


