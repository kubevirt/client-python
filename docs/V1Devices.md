# V1Devices

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**autoattach_graphics_device** | **bool** | Whether to attach the default graphics device or not. VNC will not be available if set to false. Defaults to true. | [optional] 
**autoattach_input_device** | **bool** | Whether to attach an Input Device. Defaults to false. | [optional] 
**autoattach_mem_balloon** | **bool** | Whether to attach the Memory balloon device with default period. Period can be adjusted in virt-config. Defaults to true. | [optional] 
**autoattach_pod_interface** | **bool** | Whether to attach a pod network interface. Defaults to true. | [optional] 
**autoattach_serial_console** | **bool** | Whether to attach the default virtio-serial console or not. Serial console access will not be available if set to false. Defaults to true. | [optional] 
**autoattach_vsock** | **bool** | Whether to attach the VSOCK CID to the VM or not. VSOCK access will be available if set to true. Defaults to false. | [optional] 
**block_multi_queue** | **bool** | Whether or not to enable virtio multi-queue for block devices. Defaults to false. | [optional] 
**client_passthrough** | [**V1ClientPassthroughDevices**](V1ClientPassthroughDevices.md) | To configure and access client devices such as redirecting USB | [optional] 
**disable_hotplug** | **bool** | DisableHotplug disabled the ability to hotplug disks. | [optional] 
**disks** | [**list[V1Disk]**](V1Disk.md) | Disks describes disks, cdroms and luns which are connected to the vmi. | [optional] 
**downward_metrics** | [**V1DownwardMetrics**](V1DownwardMetrics.md) | DownwardMetrics creates a virtio serials for exposing the downward metrics to the vmi. | [optional] 
**filesystems** | [**list[V1Filesystem]**](V1Filesystem.md) | Filesystems describes filesystem which is connected to the vmi. | [optional] 
**gpus** | [**list[V1GPU]**](V1GPU.md) | Whether to attach a GPU device to the vmi. | [optional] 
**host_devices** | [**list[V1HostDevice]**](V1HostDevice.md) | Whether to attach a host device to the vmi. | [optional] 
**inputs** | [**list[V1Input]**](V1Input.md) | Inputs describe input devices | [optional] 
**interfaces** | [**list[V1Interface]**](V1Interface.md) | Interfaces describe network interfaces which are added to the vmi. | [optional] 
**log_serial_console** | **bool** | Whether to log the auto-attached default serial console or not. Serial console logs will be collect to a file and then streamed from a named &#x60;guest-console-log&#x60;. Not relevant if autoattachSerialConsole is disabled. Defaults to cluster wide setting on VirtualMachineOptions. | [optional] 
**network_interface_multiqueue** | **bool** | If specified, virtual network interfaces configured with a virtio bus will also enable the vhost multiqueue feature for network devices. The number of queues created depends on additional factors of the VirtualMachineInstance, like the number of guest CPUs. | [optional] 
**panic_devices** | [**list[V1PanicDevice]**](V1PanicDevice.md) | PanicDevices provides additional crash information when a guest crashes. | [optional] 
**rng** | [**V1Rng**](V1Rng.md) | Whether to have random number generator from host | [optional] 
**sound** | [**V1SoundDevice**](V1SoundDevice.md) | Whether to emulate a sound device. | [optional] 
**tpm** | [**V1TPMDevice**](V1TPMDevice.md) | Whether to emulate a TPM device. | [optional] 
**use_virtio_transitional** | **bool** | Fall back to legacy virtio 0.9 support if virtio bus is selected on devices. This is helpful for old machines like CentOS6 or RHEL6 which do not understand virtio_non_transitional (virtio 1.0). | [optional] 
**video** | [**V1VideoDevice**](V1VideoDevice.md) | Video describes the video device configuration for the vmi. | [optional] 
**watchdog** | [**V1Watchdog**](V1Watchdog.md) | Watchdog describes a watchdog device which can be added to the vmi. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


