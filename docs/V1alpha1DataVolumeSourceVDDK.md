# V1alpha1DataVolumeSourceVDDK

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**backing_file** | **str** | BackingFile is the path to the virtual hard disk to migrate from vCenter/ESXi | [optional] 
**secret_ref** | **str** | SecretRef provides a reference to a secret containing the username and password needed to access the vCenter or ESXi host | [optional] 
**thumbprint** | **str** | Thumbprint is the certificate thumbprint of the vCenter or ESXi host | [optional] 
**url** | **str** | URL is the URL of the vCenter or ESXi host with the VM to migrate | [optional] 
**uuid** | **str** | UUID is the UUID of the virtual machine that the backing file is attached to in vCenter/ESXi | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


