# V1Timer

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hpet** | [**V1HPETTimer**](V1HPETTimer.md) | HPET (High Precision Event Timer) - multiple timers with periodic interrupts. | [optional] 
**hyperv** | [**V1HypervTimer**](V1HypervTimer.md) | Hyperv (Hypervclock) - lets guests read the host’s wall clock time (paravirtualized). For windows guests. | [optional] 
**kvm** | [**V1KVMTimer**](V1KVMTimer.md) | KVM  (KVM clock) - lets guests read the host’s wall clock time (paravirtualized). For linux guests. | [optional] 
**pit** | [**V1PITTimer**](V1PITTimer.md) | PIT (Programmable Interval Timer) - a timer with periodic interrupts. | [optional] 
**rtc** | [**V1RTCTimer**](V1RTCTimer.md) | RTC (Real Time Clock) - a continuously running timer with periodic interrupts. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


