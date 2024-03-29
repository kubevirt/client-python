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


class V1DomainMemoryDumpInfo(object):
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
        'claim_name': 'str',
        'end_timestamp': 'K8sIoApimachineryPkgApisMetaV1Time',
        'start_timestamp': 'K8sIoApimachineryPkgApisMetaV1Time',
        'target_file_name': 'str'
    }

    attribute_map = {
        'claim_name': 'claimName',
        'end_timestamp': 'endTimestamp',
        'start_timestamp': 'startTimestamp',
        'target_file_name': 'targetFileName'
    }

    def __init__(self, claim_name=None, end_timestamp=None, start_timestamp=None, target_file_name=None):
        """
        V1DomainMemoryDumpInfo - a model defined in Swagger
        """

        self._claim_name = None
        self._end_timestamp = None
        self._start_timestamp = None
        self._target_file_name = None

        if claim_name is not None:
          self.claim_name = claim_name
        if end_timestamp is not None:
          self.end_timestamp = end_timestamp
        if start_timestamp is not None:
          self.start_timestamp = start_timestamp
        if target_file_name is not None:
          self.target_file_name = target_file_name

    @property
    def claim_name(self):
        """
        Gets the claim_name of this V1DomainMemoryDumpInfo.
        ClaimName is the name of the pvc the memory was dumped to

        :return: The claim_name of this V1DomainMemoryDumpInfo.
        :rtype: str
        """
        return self._claim_name

    @claim_name.setter
    def claim_name(self, claim_name):
        """
        Sets the claim_name of this V1DomainMemoryDumpInfo.
        ClaimName is the name of the pvc the memory was dumped to

        :param claim_name: The claim_name of this V1DomainMemoryDumpInfo.
        :type: str
        """

        self._claim_name = claim_name

    @property
    def end_timestamp(self):
        """
        Gets the end_timestamp of this V1DomainMemoryDumpInfo.
        EndTimestamp is the time when the memory dump completed

        :return: The end_timestamp of this V1DomainMemoryDumpInfo.
        :rtype: K8sIoApimachineryPkgApisMetaV1Time
        """
        return self._end_timestamp

    @end_timestamp.setter
    def end_timestamp(self, end_timestamp):
        """
        Sets the end_timestamp of this V1DomainMemoryDumpInfo.
        EndTimestamp is the time when the memory dump completed

        :param end_timestamp: The end_timestamp of this V1DomainMemoryDumpInfo.
        :type: K8sIoApimachineryPkgApisMetaV1Time
        """

        self._end_timestamp = end_timestamp

    @property
    def start_timestamp(self):
        """
        Gets the start_timestamp of this V1DomainMemoryDumpInfo.
        StartTimestamp is the time when the memory dump started

        :return: The start_timestamp of this V1DomainMemoryDumpInfo.
        :rtype: K8sIoApimachineryPkgApisMetaV1Time
        """
        return self._start_timestamp

    @start_timestamp.setter
    def start_timestamp(self, start_timestamp):
        """
        Sets the start_timestamp of this V1DomainMemoryDumpInfo.
        StartTimestamp is the time when the memory dump started

        :param start_timestamp: The start_timestamp of this V1DomainMemoryDumpInfo.
        :type: K8sIoApimachineryPkgApisMetaV1Time
        """

        self._start_timestamp = start_timestamp

    @property
    def target_file_name(self):
        """
        Gets the target_file_name of this V1DomainMemoryDumpInfo.
        TargetFileName is the name of the memory dump output

        :return: The target_file_name of this V1DomainMemoryDumpInfo.
        :rtype: str
        """
        return self._target_file_name

    @target_file_name.setter
    def target_file_name(self, target_file_name):
        """
        Sets the target_file_name of this V1DomainMemoryDumpInfo.
        TargetFileName is the name of the memory dump output

        :param target_file_name: The target_file_name of this V1DomainMemoryDumpInfo.
        :type: str
        """

        self._target_file_name = target_file_name

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
        if not isinstance(other, V1DomainMemoryDumpInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
