# V1Disk

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**boot_order** | **int** | BootOrder is an integer value &gt; 0, used to determine ordering of boot devices. Lower values take precedence. Disks without a boot order are not tried if a disk with a boot order exists. +optional | [optional] 
**cdrom** | [**V1CDRomTarget**](V1CDRomTarget.md) | Attach a volume as a cdrom to the vmi. | [optional] 
**disk** | [**V1DiskTarget**](V1DiskTarget.md) | Attach a volume as a disk to the vmi. | [optional] 
**floppy** | [**V1FloppyTarget**](V1FloppyTarget.md) | Attach a volume as a floppy to the vmi. | [optional] 
**lun** | [**V1LunTarget**](V1LunTarget.md) | Attach a volume as a LUN to the vmi. | [optional] 
**name** | **str** | Name is the device name | 
**volume_name** | **str** | Name of the volume which is referenced. Must match the Name of a Volume. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


