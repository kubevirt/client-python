# V1VirtualMachineInstanceNetworkInterface

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info_source** | **str** | Specifies the origin of the interface data collected. values: domain, guest-agent, or both | [optional] 
**interface_name** | **str** | The interface name inside the Virtual Machine | [optional] 
**ip_address** | **str** | IP address of a Virtual Machine interface. It is always the first item of IPs | [optional] 
**ip_addresses** | **list[str]** | List of all IP addresses of a Virtual Machine interface | [optional] 
**mac** | **str** | Hardware address of a Virtual Machine interface | [optional] 
**name** | **str** | Name of the interface, corresponds to name of the network assigned to the interface | [optional] 
**pod_config_done** | **bool** | PodConfigDone specifies if the corresponding pod interface is properly configured by CNI | [optional] 
**queue_count** | **int** | Specifies how many queues are allocated by MultiQueue | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


