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


class V1StorageMigratedVolumeInfo(object):
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
        'destination_pvc_info': 'V1PersistentVolumeClaimInfo',
        'source_pvc_info': 'V1PersistentVolumeClaimInfo',
        'volume_name': 'str'
    }

    attribute_map = {
        'destination_pvc_info': 'destinationPVCInfo',
        'source_pvc_info': 'sourcePVCInfo',
        'volume_name': 'volumeName'
    }

    def __init__(self, destination_pvc_info=None, source_pvc_info=None, volume_name=''):
        """
        V1StorageMigratedVolumeInfo - a model defined in Swagger
        """

        self._destination_pvc_info = None
        self._source_pvc_info = None
        self._volume_name = None

        if destination_pvc_info is not None:
          self.destination_pvc_info = destination_pvc_info
        if source_pvc_info is not None:
          self.source_pvc_info = source_pvc_info
        self.volume_name = volume_name

    @property
    def destination_pvc_info(self):
        """
        Gets the destination_pvc_info of this V1StorageMigratedVolumeInfo.
        DestinationPVCInfo contains the information about the destination PVC

        :return: The destination_pvc_info of this V1StorageMigratedVolumeInfo.
        :rtype: V1PersistentVolumeClaimInfo
        """
        return self._destination_pvc_info

    @destination_pvc_info.setter
    def destination_pvc_info(self, destination_pvc_info):
        """
        Sets the destination_pvc_info of this V1StorageMigratedVolumeInfo.
        DestinationPVCInfo contains the information about the destination PVC

        :param destination_pvc_info: The destination_pvc_info of this V1StorageMigratedVolumeInfo.
        :type: V1PersistentVolumeClaimInfo
        """

        self._destination_pvc_info = destination_pvc_info

    @property
    def source_pvc_info(self):
        """
        Gets the source_pvc_info of this V1StorageMigratedVolumeInfo.
        SourcePVCInfo contains the information about the source PVC

        :return: The source_pvc_info of this V1StorageMigratedVolumeInfo.
        :rtype: V1PersistentVolumeClaimInfo
        """
        return self._source_pvc_info

    @source_pvc_info.setter
    def source_pvc_info(self, source_pvc_info):
        """
        Sets the source_pvc_info of this V1StorageMigratedVolumeInfo.
        SourcePVCInfo contains the information about the source PVC

        :param source_pvc_info: The source_pvc_info of this V1StorageMigratedVolumeInfo.
        :type: V1PersistentVolumeClaimInfo
        """

        self._source_pvc_info = source_pvc_info

    @property
    def volume_name(self):
        """
        Gets the volume_name of this V1StorageMigratedVolumeInfo.
        VolumeName is the name of the volume that is being migrated

        :return: The volume_name of this V1StorageMigratedVolumeInfo.
        :rtype: str
        """
        return self._volume_name

    @volume_name.setter
    def volume_name(self, volume_name):
        """
        Sets the volume_name of this V1StorageMigratedVolumeInfo.
        VolumeName is the name of the volume that is being migrated

        :param volume_name: The volume_name of this V1StorageMigratedVolumeInfo.
        :type: str
        """
        if volume_name is None:
            raise ValueError("Invalid value for `volume_name`, must not be `None`")

        self._volume_name = volume_name

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
        if not isinstance(other, V1StorageMigratedVolumeInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
