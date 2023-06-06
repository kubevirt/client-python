# V1MigrationConfiguration

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allow_auto_converge** | **bool** | AllowAutoConverge allows the platform to compromise performance/availability of VMIs to guarantee successful VMI live migrations. Defaults to false | [optional] 
**allow_post_copy** | **bool** | AllowPostCopy enables post-copy live migrations. Such migrations allow even the busiest VMIs to successfully live-migrate. However, events like a network failure can cause a VMI crash. If set to true, migrations will still start in pre-copy, but switch to post-copy when CompletionTimeoutPerGiB triggers. Defaults to false | [optional] 
**bandwidth_per_migration** | [**K8sIoApimachineryPkgApiResourceQuantity**](K8sIoApimachineryPkgApiResourceQuantity.md) | BandwidthPerMigration limits the amount of network bandwith live migrations are allowed to use. The value is in quantity per second. Defaults to 0 (no limit) | [optional] 
**completion_timeout_per_gi_b** | **int** | CompletionTimeoutPerGiB is the maximum number of seconds per GiB a migration is allowed to take. If a live-migration takes longer to migrate than this value multiplied by the size of the VMI, the migration will be cancelled, unless AllowPostCopy is true. Defaults to 800 | [optional] 
**disable_tls** | **bool** | When set to true, DisableTLS will disable the additional layer of live migration encryption provided by KubeVirt. This is usually a bad idea. Defaults to false | [optional] 
**match_se_linux_level_on_migration** | **bool** | By default, the SELinux level of target virt-launcher pods is forced to the level of the source virt-launcher. When set to true, MatchSELinuxLevelOnMigration lets the CRI auto-assign a random level to the target. That will ensure the target virt-launcher doesn&#39;t share categories with another pod on the node. However, migrations will fail when using RWX volumes that don&#39;t automatically deal with SELinux levels. | [optional] 
**network** | **str** | Network is the name of the CNI network to use for live migrations. By default, migrations go through the pod network. | [optional] 
**node_drain_taint_key** | **str** | NodeDrainTaintKey defines the taint key that indicates a node should be drained. Note: this option relies on the deprecated node taint feature. Default: kubevirt.io/drain | [optional] 
**parallel_migrations_per_cluster** | **int** | ParallelMigrationsPerCluster is the total number of concurrent live migrations allowed cluster-wide. Defaults to 5 | [optional] 
**parallel_outbound_migrations_per_node** | **int** | ParallelOutboundMigrationsPerNode is the maximum number of concurrent outgoing live migrations allowed per node. Defaults to 2 | [optional] 
**progress_timeout** | **int** | ProgressTimeout is the maximum number of seconds a live migration is allowed to make no progress. Hitting this timeout means a migration transferred 0 data for that many seconds. The migration is then considered stuck and therefore cancelled. Defaults to 150 | [optional] 
**unsafe_migration_override** | **bool** | UnsafeMigrationOverride allows live migrations to occur even if the compatibility check indicates the migration will be unsafe to the guest. Defaults to false | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


