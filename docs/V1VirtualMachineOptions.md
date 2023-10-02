# V1VirtualMachineOptions

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**disable_free_page_reporting** | [**V1DisableFreePageReporting**](V1DisableFreePageReporting.md) | DisableFreePageReporting disable the free page reporting of memory balloon device https://libvirt.org/formatdomain.html#memory-balloon-device. This will have effect only if AutoattachMemBalloon is not false and the vmi is not requesting any high performance feature (dedicatedCPU/realtime/hugePages), in which free page reporting is always disabled. | [optional] 
**disable_serial_console_log** | [**V1DisableSerialConsoleLog**](V1DisableSerialConsoleLog.md) | DisableSerialConsoleLog disables logging the auto-attached default serial console. If not set, serial console logs will be written to a file and then streamed from a container named &#x60;guest-console-log&#x60;. The value can be individually overridden for each VM, not relevant if AutoattachSerialConsole is disabled. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


