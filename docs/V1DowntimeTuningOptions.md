# V1DowntimeTuningOptions

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cooldown_seconds** | **int** | CooldownSeconds is the minimum interval in seconds between successive downtime increases. Defaults to 10. | [optional] 
**initial_ms** | **int** | InitialMs is the initial max_downtime value in milliseconds set at the start of migration. Tuning steps increase from this value. Defaults to 150. | [optional] 
**start_after_iteration** | **int** | StartAfterIteration is the memory copy iteration after which downtime tuning begins. Defaults to 3. | [optional] 
**steps** | **int** | Steps is the number of equal increments used to ramp from InitialMs to the cluster-level MaxDowntimeMs. Defaults to 7. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


