# V1SSHPublicKeyAccessCredentialPropagationMethod

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**config_drive** | [**V1ConfigDriveSSHPublicKeyAccessCredentialPropagation**](V1ConfigDriveSSHPublicKeyAccessCredentialPropagation.md) | ConfigDrivePropagation means that the ssh public keys are injected into the VM using metadata using the configDrive cloud-init provider | [optional] 
**qemu_guest_agent** | [**V1QemuGuestAgentSSHPublicKeyAccessCredentialPropagation**](V1QemuGuestAgentSSHPublicKeyAccessCredentialPropagation.md) | QemuGuestAgentAccessCredentailPropagation means ssh public keys are dynamically injected into the vm at runtime via the qemu guest agent. This feature requires the qemu guest agent to be running within the guest. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


