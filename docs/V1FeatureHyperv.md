# V1FeatureHyperv

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**evmcs** | [**V1FeatureState**](V1FeatureState.md) | EVMCS Speeds up L2 vmexits, but disables other virtualization features. Requires vapic. Defaults to the machine type setting. +optional | [optional] 
**frequencies** | [**V1FeatureState**](V1FeatureState.md) | Frequencies improve Hyper-V on KVM (TSC clock source). Defaults to the machine type setting. +optional | [optional] 
**ipi** | [**V1FeatureState**](V1FeatureState.md) | IPI improves performances in overcommited environments. Requires vpindex. Defaults to the machine type setting. +optional | [optional] 
**reenlightenment** | [**V1FeatureState**](V1FeatureState.md) | Reenlightenment improve Hyper-V on KVM (TSC clock source). Defaults to the machine type setting. +optional | [optional] 
**relaxed** | [**V1FeatureState**](V1FeatureState.md) | Relaxed relaxes constraints on timer. Defaults to the machine type setting. +optional | [optional] 
**reset** | [**V1FeatureState**](V1FeatureState.md) | Reset enables Hyperv reboot/reset for the vmi. Requires synic. Defaults to the machine type setting. +optional | [optional] 
**runtime** | [**V1FeatureState**](V1FeatureState.md) | Runtime. Defaults to the machine type setting. +optional | [optional] 
**spinlocks** | [**V1FeatureSpinlocks**](V1FeatureSpinlocks.md) | Spinlocks indicates if spinlocks should be made available to the guest. +optional | [optional] 
**synic** | [**V1FeatureState**](V1FeatureState.md) | SyNIC enable Synthetic Interrupt Controller. Defaults to the machine type setting. +optional | [optional] 
**synictimer** | [**V1FeatureState**](V1FeatureState.md) | SyNICTimer enable Synthetic Interrupt Controller timer. Defaults to the machine type setting. +optional | [optional] 
**tlbflush** | [**V1FeatureState**](V1FeatureState.md) | TLBFlush improves performances in overcommited environments. Requires vpindex. Defaults to the machine type setting. +optional | [optional] 
**vapic** | [**V1FeatureState**](V1FeatureState.md) | VAPIC indicates whether virtual APIC is enabled. Defaults to the machine type setting. +optional | [optional] 
**vendorid** | [**V1FeatureVendorID**](V1FeatureVendorID.md) | VendorID allows setting the hypervisor vendor id. Defaults to the machine type setting. +optional | [optional] 
**vpindex** | [**V1FeatureState**](V1FeatureState.md) | VPIndex enables the Virtual Processor Index to help windows identifying virtual processors. Defaults to the machine type setting. +optional | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


