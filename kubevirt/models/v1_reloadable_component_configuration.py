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


class V1ReloadableComponentConfiguration(object):
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
        'rest_client': 'V1RESTClientConfiguration'
    }

    attribute_map = {
        'rest_client': 'restClient'
    }

    def __init__(self, rest_client=None):
        """
        V1ReloadableComponentConfiguration - a model defined in Swagger
        """

        self._rest_client = None

        if rest_client is not None:
          self.rest_client = rest_client

    @property
    def rest_client(self):
        """
        Gets the rest_client of this V1ReloadableComponentConfiguration.
        RestClient can be used to tune certain aspects of the k8s client in use.

        :return: The rest_client of this V1ReloadableComponentConfiguration.
        :rtype: V1RESTClientConfiguration
        """
        return self._rest_client

    @rest_client.setter
    def rest_client(self, rest_client):
        """
        Sets the rest_client of this V1ReloadableComponentConfiguration.
        RestClient can be used to tune certain aspects of the k8s client in use.

        :param rest_client: The rest_client of this V1ReloadableComponentConfiguration.
        :type: V1RESTClientConfiguration
        """

        self._rest_client = rest_client

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
        if not isinstance(other, V1ReloadableComponentConfiguration):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
