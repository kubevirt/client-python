# V1beta1CPUInstancetype

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dedicated_cpu_placement** | **bool** | DedicatedCPUPlacement requests the scheduler to place the VirtualMachineInstance on a node with enough dedicated pCPUs and pin the vCPUs to it. | [optional] 
**guest** | **int** | Required number of vCPUs to expose to the guest.  The resulting CPU topology being derived from the optional PreferredCPUTopology attribute of CPUPreferences that itself defaults to PreferSockets. | [default to 0]
**isolate_emulator_thread** | **bool** | IsolateEmulatorThread requests one more dedicated pCPU to be allocated for the VMI to place the emulator thread on it. | [optional] 
**model** | **str** | Model specifies the CPU model inside the VMI. List of available models https://github.com/libvirt/libvirt/tree/master/src/cpu_map. It is possible to specify special cases like \&quot;host-passthrough\&quot; to get the same CPU as the node and \&quot;host-model\&quot; to get CPU closest to the node one. Defaults to host-model. | [optional] 
**numa** | [**V1NUMA**](V1NUMA.md) | NUMA allows specifying settings for the guest NUMA topology | [optional] 
**realtime** | [**V1Realtime**](V1Realtime.md) | Realtime instructs the virt-launcher to tune the VMI for lower latency, optional for real time workloads | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


