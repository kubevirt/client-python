# V1DeveloperConfiguration

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cluster_profiler** | **bool** | Enable the ability to pprof profile KubeVirt control plane | [optional] 
**cpu_allocation_ratio** | **int** | For each requested virtual CPU, CPUAllocationRatio defines how much physical CPU to request per VMI from the hosting node. The value is in fraction of a CPU thread (or core on non-hyperthreaded nodes). For example, a value of 1 means 1 physical CPU thread per VMI CPU thread. A value of 100 would be 1% of a physical thread allocated for each requested VMI thread. This option has no effect on VMIs that request dedicated CPUs. More information at: https://kubevirt.io/user-guide/operations/node_overcommit/#node-cpu-allocation-ratio Defaults to 10 | [optional] 
**disabled_feature_gates** | **list[str]** | DisabledFeatureGates specifies a list of experimental feature gates to disable. A feature gate must not appear in both FeatureGates and DisabledFeatureGates. | [optional] 
**disk_verification** | [**V1DiskVerification**](V1DiskVerification.md) |  | [optional] 
**feature_gates** | **list[str]** | FeatureGates specifies a list of experimental feature gates to enable. Defaults to none. A feature gate must not appear in both FeatureGates and DisabledFeatureGates. | [optional] 
**log_verbosity** | [**V1LogVerbosity**](V1LogVerbosity.md) |  | [optional] 
**memory_overcommit** | **int** | MemoryOvercommit is the percentage of memory we want to give VMIs compared to the amount given to its parent pod (virt-launcher). For example, a value of 102 means the VMI will \&quot;see\&quot; 2% more memory than its parent pod. Values under 100 are effectively \&quot;undercommits\&quot;. Overcommits can lead to memory exhaustion, which in turn can lead to crashes. Use carefully. Defaults to 100 | [optional] 
**minimum_cluster_tsc_frequency** | **int** | Allow overriding the automatically determined minimum TSC frequency of the cluster and fixate the minimum to this frequency. | [optional] 
**minimum_reserve_pvc_bytes** | **int** | MinimumReservePVCBytes is the amount of space, in bytes, to leave unused on disks. Defaults to 131072 (128KiB) | [optional] 
**node_selectors** | **dict(str, str)** | NodeSelectors allows restricting VMI creation to nodes that match a set of labels. Defaults to none | [optional] 
**pvc_tolerate_less_space_up_to_percent** | **int** | LessPVCSpaceToleration determines how much smaller, in percentage, disk PVCs are allowed to be compared to the requested size (to account for various overheads). Defaults to 10 | [optional] 
**use_emulation** | **bool** | UseEmulation can be set to true to allow fallback to software emulation in case hardware-assisted emulation is not available. Defaults to false | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


