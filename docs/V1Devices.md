# V1Devices

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**autoattach_graphics_device** | **bool** | Whether to attach the default graphics device or not. VNC will not be available if set to false. Defaults to true. | [optional] 
**autoattach_pod_interface** | **bool** | Whether to attach a pod network interface. Defaults to true. | [optional] 
**autoattach_serial_console** | **bool** | Whether to attach the default serial console or not. Serial console access will not be available if set to false. Defaults to true. | [optional] 
**block_multi_queue** | **bool** | Whether or not to enable virtio multi-queue for block devices +optional | [optional] 
**disks** | [**list[V1Disk]**](V1Disk.md) | Disks describes disks, cdroms, floppy and luns which are connected to the vmi. | [optional] 
**gpus** | [**list[V1GPU]**](V1GPU.md) | Whether to attach a GPU device to the vmi. +optional | [optional] 
**inputs** | [**list[V1Input]**](V1Input.md) | Inputs describe input devices | [optional] 
**interfaces** | [**list[V1Interface]**](V1Interface.md) | Interfaces describe network interfaces which are added to the vmi. | [optional] 
**network_interface_multiqueue** | **bool** | If specified, virtual network interfaces configured with a virtio bus will also enable the vhost multiqueue feature +optional | [optional] 
**rng** | [**V1Rng**](V1Rng.md) | Whether to have random number generator from host +optional | [optional] 
**watchdog** | [**V1Watchdog**](V1Watchdog.md) | Watchdog describes a watchdog device which can be added to the vmi. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


