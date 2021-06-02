# V1Probe

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**_exec** | [**K8sIoApiCoreV1ExecAction**](K8sIoApiCoreV1ExecAction.md) | One and only one of the following should be specified. Exec specifies the action to take, it will be executed on the guest through the qemu-guest-agent. If the guest agent is not available, this probe will fail. | [optional] 
**failure_threshold** | **int** | Minimum consecutive failures for the probe to be considered failed after having succeeded. Defaults to 3. Minimum value is 1. | [optional] 
**http_get** | [**K8sIoApiCoreV1HTTPGetAction**](K8sIoApiCoreV1HTTPGetAction.md) | HTTPGet specifies the http request to perform. | [optional] 
**initial_delay_seconds** | **int** | Number of seconds after the VirtualMachineInstance has started before liveness probes are initiated. More info: https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle#container-probes | [optional] 
**period_seconds** | **int** | How often (in seconds) to perform the probe. Default to 10 seconds. Minimum value is 1. | [optional] 
**success_threshold** | **int** | Minimum consecutive successes for the probe to be considered successful after having failed. Defaults to 1. Must be 1 for liveness. Minimum value is 1. | [optional] 
**tcp_socket** | [**K8sIoApiCoreV1TCPSocketAction**](K8sIoApiCoreV1TCPSocketAction.md) | TCPSocket specifies an action involving a TCP port. TCP hooks not yet supported | [optional] 
**timeout_seconds** | **int** | Number of seconds after which the probe times out. For exec probes the timeout fails the probe but does not terminate the command running on the guest. This means a blocking command can result in an increasing load on the guest. A small buffer will be added to the resulting workload exec probe to compensate for delays caused by the qemu guest exec mechanism. Defaults to 1 second. Minimum value is 1. More info: https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle#container-probes | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


