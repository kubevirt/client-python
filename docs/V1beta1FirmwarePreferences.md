# V1beta1FirmwarePreferences

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**preferred_efi** | [**V1EFI**](V1EFI.md) | PreferredEfi optionally enables EFI | [optional] 
**preferred_use_bios** | **bool** | PreferredUseBios optionally enables BIOS | [optional] 
**preferred_use_bios_serial** | **bool** | PreferredUseBiosSerial optionally transmitts BIOS output over the serial.  Requires PreferredUseBios to be enabled. | [optional] 
**preferred_use_efi** | **bool** | PreferredUseEfi optionally enables EFI | [optional] 
**preferred_use_secure_boot** | **bool** | PreferredUseSecureBoot optionally enables SecureBoot and the OVMF roms will be swapped for SecureBoot-enabled ones.  Requires PreferredUseEfi and PreferredSmm to be enabled. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


