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


class K8sIoApiCoreV1PersistentVolumeClaimSpec(object):
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
        'access_modes': 'list[str]',
        'data_source': 'K8sIoApiCoreV1TypedLocalObjectReference',
        'data_source_ref': 'K8sIoApiCoreV1TypedObjectReference',
        'resources': 'K8sIoApiCoreV1VolumeResourceRequirements',
        'selector': 'K8sIoApimachineryPkgApisMetaV1LabelSelector',
        'storage_class_name': 'str',
        'volume_attributes_class_name': 'str',
        'volume_mode': 'str',
        'volume_name': 'str'
    }

    attribute_map = {
        'access_modes': 'accessModes',
        'data_source': 'dataSource',
        'data_source_ref': 'dataSourceRef',
        'resources': 'resources',
        'selector': 'selector',
        'storage_class_name': 'storageClassName',
        'volume_attributes_class_name': 'volumeAttributesClassName',
        'volume_mode': 'volumeMode',
        'volume_name': 'volumeName'
    }

    def __init__(self, access_modes=None, data_source=None, data_source_ref=None, resources=None, selector=None, storage_class_name=None, volume_attributes_class_name=None, volume_mode=None, volume_name=None):
        """
        K8sIoApiCoreV1PersistentVolumeClaimSpec - a model defined in Swagger
        """

        self._access_modes = None
        self._data_source = None
        self._data_source_ref = None
        self._resources = None
        self._selector = None
        self._storage_class_name = None
        self._volume_attributes_class_name = None
        self._volume_mode = None
        self._volume_name = None

        if access_modes is not None:
          self.access_modes = access_modes
        if data_source is not None:
          self.data_source = data_source
        if data_source_ref is not None:
          self.data_source_ref = data_source_ref
        if resources is not None:
          self.resources = resources
        if selector is not None:
          self.selector = selector
        if storage_class_name is not None:
          self.storage_class_name = storage_class_name
        if volume_attributes_class_name is not None:
          self.volume_attributes_class_name = volume_attributes_class_name
        if volume_mode is not None:
          self.volume_mode = volume_mode
        if volume_name is not None:
          self.volume_name = volume_name

    @property
    def access_modes(self):
        """
        Gets the access_modes of this K8sIoApiCoreV1PersistentVolumeClaimSpec.
        accessModes contains the desired access modes the volume should have. More info: https://kubernetes.io/docs/concepts/storage/persistent-volumes#access-modes-1

        :return: The access_modes of this K8sIoApiCoreV1PersistentVolumeClaimSpec.
        :rtype: list[str]
        """
        return self._access_modes

    @access_modes.setter
    def access_modes(self, access_modes):
        """
        Sets the access_modes of this K8sIoApiCoreV1PersistentVolumeClaimSpec.
        accessModes contains the desired access modes the volume should have. More info: https://kubernetes.io/docs/concepts/storage/persistent-volumes#access-modes-1

        :param access_modes: The access_modes of this K8sIoApiCoreV1PersistentVolumeClaimSpec.
        :type: list[str]
        """
        allowed_values = ["ReadOnlyMany", "ReadWriteMany", "ReadWriteOnce", "ReadWriteOncePod"]
        if not set(access_modes).issubset(set(allowed_values)):
            raise ValueError(
                "Invalid values for `access_modes` [{0}], must be a subset of [{1}]"
                .format(", ".join(map(str, set(access_modes)-set(allowed_values))),
                        ", ".join(map(str, allowed_values)))
            )

        self._access_modes = access_modes

    @property
    def data_source(self):
        """
        Gets the data_source of this K8sIoApiCoreV1PersistentVolumeClaimSpec.
        dataSource field can be used to specify either: * An existing VolumeSnapshot object (snapshot.storage.k8s.io/VolumeSnapshot) * An existing PVC (PersistentVolumeClaim) If the provisioner or an external controller can support the specified data source, it will create a new volume based on the contents of the specified data source. When the AnyVolumeDataSource feature gate is enabled, dataSource contents will be copied to dataSourceRef, and dataSourceRef contents will be copied to dataSource when dataSourceRef.namespace is not specified. If the namespace is specified, then dataSourceRef will not be copied to dataSource.

        :return: The data_source of this K8sIoApiCoreV1PersistentVolumeClaimSpec.
        :rtype: K8sIoApiCoreV1TypedLocalObjectReference
        """
        return self._data_source

    @data_source.setter
    def data_source(self, data_source):
        """
        Sets the data_source of this K8sIoApiCoreV1PersistentVolumeClaimSpec.
        dataSource field can be used to specify either: * An existing VolumeSnapshot object (snapshot.storage.k8s.io/VolumeSnapshot) * An existing PVC (PersistentVolumeClaim) If the provisioner or an external controller can support the specified data source, it will create a new volume based on the contents of the specified data source. When the AnyVolumeDataSource feature gate is enabled, dataSource contents will be copied to dataSourceRef, and dataSourceRef contents will be copied to dataSource when dataSourceRef.namespace is not specified. If the namespace is specified, then dataSourceRef will not be copied to dataSource.

        :param data_source: The data_source of this K8sIoApiCoreV1PersistentVolumeClaimSpec.
        :type: K8sIoApiCoreV1TypedLocalObjectReference
        """

        self._data_source = data_source

    @property
    def data_source_ref(self):
        """
        Gets the data_source_ref of this K8sIoApiCoreV1PersistentVolumeClaimSpec.
        dataSourceRef specifies the object from which to populate the volume with data, if a non-empty volume is desired. This may be any object from a non-empty API group (non core object) or a PersistentVolumeClaim object. When this field is specified, volume binding will only succeed if the type of the specified object matches some installed volume populator or dynamic provisioner. This field will replace the functionality of the dataSource field and as such if both fields are non-empty, they must have the same value. For backwards compatibility, when namespace isn't specified in dataSourceRef, both fields (dataSource and dataSourceRef) will be set to the same value automatically if one of them is empty and the other is non-empty. When namespace is specified in dataSourceRef, dataSource isn't set to the same value and must be empty. There are three important differences between dataSource and dataSourceRef: * While dataSource only allows two specific types of objects, dataSourceRef   allows any non-core object, as well as PersistentVolumeClaim objects. * While dataSource ignores disallowed values (dropping them), dataSourceRef   preserves all values, and generates an error if a disallowed value is   specified. * While dataSource only allows local objects, dataSourceRef allows objects   in any namespaces. (Beta) Using this field requires the AnyVolumeDataSource feature gate to be enabled. (Alpha) Using the namespace field of dataSourceRef requires the CrossNamespaceVolumeDataSource feature gate to be enabled.

        :return: The data_source_ref of this K8sIoApiCoreV1PersistentVolumeClaimSpec.
        :rtype: K8sIoApiCoreV1TypedObjectReference
        """
        return self._data_source_ref

    @data_source_ref.setter
    def data_source_ref(self, data_source_ref):
        """
        Sets the data_source_ref of this K8sIoApiCoreV1PersistentVolumeClaimSpec.
        dataSourceRef specifies the object from which to populate the volume with data, if a non-empty volume is desired. This may be any object from a non-empty API group (non core object) or a PersistentVolumeClaim object. When this field is specified, volume binding will only succeed if the type of the specified object matches some installed volume populator or dynamic provisioner. This field will replace the functionality of the dataSource field and as such if both fields are non-empty, they must have the same value. For backwards compatibility, when namespace isn't specified in dataSourceRef, both fields (dataSource and dataSourceRef) will be set to the same value automatically if one of them is empty and the other is non-empty. When namespace is specified in dataSourceRef, dataSource isn't set to the same value and must be empty. There are three important differences between dataSource and dataSourceRef: * While dataSource only allows two specific types of objects, dataSourceRef   allows any non-core object, as well as PersistentVolumeClaim objects. * While dataSource ignores disallowed values (dropping them), dataSourceRef   preserves all values, and generates an error if a disallowed value is   specified. * While dataSource only allows local objects, dataSourceRef allows objects   in any namespaces. (Beta) Using this field requires the AnyVolumeDataSource feature gate to be enabled. (Alpha) Using the namespace field of dataSourceRef requires the CrossNamespaceVolumeDataSource feature gate to be enabled.

        :param data_source_ref: The data_source_ref of this K8sIoApiCoreV1PersistentVolumeClaimSpec.
        :type: K8sIoApiCoreV1TypedObjectReference
        """

        self._data_source_ref = data_source_ref

    @property
    def resources(self):
        """
        Gets the resources of this K8sIoApiCoreV1PersistentVolumeClaimSpec.
        resources represents the minimum resources the volume should have. If RecoverVolumeExpansionFailure feature is enabled users are allowed to specify resource requirements that are lower than previous value but must still be higher than capacity recorded in the status field of the claim. More info: https://kubernetes.io/docs/concepts/storage/persistent-volumes#resources

        :return: The resources of this K8sIoApiCoreV1PersistentVolumeClaimSpec.
        :rtype: K8sIoApiCoreV1VolumeResourceRequirements
        """
        return self._resources

    @resources.setter
    def resources(self, resources):
        """
        Sets the resources of this K8sIoApiCoreV1PersistentVolumeClaimSpec.
        resources represents the minimum resources the volume should have. If RecoverVolumeExpansionFailure feature is enabled users are allowed to specify resource requirements that are lower than previous value but must still be higher than capacity recorded in the status field of the claim. More info: https://kubernetes.io/docs/concepts/storage/persistent-volumes#resources

        :param resources: The resources of this K8sIoApiCoreV1PersistentVolumeClaimSpec.
        :type: K8sIoApiCoreV1VolumeResourceRequirements
        """

        self._resources = resources

    @property
    def selector(self):
        """
        Gets the selector of this K8sIoApiCoreV1PersistentVolumeClaimSpec.
        selector is a label query over volumes to consider for binding.

        :return: The selector of this K8sIoApiCoreV1PersistentVolumeClaimSpec.
        :rtype: K8sIoApimachineryPkgApisMetaV1LabelSelector
        """
        return self._selector

    @selector.setter
    def selector(self, selector):
        """
        Sets the selector of this K8sIoApiCoreV1PersistentVolumeClaimSpec.
        selector is a label query over volumes to consider for binding.

        :param selector: The selector of this K8sIoApiCoreV1PersistentVolumeClaimSpec.
        :type: K8sIoApimachineryPkgApisMetaV1LabelSelector
        """

        self._selector = selector

    @property
    def storage_class_name(self):
        """
        Gets the storage_class_name of this K8sIoApiCoreV1PersistentVolumeClaimSpec.
        storageClassName is the name of the StorageClass required by the claim. More info: https://kubernetes.io/docs/concepts/storage/persistent-volumes#class-1

        :return: The storage_class_name of this K8sIoApiCoreV1PersistentVolumeClaimSpec.
        :rtype: str
        """
        return self._storage_class_name

    @storage_class_name.setter
    def storage_class_name(self, storage_class_name):
        """
        Sets the storage_class_name of this K8sIoApiCoreV1PersistentVolumeClaimSpec.
        storageClassName is the name of the StorageClass required by the claim. More info: https://kubernetes.io/docs/concepts/storage/persistent-volumes#class-1

        :param storage_class_name: The storage_class_name of this K8sIoApiCoreV1PersistentVolumeClaimSpec.
        :type: str
        """

        self._storage_class_name = storage_class_name

    @property
    def volume_attributes_class_name(self):
        """
        Gets the volume_attributes_class_name of this K8sIoApiCoreV1PersistentVolumeClaimSpec.
        volumeAttributesClassName may be used to set the VolumeAttributesClass used by this claim. If specified, the CSI driver will create or update the volume with the attributes defined in the corresponding VolumeAttributesClass. This has a different purpose than storageClassName, it can be changed after the claim is created. An empty string value means that no VolumeAttributesClass will be applied to the claim but it's not allowed to reset this field to empty string once it is set. If unspecified and the PersistentVolumeClaim is unbound, the default VolumeAttributesClass will be set by the persistentvolume controller if it exists. If the resource referred to by volumeAttributesClass does not exist, this PersistentVolumeClaim will be set to a Pending state, as reflected by the modifyVolumeStatus field, until such as a resource exists. More info: https://kubernetes.io/docs/concepts/storage/volume-attributes-classes/ (Beta) Using this field requires the VolumeAttributesClass feature gate to be enabled (off by default).

        :return: The volume_attributes_class_name of this K8sIoApiCoreV1PersistentVolumeClaimSpec.
        :rtype: str
        """
        return self._volume_attributes_class_name

    @volume_attributes_class_name.setter
    def volume_attributes_class_name(self, volume_attributes_class_name):
        """
        Sets the volume_attributes_class_name of this K8sIoApiCoreV1PersistentVolumeClaimSpec.
        volumeAttributesClassName may be used to set the VolumeAttributesClass used by this claim. If specified, the CSI driver will create or update the volume with the attributes defined in the corresponding VolumeAttributesClass. This has a different purpose than storageClassName, it can be changed after the claim is created. An empty string value means that no VolumeAttributesClass will be applied to the claim but it's not allowed to reset this field to empty string once it is set. If unspecified and the PersistentVolumeClaim is unbound, the default VolumeAttributesClass will be set by the persistentvolume controller if it exists. If the resource referred to by volumeAttributesClass does not exist, this PersistentVolumeClaim will be set to a Pending state, as reflected by the modifyVolumeStatus field, until such as a resource exists. More info: https://kubernetes.io/docs/concepts/storage/volume-attributes-classes/ (Beta) Using this field requires the VolumeAttributesClass feature gate to be enabled (off by default).

        :param volume_attributes_class_name: The volume_attributes_class_name of this K8sIoApiCoreV1PersistentVolumeClaimSpec.
        :type: str
        """

        self._volume_attributes_class_name = volume_attributes_class_name

    @property
    def volume_mode(self):
        """
        Gets the volume_mode of this K8sIoApiCoreV1PersistentVolumeClaimSpec.
        volumeMode defines what type of volume is required by the claim. Value of Filesystem is implied when not included in claim spec.  Possible enum values:  - `\"Block\"` means the volume will not be formatted with a filesystem and will remain a raw block device.  - `\"Filesystem\"` means the volume will be or is formatted with a filesystem.

        :return: The volume_mode of this K8sIoApiCoreV1PersistentVolumeClaimSpec.
        :rtype: str
        """
        return self._volume_mode

    @volume_mode.setter
    def volume_mode(self, volume_mode):
        """
        Sets the volume_mode of this K8sIoApiCoreV1PersistentVolumeClaimSpec.
        volumeMode defines what type of volume is required by the claim. Value of Filesystem is implied when not included in claim spec.  Possible enum values:  - `\"Block\"` means the volume will not be formatted with a filesystem and will remain a raw block device.  - `\"Filesystem\"` means the volume will be or is formatted with a filesystem.

        :param volume_mode: The volume_mode of this K8sIoApiCoreV1PersistentVolumeClaimSpec.
        :type: str
        """
        allowed_values = ["Block", "Filesystem"]
        if volume_mode not in allowed_values:
            raise ValueError(
                "Invalid value for `volume_mode` ({0}), must be one of {1}"
                .format(volume_mode, allowed_values)
            )

        self._volume_mode = volume_mode

    @property
    def volume_name(self):
        """
        Gets the volume_name of this K8sIoApiCoreV1PersistentVolumeClaimSpec.
        volumeName is the binding reference to the PersistentVolume backing this claim.

        :return: The volume_name of this K8sIoApiCoreV1PersistentVolumeClaimSpec.
        :rtype: str
        """
        return self._volume_name

    @volume_name.setter
    def volume_name(self, volume_name):
        """
        Sets the volume_name of this K8sIoApiCoreV1PersistentVolumeClaimSpec.
        volumeName is the binding reference to the PersistentVolume backing this claim.

        :param volume_name: The volume_name of this K8sIoApiCoreV1PersistentVolumeClaimSpec.
        :type: str
        """

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
        if not isinstance(other, K8sIoApiCoreV1PersistentVolumeClaimSpec):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
