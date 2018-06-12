# V1VirtualMachineInstanceSpec

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**affinity** | [**V1Affinity**](V1Affinity.md) | If affinity is specifies, obey all the affinity rules | [optional] 
**domain** | [**V1DomainSpec**](V1DomainSpec.md) | Specification of the desired behavior of the VirtualMachineInstance on the host. | 
**hostname** | **str** | Specifies the hostname of the vmi If not specified, the hostname will be set to the name of the vmi, if dhcp or cloud-init is configured properly. +optional | [optional] 
**networks** | [**list[V1Network]**](V1Network.md) | List of networks that can be attached to a vm&#39;s virtual interface. | [optional] 
**node_selector** | **object** | NodeSelector is a selector which must be true for the vmi to fit on a node. Selector which must match a node&#39;s labels for the vmi to be scheduled on that node. More info: https://kubernetes.io/docs/concepts/configuration/assign-pod-node/ +optional | [optional] 
**subdomain** | **str** | If specified, the fully qualified vmi hostname will be \&quot;&lt;hostname&gt;.&lt;subdomain&gt;.&lt;pod namespace&gt;.svc.&lt;cluster domain&gt;\&quot;. If not specified, the vmi will not have a domainname at all. The DNS entry will resolve to the vmi, no matter if the vmi itself can pick up a hostname. +optional | [optional] 
**termination_grace_period_seconds** | **int** | Grace period observed after signalling a VirtualMachineInstance to stop after which the VirtualMachineInstance is force terminated. | [optional] 
**volumes** | [**list[V1Volume]**](V1Volume.md) | List of volumes that can be mounted by disks belonging to the vmi. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


