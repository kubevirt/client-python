# V1KubeVirtConfiguration

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_configuration** | [**V1ReloadableComponentConfiguration**](V1ReloadableComponentConfiguration.md) |  | [optional] 
**controller_configuration** | [**V1ReloadableComponentConfiguration**](V1ReloadableComponentConfiguration.md) |  | [optional] 
**cpu_model** | **str** |  | [optional] 
**cpu_request** | [**K8sIoApimachineryPkgApiResourceQuantity**](K8sIoApimachineryPkgApiResourceQuantity.md) |  | [optional] 
**default_runtime_class** | **str** |  | [optional] 
**developer_configuration** | [**V1DeveloperConfiguration**](V1DeveloperConfiguration.md) |  | [optional] 
**emulated_machines** | **list[str]** |  | [optional] 
**eviction_strategy** | **str** | EvictionStrategy defines at the cluster level if the VirtualMachineInstance should be migrated instead of shut-off in case of a node drain. If the VirtualMachineInstance specific field is set it overrides the cluster level one. | [optional] 
**handler_configuration** | [**V1ReloadableComponentConfiguration**](V1ReloadableComponentConfiguration.md) |  | [optional] 
**image_pull_policy** | **str** |  | [optional] 
**machine_type** | **str** |  | [optional] 
**mediated_devices_configuration** | [**V1MediatedDevicesConfiguration**](V1MediatedDevicesConfiguration.md) |  | [optional] 
**mem_balloon_stats_period** | **int** |  | [optional] 
**migrations** | [**V1MigrationConfiguration**](V1MigrationConfiguration.md) |  | [optional] 
**min_cpu_model** | **str** |  | [optional] 
**network** | [**V1NetworkConfiguration**](V1NetworkConfiguration.md) |  | [optional] 
**obsolete_cpu_models** | **dict(str, bool)** |  | [optional] 
**ovmf_path** | **str** |  | [optional] 
**permitted_host_devices** | [**V1PermittedHostDevices**](V1PermittedHostDevices.md) |  | [optional] 
**seccomp_configuration** | [**V1SeccompConfiguration**](V1SeccompConfiguration.md) |  | [optional] 
**selinux_launcher_type** | **str** |  | [optional] 
**smbios** | [**V1SMBiosConfiguration**](V1SMBiosConfiguration.md) |  | [optional] 
**supported_guest_agent_versions** | **list[str]** | deprecated | [optional] 
**tls_configuration** | [**V1TLSConfiguration**](V1TLSConfiguration.md) |  | [optional] 
**virtual_machine_instances_per_node** | **int** |  | [optional] 
**webhook_configuration** | [**V1ReloadableComponentConfiguration**](V1ReloadableComponentConfiguration.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


