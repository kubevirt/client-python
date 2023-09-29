# V1LiveUpdateFeatures

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**affinity** | [**V1LiveUpdateAffinity**](V1LiveUpdateAffinity.md) | Affinity allows live updating the virtual machines node affinity | [optional] 
**cpu** | [**V1LiveUpdateCPU**](V1LiveUpdateCPU.md) | LiveUpdateCPU holds hotplug configuration for the CPU resource. Empty struct indicates that default will be used for maxSockets. Default is specified on cluster level. Absence of the struct means opt-out from CPU hotplug functionality. | [optional] 
**memory** | [**V1LiveUpdateMemory**](V1LiveUpdateMemory.md) | MemoryLiveUpdateConfiguration defines the live update memory features for the VirtualMachine | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


