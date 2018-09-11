# V1Volume

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cloud_init_no_cloud** | [**V1CloudInitNoCloudSource**](V1CloudInitNoCloudSource.md) | CloudInitNoCloud represents a cloud-init NoCloud user-data source. The NoCloud data will be added as a disk to the vmi. A proper cloud-init installation is required inside the guest. More info: http://cloudinit.readthedocs.io/en/latest/topics/datasources/nocloud.html +optional | [optional] 
**config_map** | [**V1ConfigMapVolumeSource**](V1ConfigMapVolumeSource.md) | ConfigMapSource represents a reference to a ConfigMap in the same namespace. More info: https://kubernetes.io/docs/tasks/configure-pod-container/configure-pod-configmap/ +optional | [optional] 
**data_volume** | [**V1DataVolumeSource**](V1DataVolumeSource.md) | DataVolume represents the dynamic creation a PVC for this volume as well as the process of populating that PVC with a disk image. +optional | [optional] 
**empty_disk** | [**V1EmptyDiskSource**](V1EmptyDiskSource.md) | EmptyDisk represents a temporary disk which shares the vmis lifecycle. More info: https://kubevirt.gitbooks.io/user-guide/disks-and-volumes.html +optional | [optional] 
**ephemeral** | [**V1EphemeralVolumeSource**](V1EphemeralVolumeSource.md) | Ephemeral is a special volume source that \&quot;wraps\&quot; specified source and provides copy-on-write image on top of it. +optional | [optional] 
**host_disk** | [**V1HostDisk**](V1HostDisk.md) | HostDisk represents a disk created on the cluster level +optional | [optional] 
**name** | **str** | Volume&#39;s name. Must be a DNS_LABEL and unique within the vmi. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names | 
**persistent_volume_claim** | [**V1PersistentVolumeClaimVolumeSource**](V1PersistentVolumeClaimVolumeSource.md) | PersistentVolumeClaimVolumeSource represents a reference to a PersistentVolumeClaim in the same namespace. Directly attached to the vmi via qemu. More info: https://kubernetes.io/docs/concepts/storage/persistent-volumes#persistentvolumeclaims +optional | [optional] 
**registry_disk** | [**V1RegistryDiskSource**](V1RegistryDiskSource.md) | RegistryDisk references a docker image, embedding a qcow or raw disk. More info: https://kubevirt.gitbooks.io/user-guide/registry-disk.html +optional | [optional] 
**secret** | [**V1SecretVolumeSource**](V1SecretVolumeSource.md) | SecretVolumeSource represents a reference to a secret data in the same namespace. More info: https://kubernetes.io/docs/concepts/configuration/secret/ +optional | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


