# V1ResourceRequirements

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**limits** | **object** | Limits describes the maximum amount of compute resources allowed. Valid resource keys are \&quot;memory\&quot; and \&quot;cpu\&quot;. | [optional] 
**overcommit_guest_overhead** | **bool** | Don&#39;t ask the scheduler to take the guest-management overhead into account. Instead put the overhead only into the container&#39;s memory limit. This can lead to crashes if all memory is in use on a node. Defaults to false. | [optional] 
**requests** | **object** | Requests is a description of the initial vmi resources. Valid resource keys are \&quot;memory\&quot; and \&quot;cpu\&quot;. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


