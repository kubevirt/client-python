# V1MigrationSpec

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**selector** | [**V1VMSelector**](V1VMSelector.md) | Criterias for selecting the VM to migrate. For example selector:   name: testvm will select the VM &#x60;testvm&#x60; for migration |
**node_selector** | **object** | Criteria to use when selecting the destination for the migration for example, to select by the hostname, specify &#x60;kubernetes.io/hostname: master&#x60; other possible choices include the hardware required to run the vm or or lableing of the nodes to indicate their roles in larger applications. examples: disktype: ssd, randomGenerator: /dev/random, randomGenerator: superfastdevice, app: mysql, licensedForServiceX: true Note that these selectors are additions to the node selectors on the VM itself and they must not exist on the VM. If they are conflicting with the VM, no migration will be started. | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


