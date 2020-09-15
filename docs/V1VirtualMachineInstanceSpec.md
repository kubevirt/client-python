# V1VirtualMachineInstanceSpec

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**affinity** | [**K8sIoApiCoreV1Affinity**](K8sIoApiCoreV1Affinity.md) | If affinity is specifies, obey all the affinity rules | [optional] 
**dns_config** | [**K8sIoApiCoreV1PodDNSConfig**](K8sIoApiCoreV1PodDNSConfig.md) | Specifies the DNS parameters of a pod. Parameters specified here will be merged to the generated DNS configuration based on DNSPolicy. | [optional] 
**dns_policy** | **str** | Set DNS policy for the pod. Defaults to \&quot;ClusterFirst\&quot;. Valid values are &#39;ClusterFirstWithHostNet&#39;, &#39;ClusterFirst&#39;, &#39;Default&#39; or &#39;None&#39;. DNS parameters given in DNSConfig will be merged with the policy selected with DNSPolicy. To have DNS options set along with hostNetwork, you have to specify DNS policy explicitly to &#39;ClusterFirstWithHostNet&#39;. | [optional] 
**domain** | [**V1DomainSpec**](V1DomainSpec.md) | Specification of the desired behavior of the VirtualMachineInstance on the host. | 
**eviction_strategy** | **str** | EvictionStrategy can be set to \&quot;LiveMigrate\&quot; if the VirtualMachineInstance should be migrated instead of shut-off in case of a node drain. | [optional] 
**hostname** | **str** | Specifies the hostname of the vmi If not specified, the hostname will be set to the name of the vmi, if dhcp or cloud-init is configured properly. | [optional] 
**liveness_probe** | [**V1Probe**](V1Probe.md) | Periodic probe of VirtualMachineInstance liveness. VirtualmachineInstances will be stopped if the probe fails. Cannot be updated. More info: https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle#container-probes | [optional] 
**networks** | [**list[V1Network]**](V1Network.md) | List of networks that can be attached to a vm&#39;s virtual interface. | [optional] 
**node_selector** | **dict(str, str)** | NodeSelector is a selector which must be true for the vmi to fit on a node. Selector which must match a node&#39;s labels for the vmi to be scheduled on that node. More info: https://kubernetes.io/docs/concepts/configuration/assign-pod-node/ | [optional] 
**priority_class_name** | **str** | If specified, indicates the pod&#39;s priority. If not specified, the pod priority will be default or zero if there is no default. | [optional] 
**readiness_probe** | [**V1Probe**](V1Probe.md) | Periodic probe of VirtualMachineInstance service readiness. VirtualmachineInstances will be removed from service endpoints if the probe fails. Cannot be updated. More info: https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle#container-probes | [optional] 
**scheduler_name** | **str** | If specified, the VMI will be dispatched by specified scheduler. If not specified, the VMI will be dispatched by default scheduler. | [optional] 
**subdomain** | **str** | If specified, the fully qualified vmi hostname will be \&quot;&lt;hostname&gt;.&lt;subdomain&gt;.&lt;pod namespace&gt;.svc.&lt;cluster domain&gt;\&quot;. If not specified, the vmi will not have a domainname at all. The DNS entry will resolve to the vmi, no matter if the vmi itself can pick up a hostname. | [optional] 
**termination_grace_period_seconds** | **int** | Grace period observed after signalling a VirtualMachineInstance to stop after which the VirtualMachineInstance is force terminated. | [optional] 
**tolerations** | [**list[K8sIoApiCoreV1Toleration]**](K8sIoApiCoreV1Toleration.md) | If toleration is specified, obey all the toleration rules. | [optional] 
**volumes** | [**list[V1Volume]**](V1Volume.md) | List of volumes that can be mounted by disks belonging to the vmi. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


