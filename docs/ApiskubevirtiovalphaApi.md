# swagger_client.ApiskubevirtiovalphaApi

All URIs are relative to *http://localhost:8183/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**console**](ApiskubevirtiovalphaApi.md#console) | **GET** /apis/kubevirt.io/v1alpha1/namespaces/{namespace:[a-z0-9][a-z0-9\-]*}/virtualmachines/{name:[a-z0-9][a-z0-9\-]*}/console | Open a websocket connection to a serial console on the specified VM.
[**func1**](ApiskubevirtiovalphaApi.md#func1) | **GET** /apis/kubevirt.io/v1alpha1 |
[**func1_0**](ApiskubevirtiovalphaApi.md#func1_0) | **GET** /apis/kubevirt.io/v1alpha1/migrations | test4
[**func1_1**](ApiskubevirtiovalphaApi.md#func1_1) | **GET** /apis/kubevirt.io/v1alpha1/namespaces/{namespace:[a-z0-9][a-z0-9\-]*}/migrations |
[**func1_10**](ApiskubevirtiovalphaApi.md#func1_10) | **DELETE** /apis/kubevirt.io/v1alpha1/namespaces/{namespace:[a-z0-9][a-z0-9\-]*}/virtualmachines |
[**func1_11**](ApiskubevirtiovalphaApi.md#func1_11) | **GET** /apis/kubevirt.io/v1alpha1/namespaces/{namespace:[a-z0-9][a-z0-9\-]*}/virtualmachines/{name:[a-z0-9][a-z0-9\-]*} | test4
[**func1_12**](ApiskubevirtiovalphaApi.md#func1_12) | **PUT** /apis/kubevirt.io/v1alpha1/namespaces/{namespace:[a-z0-9][a-z0-9\-]*}/virtualmachines/{name:[a-z0-9][a-z0-9\-]*} | test2
[**func1_13**](ApiskubevirtiovalphaApi.md#func1_13) | **DELETE** /apis/kubevirt.io/v1alpha1/namespaces/{namespace:[a-z0-9][a-z0-9\-]*}/virtualmachines/{name:[a-z0-9][a-z0-9\-]*} | test3
[**func1_14**](ApiskubevirtiovalphaApi.md#func1_14) | **PATCH** /apis/kubevirt.io/v1alpha1/namespaces/{namespace:[a-z0-9][a-z0-9\-]*}/virtualmachines/{name:[a-z0-9][a-z0-9\-]*} | test5
[**func1_15**](ApiskubevirtiovalphaApi.md#func1_15) | **GET** /apis/kubevirt.io/v1alpha1/namespaces/{namespace:[a-z0-9][a-z0-9\-]*}/virtualmachines/{name:[a-z0-9][a-z0-9\-]*}/spice | Returns a remote-viewer configuration file. Run &#x60;man 1 remote-viewer&#x60; to learn more about the configuration format.
[**func1_16**](ApiskubevirtiovalphaApi.md#func1_16) | **GET** /apis/kubevirt.io/v1alpha1/virtualmachines | test4
[**func1_2**](ApiskubevirtiovalphaApi.md#func1_2) | **POST** /apis/kubevirt.io/v1alpha1/namespaces/{namespace:[a-z0-9][a-z0-9\-]*}/migrations |
[**func1_3**](ApiskubevirtiovalphaApi.md#func1_3) | **DELETE** /apis/kubevirt.io/v1alpha1/namespaces/{namespace:[a-z0-9][a-z0-9\-]*}/migrations |
[**func1_4**](ApiskubevirtiovalphaApi.md#func1_4) | **GET** /apis/kubevirt.io/v1alpha1/namespaces/{namespace:[a-z0-9][a-z0-9\-]*}/migrations/{name:[a-z0-9][a-z0-9\-]*} | test4
[**func1_5**](ApiskubevirtiovalphaApi.md#func1_5) | **PUT** /apis/kubevirt.io/v1alpha1/namespaces/{namespace:[a-z0-9][a-z0-9\-]*}/migrations/{name:[a-z0-9][a-z0-9\-]*} | test2
[**func1_6**](ApiskubevirtiovalphaApi.md#func1_6) | **DELETE** /apis/kubevirt.io/v1alpha1/namespaces/{namespace:[a-z0-9][a-z0-9\-]*}/migrations/{name:[a-z0-9][a-z0-9\-]*} | test3
[**func1_7**](ApiskubevirtiovalphaApi.md#func1_7) | **PATCH** /apis/kubevirt.io/v1alpha1/namespaces/{namespace:[a-z0-9][a-z0-9\-]*}/migrations/{name:[a-z0-9][a-z0-9\-]*} | test5
[**func1_8**](ApiskubevirtiovalphaApi.md#func1_8) | **GET** /apis/kubevirt.io/v1alpha1/namespaces/{namespace:[a-z0-9][a-z0-9\-]*}/virtualmachines |
[**func1_9**](ApiskubevirtiovalphaApi.md#func1_9) | **POST** /apis/kubevirt.io/v1alpha1/namespaces/{namespace:[a-z0-9][a-z0-9\-]*}/virtualmachines |
[**kube_connection_healthz_func**](ApiskubevirtiovalphaApi.md#kube_connection_healthz_func) | **GET** /apis/kubevirt.io/v1alpha1/healthz | Health endpoint
[**not_implemented_yet**](ApiskubevirtiovalphaApi.md#not_implemented_yet) | **GET** /apis/kubevirt.io/v1alpha1/watch/migrations |
[**not_implemented_yet_0**](ApiskubevirtiovalphaApi.md#not_implemented_yet_0) | **GET** /apis/kubevirt.io/v1alpha1/watch/namespaces/{namespace:[a-z0-9][a-z0-9\-]*}/migrations |
[**not_implemented_yet_1**](ApiskubevirtiovalphaApi.md#not_implemented_yet_1) | **GET** /apis/kubevirt.io/v1alpha1/watch/namespaces/{namespace:[a-z0-9][a-z0-9\-]*}/virtualmachines |
[**not_implemented_yet_2**](ApiskubevirtiovalphaApi.md#not_implemented_yet_2) | **GET** /apis/kubevirt.io/v1alpha1/watch/virtualmachines |


# **console**
> console(namespace, name, console=console)

Open a websocket connection to a serial console on the specified VM.

### Example
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ApiskubevirtiovalphaApi()
namespace = 'namespace_example' # str | Object name and auth scope, such as for teams and projects
name = 'name_example' # str | Name of the resource
console = 'console_example' # str | Name of the serial console to connect to (optional)

try:
    # Open a websocket connection to a serial console on the specified VM.
    api_instance.console(namespace, name, console=console)
except ApiException as e:
    print "Exception when calling ApiskubevirtiovalphaApi->console: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**| Object name and auth scope, such as for teams and projects |
 **name** | **str**| Name of the resource |
 **console** | **str**| Name of the serial console to connect to | [optional]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **func1**
> V1APIResourceList func1()



### Example
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ApiskubevirtiovalphaApi()

try:
    api_response = api_instance.func1()
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApiskubevirtiovalphaApi->func1: %s\n" % e
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**V1APIResourceList**](V1APIResourceList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **func1_0**
> V1MigrationList func1_0(field_selector=field_selector, label_selector=label_selector, resource_version=resource_version, timeout_seconds=timeout_seconds)

test4

### Example
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ApiskubevirtiovalphaApi()
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = swagger_client.Object() # Object | TimeoutSeconds for the list/watch call. (optional)

try:
    # test4
    api_response = api_instance.func1_0(field_selector=field_selector, label_selector=label_selector, resource_version=resource_version, timeout_seconds=timeout_seconds)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApiskubevirtiovalphaApi->func1_0: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **field_selector** | **str**| A selector to restrict the list of returned objects by their fields. Defaults to everything. | [optional]
 **label_selector** | **str**| A selector to restrict the list of returned objects by their labels. Defaults to everything | [optional]
 **resource_version** | **str**| When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. | [optional]
 **timeout_seconds** | [**Object**](.md)| TimeoutSeconds for the list/watch call. | [optional]

### Return type

[**V1MigrationList**](V1MigrationList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **func1_1**
> V1MigrationList func1_1(namespace, field_selector=field_selector, label_selector=label_selector, resource_version=resource_version, timeout_seconds=timeout_seconds)



### Example
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ApiskubevirtiovalphaApi()
namespace = 'namespace_example' # str | Object name and auth scope, such as for teams and projects
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = swagger_client.Object() # Object | TimeoutSeconds for the list/watch call. (optional)

try:
    api_response = api_instance.func1_1(namespace, field_selector=field_selector, label_selector=label_selector, resource_version=resource_version, timeout_seconds=timeout_seconds)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApiskubevirtiovalphaApi->func1_1: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**| Object name and auth scope, such as for teams and projects |
 **field_selector** | **str**| A selector to restrict the list of returned objects by their fields. Defaults to everything. | [optional]
 **label_selector** | **str**| A selector to restrict the list of returned objects by their labels. Defaults to everything | [optional]
 **resource_version** | **str**| When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. | [optional]
 **timeout_seconds** | [**Object**](.md)| TimeoutSeconds for the list/watch call. | [optional]

### Return type

[**V1MigrationList**](V1MigrationList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **func1_10**
> V1VirtualMachineList func1_10(name, field_selector=field_selector, label_selector=label_selector)



### Example
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ApiskubevirtiovalphaApi()
name = 'name_example' # str | Name of the resource
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything (optional)

try:
    api_response = api_instance.func1_10(name, field_selector=field_selector, label_selector=label_selector)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApiskubevirtiovalphaApi->func1_10: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the resource |
 **field_selector** | **str**| A selector to restrict the list of returned objects by their fields. Defaults to everything. | [optional]
 **label_selector** | **str**| A selector to restrict the list of returned objects by their labels. Defaults to everything | [optional]

### Return type

[**V1VirtualMachineList**](V1VirtualMachineList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **func1_11**
> V1VirtualMachine func1_11(namespace, name, export=export, exact=exact)

test4

### Example
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ApiskubevirtiovalphaApi()
namespace = 'namespace_example' # str | Object name and auth scope, such as for teams and projects
name = 'name_example' # str | Name of the resource
export = true # bool | Should this value be exported. Export strips fields that a user can not specify. (optional)
exact = true # bool | Should the export be exact. Exact export maintains cluster-specific fields like 'Namespace' (optional)

try:
    # test4
    api_response = api_instance.func1_11(namespace, name, export=export, exact=exact)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApiskubevirtiovalphaApi->func1_11: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**| Object name and auth scope, such as for teams and projects |
 **name** | **str**| Name of the resource |
 **export** | **bool**| Should this value be exported. Export strips fields that a user can not specify. | [optional]
 **exact** | **bool**| Should the export be exact. Exact export maintains cluster-specific fields like &#39;Namespace&#39; | [optional]

### Return type

[**V1VirtualMachine**](V1VirtualMachine.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **func1_12**
> V1VirtualMachine func1_12(body, namespace, name)

test2

### Example
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ApiskubevirtiovalphaApi()
body = swagger_client.V1VirtualMachine() # V1VirtualMachine |
namespace = 'namespace_example' # str | Object name and auth scope, such as for teams and projects
name = 'name_example' # str | Name of the resource

try:
    # test2
    api_response = api_instance.func1_12(body, namespace, name)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApiskubevirtiovalphaApi->func1_12: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1VirtualMachine**](V1VirtualMachine.md)|  |
 **namespace** | **str**| Object name and auth scope, such as for teams and projects |
 **name** | **str**| Name of the resource |

### Return type

[**V1VirtualMachine**](V1VirtualMachine.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/yaml
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **func1_13**
> V1Status func1_13(namespace, name)

test3

### Example
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ApiskubevirtiovalphaApi()
namespace = 'namespace_example' # str | Object name and auth scope, such as for teams and projects
name = 'name_example' # str | Name of the resource

try:
    # test3
    api_response = api_instance.func1_13(namespace, name)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApiskubevirtiovalphaApi->func1_13: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**| Object name and auth scope, such as for teams and projects |
 **name** | **str**| Name of the resource |

### Return type

[**V1Status**](V1Status.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/yaml
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **func1_14**
> V1VirtualMachine func1_14()

test5

### Example
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ApiskubevirtiovalphaApi()

try:
    # test5
    api_response = api_instance.func1_14()
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApiskubevirtiovalphaApi->func1_14: %s\n" % e
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**V1VirtualMachine**](V1VirtualMachine.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json-patch+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **func1_15**
> func1_15(namespace, name)

Returns a remote-viewer configuration file. Run `man 1 remote-viewer` to learn more about the configuration format.

### Example
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ApiskubevirtiovalphaApi()
namespace = 'namespace_example' # str | Object name and auth scope, such as for teams and projects
name = 'name_example' # str | Name of the resource

try:
    # Returns a remote-viewer configuration file. Run `man 1 remote-viewer` to learn more about the configuration format.
    api_instance.func1_15(namespace, name)
except ApiException as e:
    print "Exception when calling ApiskubevirtiovalphaApi->func1_15: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**| Object name and auth scope, such as for teams and projects |
 **name** | **str**| Name of the resource |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **func1_16**
> V1VirtualMachineList func1_16(field_selector=field_selector, label_selector=label_selector, resource_version=resource_version, timeout_seconds=timeout_seconds)

test4

### Example
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ApiskubevirtiovalphaApi()
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = swagger_client.Object() # Object | TimeoutSeconds for the list/watch call. (optional)

try:
    # test4
    api_response = api_instance.func1_16(field_selector=field_selector, label_selector=label_selector, resource_version=resource_version, timeout_seconds=timeout_seconds)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApiskubevirtiovalphaApi->func1_16: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **field_selector** | **str**| A selector to restrict the list of returned objects by their fields. Defaults to everything. | [optional]
 **label_selector** | **str**| A selector to restrict the list of returned objects by their labels. Defaults to everything | [optional]
 **resource_version** | **str**| When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. | [optional]
 **timeout_seconds** | [**Object**](.md)| TimeoutSeconds for the list/watch call. | [optional]

### Return type

[**V1VirtualMachineList**](V1VirtualMachineList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **func1_2**
> V1Migration func1_2(body, namespace)



### Example
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ApiskubevirtiovalphaApi()
body = swagger_client.V1Migration() # V1Migration |
namespace = 'namespace_example' # str | Object name and auth scope, such as for teams and projects

try:
    api_response = api_instance.func1_2(body, namespace)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApiskubevirtiovalphaApi->func1_2: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1Migration**](V1Migration.md)|  |
 **namespace** | **str**| Object name and auth scope, such as for teams and projects |

### Return type

[**V1Migration**](V1Migration.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/yaml
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **func1_3**
> V1MigrationList func1_3(name, field_selector=field_selector, label_selector=label_selector)



### Example
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ApiskubevirtiovalphaApi()
name = 'name_example' # str | Name of the resource
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything (optional)

try:
    api_response = api_instance.func1_3(name, field_selector=field_selector, label_selector=label_selector)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApiskubevirtiovalphaApi->func1_3: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the resource |
 **field_selector** | **str**| A selector to restrict the list of returned objects by their fields. Defaults to everything. | [optional]
 **label_selector** | **str**| A selector to restrict the list of returned objects by their labels. Defaults to everything | [optional]

### Return type

[**V1MigrationList**](V1MigrationList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **func1_4**
> V1Migration func1_4(namespace, name, export=export, exact=exact)

test4

### Example
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ApiskubevirtiovalphaApi()
namespace = 'namespace_example' # str | Object name and auth scope, such as for teams and projects
name = 'name_example' # str | Name of the resource
export = true # bool | Should this value be exported. Export strips fields that a user can not specify. (optional)
exact = true # bool | Should the export be exact. Exact export maintains cluster-specific fields like 'Namespace' (optional)

try:
    # test4
    api_response = api_instance.func1_4(namespace, name, export=export, exact=exact)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApiskubevirtiovalphaApi->func1_4: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**| Object name and auth scope, such as for teams and projects |
 **name** | **str**| Name of the resource |
 **export** | **bool**| Should this value be exported. Export strips fields that a user can not specify. | [optional]
 **exact** | **bool**| Should the export be exact. Exact export maintains cluster-specific fields like &#39;Namespace&#39; | [optional]

### Return type

[**V1Migration**](V1Migration.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **func1_5**
> V1Migration func1_5(body, namespace, name)

test2

### Example
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ApiskubevirtiovalphaApi()
body = swagger_client.V1Migration() # V1Migration |
namespace = 'namespace_example' # str | Object name and auth scope, such as for teams and projects
name = 'name_example' # str | Name of the resource

try:
    # test2
    api_response = api_instance.func1_5(body, namespace, name)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApiskubevirtiovalphaApi->func1_5: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1Migration**](V1Migration.md)|  |
 **namespace** | **str**| Object name and auth scope, such as for teams and projects |
 **name** | **str**| Name of the resource |

### Return type

[**V1Migration**](V1Migration.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/yaml
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **func1_6**
> V1Status func1_6(namespace, name)

test3

### Example
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ApiskubevirtiovalphaApi()
namespace = 'namespace_example' # str | Object name and auth scope, such as for teams and projects
name = 'name_example' # str | Name of the resource

try:
    # test3
    api_response = api_instance.func1_6(namespace, name)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApiskubevirtiovalphaApi->func1_6: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**| Object name and auth scope, such as for teams and projects |
 **name** | **str**| Name of the resource |

### Return type

[**V1Status**](V1Status.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/yaml
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **func1_7**
> V1Migration func1_7()

test5

### Example
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ApiskubevirtiovalphaApi()

try:
    # test5
    api_response = api_instance.func1_7()
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApiskubevirtiovalphaApi->func1_7: %s\n" % e
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**V1Migration**](V1Migration.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json-patch+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **func1_8**
> V1VirtualMachineList func1_8(namespace, field_selector=field_selector, label_selector=label_selector, resource_version=resource_version, timeout_seconds=timeout_seconds)



### Example
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ApiskubevirtiovalphaApi()
namespace = 'namespace_example' # str | Object name and auth scope, such as for teams and projects
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = swagger_client.Object() # Object | TimeoutSeconds for the list/watch call. (optional)

try:
    api_response = api_instance.func1_8(namespace, field_selector=field_selector, label_selector=label_selector, resource_version=resource_version, timeout_seconds=timeout_seconds)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApiskubevirtiovalphaApi->func1_8: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**| Object name and auth scope, such as for teams and projects |
 **field_selector** | **str**| A selector to restrict the list of returned objects by their fields. Defaults to everything. | [optional]
 **label_selector** | **str**| A selector to restrict the list of returned objects by their labels. Defaults to everything | [optional]
 **resource_version** | **str**| When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. | [optional]
 **timeout_seconds** | [**Object**](.md)| TimeoutSeconds for the list/watch call. | [optional]

### Return type

[**V1VirtualMachineList**](V1VirtualMachineList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **func1_9**
> V1VirtualMachine func1_9(body, namespace)



### Example
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ApiskubevirtiovalphaApi()
body = swagger_client.V1VirtualMachine() # V1VirtualMachine |
namespace = 'namespace_example' # str | Object name and auth scope, such as for teams and projects

try:
    api_response = api_instance.func1_9(body, namespace)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApiskubevirtiovalphaApi->func1_9: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1VirtualMachine**](V1VirtualMachine.md)|  |
 **namespace** | **str**| Object name and auth scope, such as for teams and projects |

### Return type

[**V1VirtualMachine**](V1VirtualMachine.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/yaml
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **kube_connection_healthz_func**
> kube_connection_healthz_func()

Health endpoint

### Example
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ApiskubevirtiovalphaApi()

try:
    # Health endpoint
    api_instance.kube_connection_healthz_func()
except ApiException as e:
    print "Exception when calling ApiskubevirtiovalphaApi->kube_connection_healthz_func: %s\n" % e
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **not_implemented_yet**
> V1Migration not_implemented_yet(namespace, field_selector=field_selector, label_selector=label_selector, resource_version=resource_version, timeout_seconds=timeout_seconds)



### Example
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ApiskubevirtiovalphaApi()
namespace = 'namespace_example' # str | Object name and auth scope, such as for teams and projects
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = swagger_client.Object() # Object | TimeoutSeconds for the list/watch call. (optional)

try:
    api_response = api_instance.not_implemented_yet(namespace, field_selector=field_selector, label_selector=label_selector, resource_version=resource_version, timeout_seconds=timeout_seconds)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApiskubevirtiovalphaApi->not_implemented_yet: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**| Object name and auth scope, such as for teams and projects |
 **field_selector** | **str**| A selector to restrict the list of returned objects by their fields. Defaults to everything. | [optional]
 **label_selector** | **str**| A selector to restrict the list of returned objects by their labels. Defaults to everything | [optional]
 **resource_version** | **str**| When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. | [optional]
 **timeout_seconds** | [**Object**](.md)| TimeoutSeconds for the list/watch call. | [optional]

### Return type

[**V1Migration**](V1Migration.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **not_implemented_yet_0**
> V1Migration not_implemented_yet_0(namespace, field_selector=field_selector, label_selector=label_selector, resource_version=resource_version, timeout_seconds=timeout_seconds)



### Example
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ApiskubevirtiovalphaApi()
namespace = 'namespace_example' # str | Object name and auth scope, such as for teams and projects
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = swagger_client.Object() # Object | TimeoutSeconds for the list/watch call. (optional)

try:
    api_response = api_instance.not_implemented_yet_0(namespace, field_selector=field_selector, label_selector=label_selector, resource_version=resource_version, timeout_seconds=timeout_seconds)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApiskubevirtiovalphaApi->not_implemented_yet_0: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**| Object name and auth scope, such as for teams and projects |
 **field_selector** | **str**| A selector to restrict the list of returned objects by their fields. Defaults to everything. | [optional]
 **label_selector** | **str**| A selector to restrict the list of returned objects by their labels. Defaults to everything | [optional]
 **resource_version** | **str**| When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. | [optional]
 **timeout_seconds** | [**Object**](.md)| TimeoutSeconds for the list/watch call. | [optional]

### Return type

[**V1Migration**](V1Migration.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **not_implemented_yet_1**
> V1VirtualMachine not_implemented_yet_1(namespace, field_selector=field_selector, label_selector=label_selector, resource_version=resource_version, timeout_seconds=timeout_seconds)



### Example
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ApiskubevirtiovalphaApi()
namespace = 'namespace_example' # str | Object name and auth scope, such as for teams and projects
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = swagger_client.Object() # Object | TimeoutSeconds for the list/watch call. (optional)

try:
    api_response = api_instance.not_implemented_yet_1(namespace, field_selector=field_selector, label_selector=label_selector, resource_version=resource_version, timeout_seconds=timeout_seconds)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApiskubevirtiovalphaApi->not_implemented_yet_1: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**| Object name and auth scope, such as for teams and projects |
 **field_selector** | **str**| A selector to restrict the list of returned objects by their fields. Defaults to everything. | [optional]
 **label_selector** | **str**| A selector to restrict the list of returned objects by their labels. Defaults to everything | [optional]
 **resource_version** | **str**| When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. | [optional]
 **timeout_seconds** | [**Object**](.md)| TimeoutSeconds for the list/watch call. | [optional]

### Return type

[**V1VirtualMachine**](V1VirtualMachine.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **not_implemented_yet_2**
> V1VirtualMachine not_implemented_yet_2(namespace, field_selector=field_selector, label_selector=label_selector, resource_version=resource_version, timeout_seconds=timeout_seconds)



### Example
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ApiskubevirtiovalphaApi()
namespace = 'namespace_example' # str | Object name and auth scope, such as for teams and projects
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = swagger_client.Object() # Object | TimeoutSeconds for the list/watch call. (optional)

try:
    api_response = api_instance.not_implemented_yet_2(namespace, field_selector=field_selector, label_selector=label_selector, resource_version=resource_version, timeout_seconds=timeout_seconds)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApiskubevirtiovalphaApi->not_implemented_yet_2: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**| Object name and auth scope, such as for teams and projects |
 **field_selector** | **str**| A selector to restrict the list of returned objects by their fields. Defaults to everything. | [optional]
 **label_selector** | **str**| A selector to restrict the list of returned objects by their labels. Defaults to everything | [optional]
 **resource_version** | **str**| When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. | [optional]
 **timeout_seconds** | [**Object**](.md)| TimeoutSeconds for the list/watch call. | [optional]

### Return type

[**V1VirtualMachine**](V1VirtualMachine.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

