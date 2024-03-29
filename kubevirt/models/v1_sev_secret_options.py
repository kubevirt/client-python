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


class V1SEVSecretOptions(object):
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
        'header': 'str',
        'secret': 'str'
    }

    attribute_map = {
        'header': 'header',
        'secret': 'secret'
    }

    def __init__(self, header=None, secret=None):
        """
        V1SEVSecretOptions - a model defined in Swagger
        """

        self._header = None
        self._secret = None

        if header is not None:
          self.header = header
        if secret is not None:
          self.secret = secret

    @property
    def header(self):
        """
        Gets the header of this V1SEVSecretOptions.
        Base64 encoded header needed to decrypt the secret.

        :return: The header of this V1SEVSecretOptions.
        :rtype: str
        """
        return self._header

    @header.setter
    def header(self, header):
        """
        Sets the header of this V1SEVSecretOptions.
        Base64 encoded header needed to decrypt the secret.

        :param header: The header of this V1SEVSecretOptions.
        :type: str
        """

        self._header = header

    @property
    def secret(self):
        """
        Gets the secret of this V1SEVSecretOptions.
        Base64 encoded encrypted launch secret.

        :return: The secret of this V1SEVSecretOptions.
        :rtype: str
        """
        return self._secret

    @secret.setter
    def secret(self, secret):
        """
        Sets the secret of this V1SEVSecretOptions.
        Base64 encoded encrypted launch secret.

        :param secret: The secret of this V1SEVSecretOptions.
        :type: str
        """

        self._secret = secret

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
        if not isinstance(other, V1SEVSecretOptions):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
