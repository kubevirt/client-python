# V1FeatureHyperv

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**evmcs** | [**V1FeatureState**](V1FeatureState.md) | EVMCS Speeds up L2 vmexits, but disables other virtualization features. Requires vapic. Defaults to the machine type setting. | [optional] 
**frequencies** | [**V1FeatureState**](V1FeatureState.md) | Frequencies improves the TSC clock source handling for Hyper-V on KVM. Defaults to the machine type setting. | [optional] 
**ipi** | [**V1FeatureState**](V1FeatureState.md) | IPI improves performances in overcommited environments. Requires vpindex. Defaults to the machine type setting. | [optional] 
**reenlightenment** | [**V1FeatureState**](V1FeatureState.md) | Reenlightenment enables the notifications on TSC frequency changes. Defaults to the machine type setting. | [optional] 
**relaxed** | [**V1FeatureState**](V1FeatureState.md) | Relaxed instructs the guest OS to disable watchdog timeouts. Defaults to the machine type setting. | [optional] 
**reset** | [**V1FeatureState**](V1FeatureState.md) | Reset enables Hyperv reboot/reset for the vmi. Requires synic. Defaults to the machine type setting. | [optional] 
**runtime** | [**V1FeatureState**](V1FeatureState.md) | Runtime improves the time accounting to improve scheduling in the guest. Defaults to the machine type setting. | [optional] 
**spinlocks** | [**V1FeatureSpinlocks**](V1FeatureSpinlocks.md) | Spinlocks allows to configure the spinlock retry attempts. | [optional] 
**synic** | [**V1FeatureState**](V1FeatureState.md) | SyNIC enables the Synthetic Interrupt Controller. Defaults to the machine type setting. | [optional] 
**synictimer** | [**V1SyNICTimer**](V1SyNICTimer.md) | SyNICTimer enables Synthetic Interrupt Controller Timers, reducing CPU load. Defaults to the machine type setting. | [optional] 
**tlbflush** | [**V1TLBFlush**](V1TLBFlush.md) | TLBFlush improves performances in overcommited environments. Requires vpindex. Defaults to the machine type setting. | [optional] 
**vapic** | [**V1FeatureState**](V1FeatureState.md) | VAPIC improves the paravirtualized handling of interrupts. Defaults to the machine type setting. | [optional] 
**vendorid** | [**V1FeatureVendorID**](V1FeatureVendorID.md) | VendorID allows setting the hypervisor vendor id. Defaults to the machine type setting. | [optional] 
**vpindex** | [**V1FeatureState**](V1FeatureState.md) | VPIndex enables the Virtual Processor Index to help windows identifying virtual processors. Defaults to the machine type setting. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


