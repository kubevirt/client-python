# V1PortRange

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**end** | **int** | Last port of the range to expose for the virtual machine. This must be a valid port number, 0 &lt; x &lt; 65536. Must be greater than or equal to start. | [default to 0]
**protocol** | **str** | Required. Must be UDP or TCP. | [default to '']
**start** | **int** | First port of the range to expose for the virtual machine. This must be a valid port number, 0 &lt; x &lt; 65536. | [default to 0]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


