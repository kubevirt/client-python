# V1VirtualMachineInstanceStatus

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active_pods** | **dict(str, str)** | ActivePods is a mapping of pod UID to node name. It is possible for multiple pods to be running for a single VMI during migration. | [optional] 
**conditions** | [**list[V1VirtualMachineInstanceCondition]**](V1VirtualMachineInstanceCondition.md) | Conditions are specific points in VirtualMachineInstance&#39;s pod runtime. | [optional] 
**evacuation_node_name** | **str** | EvacuationNodeName is used to track the eviction process of a VMI. It stores the name of the node that we want to evacuate. It is meant to be used by KubeVirt core components only and can&#39;t be set or modified by users. | [optional] 
**fs_freeze_status** | **str** | FSFreezeStatus is the state of the fs of the guest it can be either frozen or thawed | [optional] 
**guest_os_info** | [**V1VirtualMachineInstanceGuestOSInfo**](V1VirtualMachineInstanceGuestOSInfo.md) | Guest OS Information | [optional] 
**interfaces** | [**list[V1VirtualMachineInstanceNetworkInterface]**](V1VirtualMachineInstanceNetworkInterface.md) | Interfaces represent the details of available network interfaces. | [optional] 
**launcher_container_image_version** | **str** | LauncherContainerImageVersion indicates what container image is currently active for the vmi. | [optional] 
**migration_method** | **str** | Represents the method using which the vmi can be migrated: live migration or block migration | [optional] 
**migration_state** | [**V1VirtualMachineInstanceMigrationState**](V1VirtualMachineInstanceMigrationState.md) | Represents the status of a live migration | [optional] 
**node_name** | **str** | NodeName is the name where the VirtualMachineInstance is currently running. | [optional] 
**phase** | **str** | Phase is the status of the VirtualMachineInstance in kubernetes world. It is not the VirtualMachineInstance status, but partially correlates to it. | [optional] 
**phase_transition_timestamps** | [**list[V1VirtualMachineInstancePhaseTransitionTimestamp]**](V1VirtualMachineInstancePhaseTransitionTimestamp.md) | PhaseTransitionTimestamp is the timestamp of when the last phase change occurred | [optional] 
**qos_class** | **str** | The Quality of Service (QOS) classification assigned to the virtual machine instance based on resource requirements See PodQOSClass type for available QOS classes More info: https://git.k8s.io/community/contributors/design-proposals/node/resource-qos.md | [optional] 
**reason** | **str** | A brief CamelCase message indicating details about why the VMI is in this state. e.g. &#39;NodeUnresponsive&#39; | [optional] 
**topology_hints** | [**V1TopologyHints**](V1TopologyHints.md) |  | [optional] 
**virtual_machine_revision_name** | **str** | VirtualMachineRevisionName is used to get the vm revision of the vmi when doing an online vm snapshot | [optional] 
**volume_status** | [**list[V1VolumeStatus]**](V1VolumeStatus.md) | VolumeStatus contains the statuses of all the volumes | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


