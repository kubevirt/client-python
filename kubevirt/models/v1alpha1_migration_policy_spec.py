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


class V1alpha1MigrationPolicySpec(object):
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
        'selectors': 'V1alpha1Selectors'
    }

    attribute_map = {
        'allow_auto_converge': 'allowAutoConverge',
        'allow_post_copy': 'allowPostCopy',
        'allow_workload_disruption': 'allowWorkloadDisruption',
        'bandwidth_per_migration': 'bandwidthPerMigration',
        'completion_timeout_per_gi_b': 'completionTimeoutPerGiB',
        'selectors': 'selectors'
    }

    def __init__(self, allow_auto_converge=None, allow_post_copy=None, allow_workload_disruption=None, bandwidth_per_migration=None, completion_timeout_per_gi_b=None, selectors=None):
        """
        V1alpha1MigrationPolicySpec - a model defined in Swagger
        """

        self._allow_auto_converge = None
        self._allow_post_copy = None
        self._allow_workload_disruption = None
        self._bandwidth_per_migration = None
        self._completion_timeout_per_gi_b = None
        self._selectors = None

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
        self.selectors = selectors

    @property
    def allow_auto_converge(self):
        """
        Gets the allow_auto_converge of this V1alpha1MigrationPolicySpec.

        :return: The allow_auto_converge of this V1alpha1MigrationPolicySpec.
        :rtype: bool
        """
        return self._allow_auto_converge

    @allow_auto_converge.setter
    def allow_auto_converge(self, allow_auto_converge):
        """
        Sets the allow_auto_converge of this V1alpha1MigrationPolicySpec.

        :param allow_auto_converge: The allow_auto_converge of this V1alpha1MigrationPolicySpec.
        :type: bool
        """

        self._allow_auto_converge = allow_auto_converge

    @property
    def allow_post_copy(self):
        """
        Gets the allow_post_copy of this V1alpha1MigrationPolicySpec.

        :return: The allow_post_copy of this V1alpha1MigrationPolicySpec.
        :rtype: bool
        """
        return self._allow_post_copy

    @allow_post_copy.setter
    def allow_post_copy(self, allow_post_copy):
        """
        Sets the allow_post_copy of this V1alpha1MigrationPolicySpec.

        :param allow_post_copy: The allow_post_copy of this V1alpha1MigrationPolicySpec.
        :type: bool
        """

        self._allow_post_copy = allow_post_copy

    @property
    def allow_workload_disruption(self):
        """
        Gets the allow_workload_disruption of this V1alpha1MigrationPolicySpec.

        :return: The allow_workload_disruption of this V1alpha1MigrationPolicySpec.
        :rtype: bool
        """
        return self._allow_workload_disruption

    @allow_workload_disruption.setter
    def allow_workload_disruption(self, allow_workload_disruption):
        """
        Sets the allow_workload_disruption of this V1alpha1MigrationPolicySpec.

        :param allow_workload_disruption: The allow_workload_disruption of this V1alpha1MigrationPolicySpec.
        :type: bool
        """

        self._allow_workload_disruption = allow_workload_disruption

    @property
    def bandwidth_per_migration(self):
        """
        Gets the bandwidth_per_migration of this V1alpha1MigrationPolicySpec.

        :return: The bandwidth_per_migration of this V1alpha1MigrationPolicySpec.
        :rtype: K8sIoApimachineryPkgApiResourceQuantity
        """
        return self._bandwidth_per_migration

    @bandwidth_per_migration.setter
    def bandwidth_per_migration(self, bandwidth_per_migration):
        """
        Sets the bandwidth_per_migration of this V1alpha1MigrationPolicySpec.

        :param bandwidth_per_migration: The bandwidth_per_migration of this V1alpha1MigrationPolicySpec.
        :type: K8sIoApimachineryPkgApiResourceQuantity
        """

        self._bandwidth_per_migration = bandwidth_per_migration

    @property
    def completion_timeout_per_gi_b(self):
        """
        Gets the completion_timeout_per_gi_b of this V1alpha1MigrationPolicySpec.

        :return: The completion_timeout_per_gi_b of this V1alpha1MigrationPolicySpec.
        :rtype: int
        """
        return self._completion_timeout_per_gi_b

    @completion_timeout_per_gi_b.setter
    def completion_timeout_per_gi_b(self, completion_timeout_per_gi_b):
        """
        Sets the completion_timeout_per_gi_b of this V1alpha1MigrationPolicySpec.

        :param completion_timeout_per_gi_b: The completion_timeout_per_gi_b of this V1alpha1MigrationPolicySpec.
        :type: int
        """

        self._completion_timeout_per_gi_b = completion_timeout_per_gi_b

    @property
    def selectors(self):
        """
        Gets the selectors of this V1alpha1MigrationPolicySpec.

        :return: The selectors of this V1alpha1MigrationPolicySpec.
        :rtype: V1alpha1Selectors
        """
        return self._selectors

    @selectors.setter
    def selectors(self, selectors):
        """
        Sets the selectors of this V1alpha1MigrationPolicySpec.

        :param selectors: The selectors of this V1alpha1MigrationPolicySpec.
        :type: V1alpha1Selectors
        """
        if selectors is None:
            raise ValueError("Invalid value for `selectors`, must not be `None`")

        self._selectors = selectors

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
        if not isinstance(other, V1alpha1MigrationPolicySpec):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
