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


class V1RateLimiter(object):
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
        'token_bucket_rate_limiter': 'V1TokenBucketRateLimiter'
    }

    attribute_map = {
        'token_bucket_rate_limiter': 'tokenBucketRateLimiter'
    }

    def __init__(self, token_bucket_rate_limiter=None):
        """
        V1RateLimiter - a model defined in Swagger
        """

        self._token_bucket_rate_limiter = None

        if token_bucket_rate_limiter is not None:
          self.token_bucket_rate_limiter = token_bucket_rate_limiter

    @property
    def token_bucket_rate_limiter(self):
        """
        Gets the token_bucket_rate_limiter of this V1RateLimiter.

        :return: The token_bucket_rate_limiter of this V1RateLimiter.
        :rtype: V1TokenBucketRateLimiter
        """
        return self._token_bucket_rate_limiter

    @token_bucket_rate_limiter.setter
    def token_bucket_rate_limiter(self, token_bucket_rate_limiter):
        """
        Sets the token_bucket_rate_limiter of this V1RateLimiter.

        :param token_bucket_rate_limiter: The token_bucket_rate_limiter of this V1RateLimiter.
        :type: V1TokenBucketRateLimiter
        """

        self._token_bucket_rate_limiter = token_bucket_rate_limiter

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
        if not isinstance(other, V1RateLimiter):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other