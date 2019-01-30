# V1DomainSpec

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**clock** | [**V1Clock**](V1Clock.md) | Clock sets the clock and timers of the vmi. +optional | [optional] 
**cpu** | [**V1CPU**](V1CPU.md) | CPU allow specified the detailed CPU topology inside the vmi. +optional | [optional] 
**devices** | [**V1Devices**](V1Devices.md) | Devices allows adding disks, network interfaces, ... | 
**features** | [**V1Features**](V1Features.md) | Features like acpi, apic, hyperv, smm. +optional | [optional] 
**firmware** | [**V1Firmware**](V1Firmware.md) | Firmware. +optional | [optional] 
**io_threads_policy** | [**V1IOThreadsPolicy**](V1IOThreadsPolicy.md) | Controls whether or not disks will share IOThreads. Omitting IOThreadsPolicy disables use of IOThreads. One of: shared, auto +optional | [optional] 
**machine** | [**V1Machine**](V1Machine.md) | Machine type. +optional | [optional] 
**memory** | [**V1Memory**](V1Memory.md) | Memory allow specifying the VMI memory features. +optional | [optional] 
**resources** | [**V1ResourceRequirements**](V1ResourceRequirements.md) | Resources describes the Compute Resources required by this vmi. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


