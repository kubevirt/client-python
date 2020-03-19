# V1Disk

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**boot_order** | **int** | BootOrder is an integer value &gt; 0, used to determine ordering of boot devices. Lower values take precedence. Each disk or interface that has a boot order must have a unique value. Disks without a boot order are not tried if a disk with a boot order exists. +optional | [optional] 
**cache** | **str** | Cache specifies which kvm disk cache mode should be used. +optional | [optional] 
**cdrom** | [**V1CDRomTarget**](V1CDRomTarget.md) | Attach a volume as a cdrom to the vmi. | [optional] 
**dedicated_io_thread** | **bool** | dedicatedIOThread indicates this disk should have an exclusive IO Thread. Enabling this implies useIOThreads &#x3D; true. Defaults to false. +optional | [optional] 
**disk** | [**V1DiskTarget**](V1DiskTarget.md) | Attach a volume as a disk to the vmi. | [optional] 
**floppy** | [**V1FloppyTarget**](V1FloppyTarget.md) | Attach a volume as a floppy to the vmi. | [optional] 
**lun** | [**V1LunTarget**](V1LunTarget.md) | Attach a volume as a LUN to the vmi. | [optional] 
**name** | **str** | Name is the device name | 
**serial** | **str** | Serial provides the ability to specify a serial number for the disk device. +optional | [optional] 
**tag** | **str** | If specified, disk address and its tag will be provided to the guest via config drive metadata +optional | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


