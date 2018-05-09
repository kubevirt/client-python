# V1VirtualMachineSpec

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**affinity** | [**V1Affinity**](V1Affinity.md) | If affinity is specifies, obey all the affinity rules | [optional] 
**domain** | [**V1DomainSpec**](V1DomainSpec.md) | Specification of the desired behavior of the VirtualMachine on the host. | 
**hostname** | **str** | Specifies the hostname of the vm If not specified, the hostname will be set to the name of the vm, if dhcp or cloud-init is configured properly. +optional | [optional] 
**node_selector** | **object** | NodeSelector is a selector which must be true for the vm to fit on a node. Selector which must match a node&#39;s labels for the vm to be scheduled on that node. More info: https://kubernetes.io/docs/concepts/configuration/assign-pod-node/ +optional | [optional] 
**subdomain** | **str** | If specified, the fully qualified vm hostname will be \&quot;&lt;hostname&gt;.&lt;subdomain&gt;.&lt;pod namespace&gt;.svc.&lt;cluster domain&gt;\&quot;. If not specified, the vm will not have a domainname at all. The DNS entry will resolve to the vm, no matter if the vm itself can pick up a hostname. +optional | [optional] 
**termination_grace_period_seconds** | **int** | Grace period observed after signalling a VM to stop after which the VM is force terminated. | [optional] 
**volumes** | [**list[V1Volume]**](V1Volume.md) | List of volumes that can be mounted by disks belonging to the vm. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


