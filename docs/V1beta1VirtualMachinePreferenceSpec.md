# V1beta1VirtualMachinePreferenceSpec

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**annotations** | **dict(str, str)** | Optionally defines preferred Annotations to be applied to the VirtualMachineInstance | [optional] 
**clock** | [**V1beta1ClockPreferences**](V1beta1ClockPreferences.md) | Clock optionally defines preferences associated with the Clock attribute of a VirtualMachineInstance DomainSpec | [optional] 
**cpu** | [**V1beta1CPUPreferences**](V1beta1CPUPreferences.md) | CPU optionally defines preferences associated with the CPU attribute of a VirtualMachineInstance DomainSpec | [optional] 
**devices** | [**V1beta1DevicePreferences**](V1beta1DevicePreferences.md) | Devices optionally defines preferences associated with the Devices attribute of a VirtualMachineInstance DomainSpec | [optional] 
**features** | [**V1beta1FeaturePreferences**](V1beta1FeaturePreferences.md) | Features optionally defines preferences associated with the Features attribute of a VirtualMachineInstance DomainSpec | [optional] 
**firmware** | [**V1beta1FirmwarePreferences**](V1beta1FirmwarePreferences.md) | Firmware optionally defines preferences associated with the Firmware attribute of a VirtualMachineInstance DomainSpec | [optional] 
**machine** | [**V1beta1MachinePreferences**](V1beta1MachinePreferences.md) | Machine optionally defines preferences associated with the Machine attribute of a VirtualMachineInstance DomainSpec | [optional] 
**prefer_spread_socket_to_core_ratio** | **int** | PreferSpreadSocketToCoreRatio defines the ratio to spread vCPUs between cores and sockets, it defaults to 2. | [optional] 
**preferred_architecture** | **str** | PreferredArchitecture defines a prefeerred architecture for the VirtualMachine | [optional] 
**preferred_subdomain** | **str** | Subdomain of the VirtualMachineInstance | [optional] 
**preferred_termination_grace_period_seconds** | **int** | Grace period observed after signalling a VirtualMachineInstance to stop after which the VirtualMachineInstance is force terminated. | [optional] 
**requirements** | [**V1beta1PreferenceRequirements**](V1beta1PreferenceRequirements.md) | Requirements defines the minium amount of instance type defined resources required by a set of preferences | [optional] 
**volumes** | [**V1beta1VolumePreferences**](V1beta1VolumePreferences.md) | Volumes optionally defines preferences associated with the Volumes attribute of a VirtualMachineInstace DomainSpec | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


