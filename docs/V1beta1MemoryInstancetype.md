# V1beta1MemoryInstancetype

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**guest** | [**K8sIoApimachineryPkgApiResourceQuantity**](K8sIoApimachineryPkgApiResourceQuantity.md) | Required amount of memory which is visible inside the guest OS. | 
**hugepages** | [**V1Hugepages**](V1Hugepages.md) | Optionally enables the use of hugepages for the VirtualMachineInstance instead of regular memory. | [optional] 
**max_guest** | [**K8sIoApimachineryPkgApiResourceQuantity**](K8sIoApimachineryPkgApiResourceQuantity.md) | MaxGuest allows to specify the maximum amount of memory which is visible inside the Guest OS. The delta between MaxGuest and Guest is the amount of memory that can be hot(un)plugged. | [optional] 
**overcommit_percent** | **int** | OvercommitPercent is the percentage of the guest memory which will be overcommitted. This means that the VMIs parent pod (virt-launcher) will request less physical memory by a factor specified by the OvercommitPercent. Overcommits can lead to memory exhaustion, which in turn can lead to crashes. Use carefully. Defaults to 0 | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


