# V1KubeVirtConfiguration

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**additional_guest_memory_overhead_ratio** | **str** | AdditionalGuestMemoryOverheadRatio can be used to increase the virtualization infrastructure overhead. This is useful, since the calculation of this overhead is not accurate and cannot be entirely known in advance. The ratio that is being set determines by which factor to increase the overhead calculated by Kubevirt. A higher ratio means that the VMs would be less compromised by node pressures, but would mean that fewer VMs could be scheduled to a node. If not set, the default is 1. | [optional] 
**api_configuration** | [**V1ReloadableComponentConfiguration**](V1ReloadableComponentConfiguration.md) |  | [optional] 
**architecture_configuration** | [**V1ArchConfiguration**](V1ArchConfiguration.md) |  | [optional] 
**auto_cpu_limit_namespace_label_selector** | [**K8sIoApimachineryPkgApisMetaV1LabelSelector**](K8sIoApimachineryPkgApisMetaV1LabelSelector.md) | When set, AutoCPULimitNamespaceLabelSelector will set a CPU limit on virt-launcher for VMIs running inside namespaces that match the label selector. The CPU limit will equal the number of requested vCPUs. This setting does not apply to VMIs with dedicated CPUs. | [optional] 
**changed_block_tracking_label_selectors** | [**V1ChangedBlockTrackingSelectors**](V1ChangedBlockTrackingSelectors.md) | ChangedBlockTrackingLabelSelectors defines label selectors. VMs matching these selectors will have changed block tracking enabled. Enabling changedBlockTracking is mandatory for performing storage-agnostic backups and incremental backups. | [optional] 
**common_instancetypes_deployment** | [**V1CommonInstancetypesDeployment**](V1CommonInstancetypesDeployment.md) | CommonInstancetypesDeployment controls the deployment of common-instancetypes resources | [optional] 
**controller_configuration** | [**V1ReloadableComponentConfiguration**](V1ReloadableComponentConfiguration.md) |  | [optional] 
**cpu_model** | **str** |  | [optional] 
**cpu_request** | [**K8sIoApimachineryPkgApiResourceQuantity**](K8sIoApimachineryPkgApiResourceQuantity.md) |  | [optional] 
**default_runtime_class** | **str** |  | [optional] 
**developer_configuration** | [**V1DeveloperConfiguration**](V1DeveloperConfiguration.md) |  | [optional] 
**emulated_machines** | **list[str]** | Deprecated. Use architectureConfiguration instead. | [optional] 
**eviction_strategy** | **str** | EvictionStrategy defines at the cluster level if the VirtualMachineInstance should be migrated instead of shut-off in case of a node drain. If the VirtualMachineInstance specific field is set it overrides the cluster level one. | [optional] 
**handler_configuration** | [**V1ReloadableComponentConfiguration**](V1ReloadableComponentConfiguration.md) |  | [optional] 
**image_pull_policy** | **str** | Possible enum values:  - &#x60;\&quot;Always\&quot;&#x60; means that kubelet always attempts to pull the latest image. Container will fail If the pull fails.  - &#x60;\&quot;IfNotPresent\&quot;&#x60; means that kubelet pulls if the image isn&#39;t present on disk. Container will fail if the image isn&#39;t present and the pull fails.  - &#x60;\&quot;Never\&quot;&#x60; means that kubelet never pulls an image, but only uses a local image. Container will fail if the image isn&#39;t present | [optional] 
**instancetype** | [**V1InstancetypeConfiguration**](V1InstancetypeConfiguration.md) | Instancetype configuration | [optional] 
**ksm_configuration** | [**V1KSMConfiguration**](V1KSMConfiguration.md) | KSMConfiguration holds the information regarding the enabling the KSM in the nodes (if available). | [optional] 
**live_update_configuration** | [**V1LiveUpdateConfiguration**](V1LiveUpdateConfiguration.md) | LiveUpdateConfiguration holds defaults for live update features | [optional] 
**machine_type** | **str** | Deprecated. Use architectureConfiguration instead. | [optional] 
**mediated_devices_configuration** | [**V1MediatedDevicesConfiguration**](V1MediatedDevicesConfiguration.md) |  | [optional] 
**mem_balloon_stats_period** | **int** |  | [optional] 
**migrations** | [**V1MigrationConfiguration**](V1MigrationConfiguration.md) |  | [optional] 
**min_cpu_model** | **str** | deprecated | [optional] 
**network** | [**V1NetworkConfiguration**](V1NetworkConfiguration.md) |  | [optional] 
**obsolete_cpu_models** | **dict(str, bool)** |  | [optional] 
**ovmf_path** | **str** | Deprecated. Use architectureConfiguration instead. | [optional] 
**permitted_host_devices** | [**V1PermittedHostDevices**](V1PermittedHostDevices.md) |  | [optional] 
**seccomp_configuration** | [**V1SeccompConfiguration**](V1SeccompConfiguration.md) |  | [optional] 
**selinux_launcher_type** | **str** |  | [optional] 
**smbios** | [**V1SMBiosConfiguration**](V1SMBiosConfiguration.md) |  | [optional] 
**support_container_resources** | [**list[V1SupportContainerResources]**](V1SupportContainerResources.md) | SupportContainerResources specifies the resource requirements for various types of supporting containers such as container disks/virtiofs/sidecars and hotplug attachment pods. If omitted a sensible default will be supplied. | [optional] 
**supported_guest_agent_versions** | **list[str]** | deprecated | [optional] 
**tls_configuration** | [**V1TLSConfiguration**](V1TLSConfiguration.md) |  | [optional] 
**virtual_machine_instances_per_node** | **int** |  | [optional] 
**virtual_machine_options** | [**V1VirtualMachineOptions**](V1VirtualMachineOptions.md) |  | [optional] 
**vm_rollout_strategy** | **str** | VMRolloutStrategy defines how live-updatable fields, like CPU sockets, memory, tolerations, and affinity, are propagated from a VM to its VMI. | [optional] 
**vm_state_storage_class** | **str** | VMStateStorageClass is the name of the storage class to use for the PVCs created to preserve VM state, like TPM. | [optional] 
**webhook_configuration** | [**V1ReloadableComponentConfiguration**](V1ReloadableComponentConfiguration.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


