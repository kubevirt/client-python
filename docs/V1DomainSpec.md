# V1DomainSpec

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**chassis** | [**V1Chassis**](V1Chassis.md) | Chassis specifies the chassis info passed to the domain. | [optional] 
**clock** | [**V1Clock**](V1Clock.md) | Clock sets the clock and timers of the vmi. | [optional] 
**cpu** | [**V1CPU**](V1CPU.md) | CPU allow specified the detailed CPU topology inside the vmi. | [optional] 
**devices** | [**V1Devices**](V1Devices.md) | Devices allows adding disks, network interfaces, and others | 
**features** | [**V1Features**](V1Features.md) | Features like acpi, apic, hyperv, smm. | [optional] 
**firmware** | [**V1Firmware**](V1Firmware.md) | Firmware. | [optional] 
**io_threads_policy** | **str** | Controls whether or not disks will share IOThreads. Omitting IOThreadsPolicy disables use of IOThreads. One of: shared, auto | [optional] 
**launch_security** | [**V1LaunchSecurity**](V1LaunchSecurity.md) | Launch Security setting of the vmi. | [optional] 
**machine** | [**V1Machine**](V1Machine.md) | Machine type. | [optional] 
**memory** | [**V1Memory**](V1Memory.md) | Memory allow specifying the VMI memory features. | [optional] 
**resources** | [**V1ResourceRequirements**](V1ResourceRequirements.md) | Resources describes the Compute Resources required by this vmi. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


