# coding: utf-8

"""
    KubeVirt API

    This is KubeVirt API an add-on for Kubernetes.

    OpenAPI spec version: 1.0.0
    Contact: kubevirt-dev@googlegroups.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class V1MigrationConfiguration(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """


    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'allow_auto_converge': 'bool',
        'allow_post_copy': 'bool',
        'allow_workload_disruption': 'bool',
        'bandwidth_per_migration': 'K8sIoApimachineryPkgApiResourceQuantity',
        'completion_timeout_per_gi_b': 'int',
        'disable_tls': 'bool',
        'match_se_linux_level_on_migration': 'bool',
        'network': 'str',
        'node_drain_taint_key': 'str',
        'parallel_migrations_per_cluster': 'int',
        'parallel_outbound_migrations_per_node': 'int',
        'progress_timeout': 'int',
        'unsafe_migration_override': 'bool'
    }

    attribute_map = {
        'allow_auto_converge': 'allowAutoConverge',
        'allow_post_copy': 'allowPostCopy',
        'allow_workload_disruption': 'allowWorkloadDisruption',
        'bandwidth_per_migration': 'bandwidthPerMigration',
        'completion_timeout_per_gi_b': 'completionTimeoutPerGiB',
        'disable_tls': 'disableTLS',
        'match_se_linux_level_on_migration': 'matchSELinuxLevelOnMigration',
        'network': 'network',
        'node_drain_taint_key': 'nodeDrainTaintKey',
        'parallel_migrations_per_cluster': 'parallelMigrationsPerCluster',
        'parallel_outbound_migrations_per_node': 'parallelOutboundMigrationsPerNode',
        'progress_timeout': 'progressTimeout',
        'unsafe_migration_override': 'unsafeMigrationOverride'
    }

    def __init__(self, allow_auto_converge=None, allow_post_copy=None, allow_workload_disruption=None, bandwidth_per_migration=None, completion_timeout_per_gi_b=None, disable_tls=None, match_se_linux_level_on_migration=None, network=None, node_drain_taint_key=None, parallel_migrations_per_cluster=None, parallel_outbound_migrations_per_node=None, progress_timeout=None, unsafe_migration_override=None):
        """
        V1MigrationConfiguration - a model defined in Swagger
        """

        self._allow_auto_converge = None
        self._allow_post_copy = None
        self._allow_workload_disruption = None
        self._bandwidth_per_migration = None
        self._completion_timeout_per_gi_b = None
        self._disable_tls = None
        self._match_se_linux_level_on_migration = None
        self._network = None
        self._node_drain_taint_key = None
        self._parallel_migrations_per_cluster = None
        self._parallel_outbound_migrations_per_node = None
        self._progress_timeout = None
        self._unsafe_migration_override = None

        if allow_auto_converge is not None:
          self.allow_auto_converge = allow_auto_converge
        if allow_post_copy is not None:
          self.allow_post_copy = allow_post_copy
        if allow_workload_disruption is not None:
          self.allow_workload_disruption = allow_workload_disruption
        if bandwidth_per_migration is not None:
          self.bandwidth_per_migration = bandwidth_per_migration
        if completion_timeout_per_gi_b is not None:
          self.completion_timeout_per_gi_b = completion_timeout_per_gi_b
        if disable_tls is not None:
          self.disable_tls = disable_tls
        if match_se_linux_level_on_migration is not None:
          self.match_se_linux_level_on_migration = match_se_linux_level_on_migration
        if network is not None:
          self.network = network
        if node_drain_taint_key is not None:
          self.node_drain_taint_key = node_drain_taint_key
        if parallel_migrations_per_cluster is not None:
          self.parallel_migrations_per_cluster = parallel_migrations_per_cluster
        if parallel_outbound_migrations_per_node is not None:
          self.parallel_outbound_migrations_per_node = parallel_outbound_migrations_per_node
        if progress_timeout is not None:
          self.progress_timeout = progress_timeout
        if unsafe_migration_override is not None:
          self.unsafe_migration_override = unsafe_migration_override

    @property
    def allow_auto_converge(self):
        """
        Gets the allow_auto_converge of this V1MigrationConfiguration.
        AllowAutoConverge allows the platform to compromise performance/availability of VMIs to guarantee successful VMI live migrations. Defaults to false

        :return: The allow_auto_converge of this V1MigrationConfiguration.
        :rtype: bool
        """
        return self._allow_auto_converge

    @allow_auto_converge.setter
    def allow_auto_converge(self, allow_auto_converge):
        """
        Sets the allow_auto_converge of this V1MigrationConfiguration.
        AllowAutoConverge allows the platform to compromise performance/availability of VMIs to guarantee successful VMI live migrations. Defaults to false

        :param allow_auto_converge: The allow_auto_converge of this V1MigrationConfiguration.
        :type: bool
        """

        self._allow_auto_converge = allow_auto_converge

    @property
    def allow_post_copy(self):
        """
        Gets the allow_post_copy of this V1MigrationConfiguration.
        AllowPostCopy enables post-copy live migrations. Such migrations allow even the busiest VMIs to successfully live-migrate. However, events like a network failure can cause a VMI crash. If set to true, migrations will still start in pre-copy, but switch to post-copy when CompletionTimeoutPerGiB triggers. Defaults to false

        :return: The allow_post_copy of this V1MigrationConfiguration.
        :rtype: bool
        """
        return self._allow_post_copy

    @allow_post_copy.setter
    def allow_post_copy(self, allow_post_copy):
        """
        Sets the allow_post_copy of this V1MigrationConfiguration.
        AllowPostCopy enables post-copy live migrations. Such migrations allow even the busiest VMIs to successfully live-migrate. However, events like a network failure can cause a VMI crash. If set to true, migrations will still start in pre-copy, but switch to post-copy when CompletionTimeoutPerGiB triggers. Defaults to false

        :param allow_post_copy: The allow_post_copy of this V1MigrationConfiguration.
        :type: bool
        """

        self._allow_post_copy = allow_post_copy

    @property
    def allow_workload_disruption(self):
        """
        Gets the allow_workload_disruption of this V1MigrationConfiguration.
        AllowWorkloadDisruption indicates that the migration shouldn't be canceled after acceptableCompletionTime is exceeded. Instead, if permitted, migration will be switched to post-copy or the VMI will be paused to allow the migration to complete

        :return: The allow_workload_disruption of this V1MigrationConfiguration.
        :rtype: bool
        """
        return self._allow_workload_disruption

    @allow_workload_disruption.setter
    def allow_workload_disruption(self, allow_workload_disruption):
        """
        Sets the allow_workload_disruption of this V1MigrationConfiguration.
        AllowWorkloadDisruption indicates that the migration shouldn't be canceled after acceptableCompletionTime is exceeded. Instead, if permitted, migration will be switched to post-copy or the VMI will be paused to allow the migration to complete

        :param allow_workload_disruption: The allow_workload_disruption of this V1MigrationConfiguration.
        :type: bool
        """

        self._allow_workload_disruption = allow_workload_disruption

    @property
    def bandwidth_per_migration(self):
        """
        Gets the bandwidth_per_migration of this V1MigrationConfiguration.
        BandwidthPerMigration limits the amount of network bandwidth live migrations are allowed to use. The value is in quantity per second. Defaults to 0 (no limit)

        :return: The bandwidth_per_migration of this V1MigrationConfiguration.
        :rtype: K8sIoApimachineryPkgApiResourceQuantity
        """
        return self._bandwidth_per_migration

    @bandwidth_per_migration.setter
    def bandwidth_per_migration(self, bandwidth_per_migration):
        """
        Sets the bandwidth_per_migration of this V1MigrationConfiguration.
        BandwidthPerMigration limits the amount of network bandwidth live migrations are allowed to use. The value is in quantity per second. Defaults to 0 (no limit)

        :param bandwidth_per_migration: The bandwidth_per_migration of this V1MigrationConfiguration.
        :type: K8sIoApimachineryPkgApiResourceQuantity
        """

        self._bandwidth_per_migration = bandwidth_per_migration

    @property
    def completion_timeout_per_gi_b(self):
        """
        Gets the completion_timeout_per_gi_b of this V1MigrationConfiguration.
        CompletionTimeoutPerGiB is the maximum number of seconds per GiB a migration is allowed to take. If the timeout is reached, the migration will be either paused, switched to post-copy or cancelled depending on other settings. Defaults to 150

        :return: The completion_timeout_per_gi_b of this V1MigrationConfiguration.
        :rtype: int
        """
        return self._completion_timeout_per_gi_b

    @completion_timeout_per_gi_b.setter
    def completion_timeout_per_gi_b(self, completion_timeout_per_gi_b):
        """
        Sets the completion_timeout_per_gi_b of this V1MigrationConfiguration.
        CompletionTimeoutPerGiB is the maximum number of seconds per GiB a migration is allowed to take. If the timeout is reached, the migration will be either paused, switched to post-copy or cancelled depending on other settings. Defaults to 150

        :param completion_timeout_per_gi_b: The completion_timeout_per_gi_b of this V1MigrationConfiguration.
        :type: int
        """

        self._completion_timeout_per_gi_b = completion_timeout_per_gi_b

    @property
    def disable_tls(self):
        """
        Gets the disable_tls of this V1MigrationConfiguration.
        When set to true, DisableTLS will disable the additional layer of live migration encryption provided by KubeVirt. This is usually a bad idea. Defaults to false

        :return: The disable_tls of this V1MigrationConfiguration.
        :rtype: bool
        """
        return self._disable_tls

    @disable_tls.setter
    def disable_tls(self, disable_tls):
        """
        Sets the disable_tls of this V1MigrationConfiguration.
        When set to true, DisableTLS will disable the additional layer of live migration encryption provided by KubeVirt. This is usually a bad idea. Defaults to false

        :param disable_tls: The disable_tls of this V1MigrationConfiguration.
        :type: bool
        """

        self._disable_tls = disable_tls

    @property
    def match_se_linux_level_on_migration(self):
        """
        Gets the match_se_linux_level_on_migration of this V1MigrationConfiguration.
        By default, the SELinux level of target virt-launcher pods is forced to the level of the source virt-launcher. When set to true, MatchSELinuxLevelOnMigration lets the CRI auto-assign a random level to the target. That will ensure the target virt-launcher doesn't share categories with another pod on the node. However, migrations will fail when using RWX volumes that don't automatically deal with SELinux levels.

        :return: The match_se_linux_level_on_migration of this V1MigrationConfiguration.
        :rtype: bool
        """
        return self._match_se_linux_level_on_migration

    @match_se_linux_level_on_migration.setter
    def match_se_linux_level_on_migration(self, match_se_linux_level_on_migration):
        """
        Sets the match_se_linux_level_on_migration of this V1MigrationConfiguration.
        By default, the SELinux level of target virt-launcher pods is forced to the level of the source virt-launcher. When set to true, MatchSELinuxLevelOnMigration lets the CRI auto-assign a random level to the target. That will ensure the target virt-launcher doesn't share categories with another pod on the node. However, migrations will fail when using RWX volumes that don't automatically deal with SELinux levels.

        :param match_se_linux_level_on_migration: The match_se_linux_level_on_migration of this V1MigrationConfiguration.
        :type: bool
        """

        self._match_se_linux_level_on_migration = match_se_linux_level_on_migration

    @property
    def network(self):
        """
        Gets the network of this V1MigrationConfiguration.
        Network is the name of the CNI network to use for live migrations. By default, migrations go through the pod network.

        :return: The network of this V1MigrationConfiguration.
        :rtype: str
        """
        return self._network

    @network.setter
    def network(self, network):
        """
        Sets the network of this V1MigrationConfiguration.
        Network is the name of the CNI network to use for live migrations. By default, migrations go through the pod network.

        :param network: The network of this V1MigrationConfiguration.
        :type: str
        """

        self._network = network

    @property
    def node_drain_taint_key(self):
        """
        Gets the node_drain_taint_key of this V1MigrationConfiguration.
        NodeDrainTaintKey defines the taint key that indicates a node should be drained. Note: this option relies on the deprecated node taint feature. Default: kubevirt.io/drain

        :return: The node_drain_taint_key of this V1MigrationConfiguration.
        :rtype: str
        """
        return self._node_drain_taint_key

    @node_drain_taint_key.setter
    def node_drain_taint_key(self, node_drain_taint_key):
        """
        Sets the node_drain_taint_key of this V1MigrationConfiguration.
        NodeDrainTaintKey defines the taint key that indicates a node should be drained. Note: this option relies on the deprecated node taint feature. Default: kubevirt.io/drain

        :param node_drain_taint_key: The node_drain_taint_key of this V1MigrationConfiguration.
        :type: str
        """

        self._node_drain_taint_key = node_drain_taint_key

    @property
    def parallel_migrations_per_cluster(self):
        """
        Gets the parallel_migrations_per_cluster of this V1MigrationConfiguration.
        ParallelMigrationsPerCluster is the total number of concurrent live migrations allowed cluster-wide. Defaults to 5

        :return: The parallel_migrations_per_cluster of this V1MigrationConfiguration.
        :rtype: int
        """
        return self._parallel_migrations_per_cluster

    @parallel_migrations_per_cluster.setter
    def parallel_migrations_per_cluster(self, parallel_migrations_per_cluster):
        """
        Sets the parallel_migrations_per_cluster of this V1MigrationConfiguration.
        ParallelMigrationsPerCluster is the total number of concurrent live migrations allowed cluster-wide. Defaults to 5

        :param parallel_migrations_per_cluster: The parallel_migrations_per_cluster of this V1MigrationConfiguration.
        :type: int
        """

        self._parallel_migrations_per_cluster = parallel_migrations_per_cluster

    @property
    def parallel_outbound_migrations_per_node(self):
        """
        Gets the parallel_outbound_migrations_per_node of this V1MigrationConfiguration.
        ParallelOutboundMigrationsPerNode is the maximum number of concurrent outgoing live migrations allowed per node. Defaults to 2

        :return: The parallel_outbound_migrations_per_node of this V1MigrationConfiguration.
        :rtype: int
        """
        return self._parallel_outbound_migrations_per_node

    @parallel_outbound_migrations_per_node.setter
    def parallel_outbound_migrations_per_node(self, parallel_outbound_migrations_per_node):
        """
        Sets the parallel_outbound_migrations_per_node of this V1MigrationConfiguration.
        ParallelOutboundMigrationsPerNode is the maximum number of concurrent outgoing live migrations allowed per node. Defaults to 2

        :param parallel_outbound_migrations_per_node: The parallel_outbound_migrations_per_node of this V1MigrationConfiguration.
        :type: int
        """

        self._parallel_outbound_migrations_per_node = parallel_outbound_migrations_per_node

    @property
    def progress_timeout(self):
        """
        Gets the progress_timeout of this V1MigrationConfiguration.
        ProgressTimeout is the maximum number of seconds a live migration is allowed to make no progress. Hitting this timeout means a migration transferred 0 data for that many seconds. The migration is then considered stuck and therefore cancelled. Defaults to 150

        :return: The progress_timeout of this V1MigrationConfiguration.
        :rtype: int
        """
        return self._progress_timeout

    @progress_timeout.setter
    def progress_timeout(self, progress_timeout):
        """
        Sets the progress_timeout of this V1MigrationConfiguration.
        ProgressTimeout is the maximum number of seconds a live migration is allowed to make no progress. Hitting this timeout means a migration transferred 0 data for that many seconds. The migration is then considered stuck and therefore cancelled. Defaults to 150

        :param progress_timeout: The progress_timeout of this V1MigrationConfiguration.
        :type: int
        """

        self._progress_timeout = progress_timeout

    @property
    def unsafe_migration_override(self):
        """
        Gets the unsafe_migration_override of this V1MigrationConfiguration.
        UnsafeMigrationOverride allows live migrations to occur even if the compatibility check indicates the migration will be unsafe to the guest. Defaults to false

        :return: The unsafe_migration_override of this V1MigrationConfiguration.
        :rtype: bool
        """
        return self._unsafe_migration_override

    @unsafe_migration_override.setter
    def unsafe_migration_override(self, unsafe_migration_override):
        """
        Sets the unsafe_migration_override of this V1MigrationConfiguration.
        UnsafeMigrationOverride allows live migrations to occur even if the compatibility check indicates the migration will be unsafe to the guest. Defaults to false

        :param unsafe_migration_override: The unsafe_migration_override of this V1MigrationConfiguration.
        :type: bool
        """

        self._unsafe_migration_override = unsafe_migration_override

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, V1MigrationConfiguration):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
