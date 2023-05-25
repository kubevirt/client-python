# V1AddVolumeOptions

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**disk** | [**V1Disk**](V1Disk.md) | Disk represents the hotplug disk that will be plugged into the running VMI | 
**dry_run** | **list[str]** | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed | [optional] 
**name** | **str** | Name represents the name that will be used to map the disk to the corresponding volume. This overrides any name set inside the Disk struct itself. | [default to '']
**volume_source** | [**V1HotplugVolumeSource**](V1HotplugVolumeSource.md) | VolumeSource represents the source of the volume to map to the disk. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


