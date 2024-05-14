# V1beta1SpreadOptions

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**across** | **str** | Across optionally defines how to spread vCPUs across the guest visible topology. Default: SocketsCores | [optional] 
**ratio** | **int** | Ratio optionally defines the ratio to spread vCPUs across the guest visible topology:  CoresThreads        - 1:2   - Controls the ratio of cores to threads. Only a ratio of 2 is currently accepted. SocketsCores        - 1:N   - Controls the ratio of socket to cores. SocketsCoresThreads - 1:N:2 - Controls the ratio of socket to cores. Each core providing 2 threads.  Default: 2 | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


