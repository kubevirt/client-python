# V1alpha1VirtualMachinePoolAutohealingStrategy

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**min_failing_to_start_duration** | [**K8sIoApimachineryPkgApisMetaV1Duration**](K8sIoApimachineryPkgApisMetaV1Duration.md) | MinFailingToStartDuration is the minimum time a VM must be in a failing status (applies to status conditions like CrashLoopBackOff, Unschedulable) before being replaced. It measures the duration since the VM&#39;s Ready condition transitioned to False. Defaults to 5 minutes | [optional] 
**start_up_failure_threshold** | **int** | StartUpFailureThreshold is the number of consecutive VMI start failures (it tracks the value of Status.StartFailure.ConsecutiveFailCount field) before replacing the VM. Defaults to 3 | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


