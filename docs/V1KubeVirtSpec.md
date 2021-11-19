# V1KubeVirtSpec

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**certificate_rotate_strategy** | [**V1KubeVirtCertificateRotateStrategy**](V1KubeVirtCertificateRotateStrategy.md) |  | [optional] 
**configuration** | [**V1KubeVirtConfiguration**](V1KubeVirtConfiguration.md) | holds kubevirt configurations. same as the virt-configMap | [optional] 
**customize_components** | [**V1CustomizeComponents**](V1CustomizeComponents.md) |  | [optional] 
**image_pull_policy** | **str** | The ImagePullPolicy to use. | [optional] 
**image_registry** | **str** | The image registry to pull the container images from Defaults to the same registry the operator&#39;s container image is pulled from. | [optional] 
**image_tag** | **str** | The image tag to use for the continer images installed. Defaults to the same tag as the operator&#39;s container image. | [optional] 
**infra** | [**V1ComponentConfig**](V1ComponentConfig.md) | selectors and tolerations that should apply to KubeVirt infrastructure components | [optional] 
**monitor_account** | **str** | The name of the Prometheus service account that needs read-access to KubeVirt endpoints Defaults to prometheus-k8s | [optional] 
**monitor_namespace** | **str** | The namespace Prometheus is deployed in Defaults to openshift-monitor | [optional] 
**product_component** | **str** | Designate the apps.kubevirt.io/component label for KubeVirt components. Useful if KubeVirt is included as part of a product. If ProductComponent is not specified, the component label default value is kubevirt. | [optional] 
**product_name** | **str** | Designate the apps.kubevirt.io/part-of label for KubeVirt components. Useful if KubeVirt is included as part of a product. If ProductName is not specified, the part-of label will be omitted. | [optional] 
**product_version** | **str** | Designate the apps.kubevirt.io/version label for KubeVirt components. Useful if KubeVirt is included as part of a product. If ProductVersion is not specified, KubeVirt&#39;s version will be used. | [optional] 
**uninstall_strategy** | **str** | Specifies if kubevirt can be deleted if workloads are still present. This is mainly a precaution to avoid accidental data loss | [optional] 
**workload_update_strategy** | [**V1KubeVirtWorkloadUpdateStrategy**](V1KubeVirtWorkloadUpdateStrategy.md) | WorkloadUpdateStrategy defines at the cluster level how to handle automated workload updates | [optional] 
**workloads** | [**V1ComponentConfig**](V1ComponentConfig.md) | selectors and tolerations that should apply to KubeVirt workloads | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


