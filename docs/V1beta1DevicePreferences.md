# V1beta1DevicePreferences

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**preferred_autoattach_graphics_device** | **bool** | PreferredAutoattachGraphicsDevice optionally defines the preferred value of AutoattachGraphicsDevice | [optional] 
**preferred_autoattach_input_device** | **bool** | PreferredAutoattachInputDevice optionally defines the preferred value of AutoattachInputDevice | [optional] 
**preferred_autoattach_mem_balloon** | **bool** | PreferredAutoattachMemBalloon optionally defines the preferred value of AutoattachMemBalloon | [optional] 
**preferred_autoattach_pod_interface** | **bool** | PreferredAutoattachPodInterface optionally defines the preferred value of AutoattachPodInterface | [optional] 
**preferred_autoattach_serial_console** | **bool** | PreferredAutoattachSerialConsole optionally defines the preferred value of AutoattachSerialConsole | [optional] 
**preferred_block_multi_queue** | **bool** | PreferredBlockMultiQueue optionally enables the vhost multiqueue feature for virtio disks. | [optional] 
**preferred_cdrom_bus** | **str** | PreferredCdromBus optionally defines the preferred bus for Cdrom Disk devices. | [optional] 
**preferred_disable_hotplug** | **bool** | PreferredDisableHotplug optionally defines the preferred value of DisableHotplug | [optional] 
**preferred_disk_block_size** | [**V1BlockSize**](V1BlockSize.md) | PreferredBlockSize optionally defines the block size of Disk devices. | [optional] 
**preferred_disk_bus** | **str** | PreferredDiskBus optionally defines the preferred bus for Disk Disk devices. | [optional] 
**preferred_disk_cache** | **str** | PreferredCache optionally defines the DriverCache to be used by Disk devices. | [optional] 
**preferred_disk_dedicated_io_thread** | **bool** | PreferredDedicatedIoThread optionally enables dedicated IO threads for Disk devices. | [optional] 
**preferred_disk_io** | **str** | PreferredIo optionally defines the QEMU disk IO mode to be used by Disk devices. | [optional] 
**preferred_input_bus** | **str** | PreferredInputBus optionally defines the preferred bus for Input devices. | [optional] 
**preferred_input_type** | **str** | PreferredInputType optionally defines the preferred type for Input devices. | [optional] 
**preferred_interface_masquerade** | [**V1InterfaceMasquerade**](V1InterfaceMasquerade.md) | PreferredInterfaceMasquerade optionally defines the preferred masquerade configuration to use with each network interface. | [optional] 
**preferred_interface_model** | **str** | PreferredInterfaceModel optionally defines the preferred model to be used by Interface devices. | [optional] 
**preferred_lun_bus** | **str** | PreferredLunBus optionally defines the preferred bus for Lun Disk devices. | [optional] 
**preferred_network_interface_multi_queue** | **bool** | PreferredNetworkInterfaceMultiQueue optionally enables the vhost multiqueue feature for virtio interfaces. | [optional] 
**preferred_rng** | [**V1Rng**](V1Rng.md) | PreferredRng optionally defines the preferred rng device to be used. | [optional] 
**preferred_sound_model** | **str** | PreferredSoundModel optionally defines the preferred model for Sound devices. | [optional] 
**preferred_tpm** | [**V1TPMDevice**](V1TPMDevice.md) | PreferredTPM optionally defines the preferred TPM device to be used. | [optional] 
**preferred_use_virtio_transitional** | **bool** | PreferredUseVirtioTransitional optionally defines the preferred value of UseVirtioTransitional | [optional] 
**preferred_virtual_gpu_options** | [**V1VGPUOptions**](V1VGPUOptions.md) | PreferredVirtualGPUOptions optionally defines the preferred value of VirtualGPUOptions | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


