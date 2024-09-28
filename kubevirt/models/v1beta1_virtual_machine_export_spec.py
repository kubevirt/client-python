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


class V1beta1VirtualMachineExportSpec(object):
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
        'source': 'K8sIoApiCoreV1TypedLocalObjectReference',
        'token_secret_ref': 'str',
        'ttl_duration': 'K8sIoApimachineryPkgApisMetaV1Duration'
    }

    attribute_map = {
        'source': 'source',
        'token_secret_ref': 'tokenSecretRef',
        'ttl_duration': 'ttlDuration'
    }

    def __init__(self, source=None, token_secret_ref=None, ttl_duration=None):
        """
        V1beta1VirtualMachineExportSpec - a model defined in Swagger
        """

        self._source = None
        self._token_secret_ref = None
        self._ttl_duration = None

        self.source = source
        if token_secret_ref is not None:
          self.token_secret_ref = token_secret_ref
        if ttl_duration is not None:
          self.ttl_duration = ttl_duration

    @property
    def source(self):
        """
        Gets the source of this V1beta1VirtualMachineExportSpec.

        :return: The source of this V1beta1VirtualMachineExportSpec.
        :rtype: K8sIoApiCoreV1TypedLocalObjectReference
        """
        return self._source

    @source.setter
    def source(self, source):
        """
        Sets the source of this V1beta1VirtualMachineExportSpec.

        :param source: The source of this V1beta1VirtualMachineExportSpec.
        :type: K8sIoApiCoreV1TypedLocalObjectReference
        """
        if source is None:
            raise ValueError("Invalid value for `source`, must not be `None`")

        self._source = source

    @property
    def token_secret_ref(self):
        """
        Gets the token_secret_ref of this V1beta1VirtualMachineExportSpec.
        TokenSecretRef is the name of the custom-defined secret that contains the token used by the export server pod

        :return: The token_secret_ref of this V1beta1VirtualMachineExportSpec.
        :rtype: str
        """
        return self._token_secret_ref

    @token_secret_ref.setter
    def token_secret_ref(self, token_secret_ref):
        """
        Sets the token_secret_ref of this V1beta1VirtualMachineExportSpec.
        TokenSecretRef is the name of the custom-defined secret that contains the token used by the export server pod

        :param token_secret_ref: The token_secret_ref of this V1beta1VirtualMachineExportSpec.
        :type: str
        """

        self._token_secret_ref = token_secret_ref

    @property
    def ttl_duration(self):
        """
        Gets the ttl_duration of this V1beta1VirtualMachineExportSpec.
        ttlDuration limits the lifetime of an export If this field is set, after this duration has passed from counting from CreationTimestamp, the export is eligible to be automatically deleted. If this field is omitted, a reasonable default is applied.

        :return: The ttl_duration of this V1beta1VirtualMachineExportSpec.
        :rtype: K8sIoApimachineryPkgApisMetaV1Duration
        """
        return self._ttl_duration

    @ttl_duration.setter
    def ttl_duration(self, ttl_duration):
        """
        Sets the ttl_duration of this V1beta1VirtualMachineExportSpec.
        ttlDuration limits the lifetime of an export If this field is set, after this duration has passed from counting from CreationTimestamp, the export is eligible to be automatically deleted. If this field is omitted, a reasonable default is applied.

        :param ttl_duration: The ttl_duration of this V1beta1VirtualMachineExportSpec.
        :type: K8sIoApimachineryPkgApisMetaV1Duration
        """

        self._ttl_duration = ttl_duration

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
        if not isinstance(other, V1beta1VirtualMachineExportSpec):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other