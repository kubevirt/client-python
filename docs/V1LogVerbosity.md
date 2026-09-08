# V1LogVerbosity

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**node_verbosity** | **dict(str, int)** | NodeVerbosity represents a map of node names to specific log verbosity levels. Allows overriding verbosity on specific nodes without altering cluster-wide settings. Changes take effect on the fly without triggering a pod restart. | [optional] 
**virt_api** | **int** | VirtAPI specifies the log verbosity level for the virt-api deployment. A higher value increases the amount of logged information. Changes take effect on the fly without triggering a pod restart. Default: 2. Levels up to 9 produce progressively more detailed logs. | [optional] 
**virt_controller** | **int** | VirtController specifies the log verbosity level for the virt-controller deployment. A higher value increases the amount of logged information. Changes take effect on the fly without triggering a pod restart. Default: 2. Levels up to 9 produce progressively more detailed logs. | [optional] 
**virt_handler** | **int** | VirtHandler specifies the log verbosity level for the virt-handler DaemonSet. A higher value increases the amount of logged information. Changes take effect on the fly without triggering a pod restart. Default: 2. Levels up to 9 produce progressively more detailed logs. | [optional] 
**virt_launcher** | **int** | VirtLauncher specifies the log verbosity level for virt-launcher pods managing VMI workloads. A higher value increases the amount of logged information. Changes apply to newly created virt-launcher pods. Existing pods retain their original verbosity. Default: 2. Levels up to 9 produce progressively more detailed logs. | [optional] 
**virt_operator** | **int** | VirtOperator specifies the log verbosity level for the virt-operator deployment. A higher value increases the amount of logged information. Changes take effect on the fly without triggering a pod restart. Default: 2. Levels up to 9 produce progressively more detailed logs. | [optional] 
**virt_synchronization_controller** | **int** | VirtSynchronizationController specifies the log verbosity level for the virt-synchronization-controller component. A higher value increases the amount of logged information. Changes take effect on the fly without triggering a pod restart. Default: 2. Levels up to 9 produce progressively more detailed logs. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


