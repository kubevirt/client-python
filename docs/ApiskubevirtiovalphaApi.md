# swagger_client.ApiskubevirtiovalphaApi

All URIs are relative to *http://localhost:8183/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**console**](ApiskubevirtiovalphaApi.md#console) | **GET** /apis/kubevirt.io/v1alpha1/namespaces/{namespace:[a-z0-9][a-z0-9\-]*}/virtualmachines/{name:[a-z0-9][a-z0-9\-]*}/console | Open a websocket connection to a serial console on the specified VM.
[**create_migration**](ApiskubevirtiovalphaApi.md#create_migration) | **POST** /apis/kubevirt.io/v1alpha1/namespaces/{namespace:[a-z0-9][a-z0-9\-]*}/migrations |
[**create_virtualmachine**](ApiskubevirtiovalphaApi.md#create_virtualmachine) | **POST** /apis/kubevirt.io/v1alpha1/namespaces/{namespace:[a-z0-9][a-z0-9\-]*}/virtualmachines |
[**create_virtualmachinereplicaset**](ApiskubevirtiovalphaApi.md#create_virtualmachinereplicaset) | **POST** /apis/kubevirt.io/v1alpha1/namespaces/{namespace:[a-z0-9][a-z0-9\-]*}/virtualmachinereplicasets |
[**delete_migration**](ApiskubevirtiovalphaApi.md#delete_migration) | **DELETE** /apis/kubevirt.io/v1alpha1/namespaces/{namespace:[a-z0-9][a-z0-9\-]*}/migrations/{name:[a-z0-9][a-z0-9\-]*} | test3
[**delete_migrations**](ApiskubevirtiovalphaApi.md#delete_migrations) | **DELETE** /apis/kubevirt.io/v1alpha1/namespaces/{namespace:[a-z0-9][a-z0-9\-]*}/migrations |
[**delete_virtualmachine**](ApiskubevirtiovalphaApi.md#delete_virtualmachine) | **DELETE** /apis/kubevirt.io/v1alpha1/namespaces/{namespace:[a-z0-9][a-z0-9\-]*}/virtualmachines/{name:[a-z0-9][a-z0-9\-]*} | test3
[**delete_virtualmachinereplicaset**](ApiskubevirtiovalphaApi.md#delete_virtualmachinereplicaset) | **DELETE** /apis/kubevirt.io/v1alpha1/namespaces/{namespace:[a-z0-9][a-z0-9\-]*}/virtualmachinereplicasets/{name:[a-z0-9][a-z0-9\-]*} | test3
[**delete_virtualmachinereplicasets**](ApiskubevirtiovalphaApi.md#delete_virtualmachinereplicasets) | **DELETE** /apis/kubevirt.io/v1alpha1/namespaces/{namespace:[a-z0-9][a-z0-9\-]*}/virtualmachinereplicasets |
[**delete_virtualmachines**](ApiskubevirtiovalphaApi.md#delete_virtualmachines) | **DELETE** /apis/kubevirt.io/v1alpha1/namespaces/{namespace:[a-z0-9][a-z0-9\-]*}/virtualmachines |
[**func1**](ApiskubevirtiovalphaApi.md#func1) | **GET** /apis/kubevirt.io/v1alpha1 |
[**get_migration**](ApiskubevirtiovalphaApi.md#get_migration) | **GET** /apis/kubevirt.io/v1alpha1/namespaces/{namespace:[a-z0-9][a-z0-9\-]*}/migrations/{name:[a-z0-9][a-z0-9\-]*} | test4
[**get_virtualmachine**](ApiskubevirtiovalphaApi.md#get_virtualmachine) | **GET** /apis/kubevirt.io/v1alpha1/namespaces/{namespace:[a-z0-9][a-z0-9\-]*}/virtualmachines/{name:[a-z0-9][a-z0-9\-]*} | test4
[**get_virtualmachinereplicaset**](ApiskubevirtiovalphaApi.md#get_virtualmachinereplicaset) | **GET** /apis/kubevirt.io/v1alpha1/namespaces/{namespace:[a-z0-9][a-z0-9\-]*}/virtualmachinereplicasets/{name:[a-z0-9][a-z0-9\-]*} | test4
[**kube_connection_healthz_func**](ApiskubevirtiovalphaApi.md#kube_connection_healthz_func) | **GET** /apis/kubevirt.io/v1alpha1/healthz | Health endpoint
[**list_all_migrations**](ApiskubevirtiovalphaApi.md#list_all_migrations) | **GET** /apis/kubevirt.io/v1alpha1/migrations | test4
[**list_all_virtualmachinereplicasets**](ApiskubevirtiovalphaApi.md#list_all_virtualmachinereplicasets) | **GET** /apis/kubevirt.io/v1alpha1/virtualmachinereplicasets | test4
[**list_all_virtualmachines**](ApiskubevirtiovalphaApi.md#list_all_virtualmachines) | **GET** /apis/kubevirt.io/v1alpha1/virtualmachines | test4
[**list_migrations**](ApiskubevirtiovalphaApi.md#list_migrations) | **GET** /apis/kubevirt.io/v1alpha1/namespaces/{namespace:[a-z0-9][a-z0-9\-]*}/migrations |
[**list_virtualmachinereplicasets**](ApiskubevirtiovalphaApi.md#list_virtualmachinereplicasets) | **GET** /apis/kubevirt.io/v1alpha1/namespaces/{namespace:[a-z0-9][a-z0-9\-]*}/virtualmachinereplicasets |
[**list_virtualmachines**](ApiskubevirtiovalphaApi.md#list_virtualmachines) | **GET** /apis/kubevirt.io/v1alpha1/namespaces/{namespace:[a-z0-9][a-z0-9\-]*}/virtualmachines |
[**patch_migration**](ApiskubevirtiovalphaApi.md#patch_migration) | **PATCH** /apis/kubevirt.io/v1alpha1/namespaces/{namespace:[a-z0-9][a-z0-9\-]*}/migrations/{name:[a-z0-9][a-z0-9\-]*} | test5
[**patch_virtualmachine**](ApiskubevirtiovalphaApi.md#patch_virtualmachine) | **PATCH** /apis/kubevirt.io/v1alpha1/namespaces/{namespace:[a-z0-9][a-z0-9\-]*}/virtualmachines/{name:[a-z0-9][a-z0-9\-]*} | test5
[**patch_virtualmachinereplicaset**](ApiskubevirtiovalphaApi.md#patch_virtualmachinereplicaset) | **PATCH** /apis/kubevirt.io/v1alpha1/namespaces/{namespace:[a-z0-9][a-z0-9\-]*}/virtualmachinereplicasets/{name:[a-z0-9][a-z0-9\-]*} | test5
[**spice**](ApiskubevirtiovalphaApi.md#spice) | **GET** /apis/kubevirt.io/v1alpha1/namespaces/{namespace:[a-z0-9][a-z0-9\-]*}/virtualmachines/{name:[a-z0-9][a-z0-9\-]*}/spice | Returns a remote-viewer configuration file. Run &#x60;man 1 remote-viewer&#x60; to learn more about the configuration format.
[**update_migration**](ApiskubevirtiovalphaApi.md#update_migration) | **PUT** /apis/kubevirt.io/v1alpha1/namespaces/{namespace:[a-z0-9][a-z0-9\-]*}/migrations/{name:[a-z0-9][a-z0-9\-]*} | test2
[**update_virtualmachine**](ApiskubevirtiovalphaApi.md#update_virtualmachine) | **PUT** /apis/kubevirt.io/v1alpha1/namespaces/{namespace:[a-z0-9][a-z0-9\-]*}/virtualmachines/{name:[a-z0-9][a-z0-9\-]*} | test2
[**update_virtualmachinereplicaset**](ApiskubevirtiovalphaApi.md#update_virtualmachinereplicaset) | **PUT** /apis/kubevirt.io/v1alpha1/namespaces/{namespace:[a-z0-9][a-z0-9\-]*}/virtualmachinereplicasets/{name:[a-z0-9][a-z0-9\-]*} | test2
[**watch_all_migrations**](ApiskubevirtiovalphaApi.md#watch_all_migrations) | **GET** /apis/kubevirt.io/v1alpha1/watch/migrations |
[**watch_all_virtualmachinereplicasets**](ApiskubevirtiovalphaApi.md#watch_all_virtualmachinereplicasets) | **GET** /apis/kubevirt.io/v1alpha1/watch/virtualmachinereplicasets |
[**watch_all_virtualmachines**](ApiskubevirtiovalphaApi.md#watch_all_virtualmachines) | **GET** /apis/kubevirt.io/v1alpha1/watch/virtualmachines |
[**watch_migrations**](ApiskubevirtiovalphaApi.md#watch_migrations) | **GET** /apis/kubevirt.io/v1alpha1/watch/namespaces/{namespace:[a-z0-9][a-z0-9\-]*}/migrations |
[**watch_virtualmachinereplicasets**](ApiskubevirtiovalphaApi.md#watch_virtualmachinereplicasets) | **GET** /apis/kubevirt.io/v1alpha1/watch/namespaces/{namespace:[a-z0-9][a-z0-9\-]*}/virtualmachinereplicasets |
[**watch_virtualmachines**](ApiskubevirtiovalphaApi.md#watch_virtualmachines) | **GET** /apis/kubevirt.io/v1alpha1/watch/namespaces/{namespace:[a-z0-9][a-z0-9\-]*}/virtualmachines |


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

# **create_migration**
> V1Migration create_migration(body, namespace)



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
    api_response = api_instance.create_migration(body, namespace)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApiskubevirtiovalphaApi->create_migration: %s\n" % e
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

# **create_virtualmachine**
> V1VirtualMachine create_virtualmachine(body, namespace)



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
    api_response = api_instance.create_virtualmachine(body, namespace)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApiskubevirtiovalphaApi->create_virtualmachine: %s\n" % e
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

# **create_virtualmachinereplicaset**
> V1VirtualMachineReplicaSet create_virtualmachinereplicaset(body, namespace)



### Example
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ApiskubevirtiovalphaApi()
body = swagger_client.V1VirtualMachineReplicaSet() # V1VirtualMachineReplicaSet |
namespace = 'namespace_example' # str | Object name and auth scope, such as for teams and projects

try:
    api_response = api_instance.create_virtualmachinereplicaset(body, namespace)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApiskubevirtiovalphaApi->create_virtualmachinereplicaset: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1VirtualMachineReplicaSet**](V1VirtualMachineReplicaSet.md)|  |
 **namespace** | **str**| Object name and auth scope, such as for teams and projects |

### Return type

[**V1VirtualMachineReplicaSet**](V1VirtualMachineReplicaSet.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/yaml
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_migration**
> V1Status delete_migration(namespace, name)

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
    api_response = api_instance.delete_migration(namespace, name)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApiskubevirtiovalphaApi->delete_migration: %s\n" % e
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

# **delete_migrations**
> V1MigrationList delete_migrations(name, field_selector=field_selector, label_selector=label_selector)



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
    api_response = api_instance.delete_migrations(name, field_selector=field_selector, label_selector=label_selector)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApiskubevirtiovalphaApi->delete_migrations: %s\n" % e
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

# **delete_virtualmachine**
> V1Status delete_virtualmachine(namespace, name)

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
    api_response = api_instance.delete_virtualmachine(namespace, name)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApiskubevirtiovalphaApi->delete_virtualmachine: %s\n" % e
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

# **delete_virtualmachinereplicaset**
> V1Status delete_virtualmachinereplicaset(namespace, name)

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
    api_response = api_instance.delete_virtualmachinereplicaset(namespace, name)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApiskubevirtiovalphaApi->delete_virtualmachinereplicaset: %s\n" % e
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

# **delete_virtualmachinereplicasets**
> V1VirtualMachineReplicaSetList delete_virtualmachinereplicasets(name, field_selector=field_selector, label_selector=label_selector)



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
    api_response = api_instance.delete_virtualmachinereplicasets(name, field_selector=field_selector, label_selector=label_selector)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApiskubevirtiovalphaApi->delete_virtualmachinereplicasets: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the resource |
 **field_selector** | **str**| A selector to restrict the list of returned objects by their fields. Defaults to everything. | [optional]
 **label_selector** | **str**| A selector to restrict the list of returned objects by their labels. Defaults to everything | [optional]

### Return type

[**V1VirtualMachineReplicaSetList**](V1VirtualMachineReplicaSetList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_virtualmachines**
> V1VirtualMachineList delete_virtualmachines(name, field_selector=field_selector, label_selector=label_selector)



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
    api_response = api_instance.delete_virtualmachines(name, field_selector=field_selector, label_selector=label_selector)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApiskubevirtiovalphaApi->delete_virtualmachines: %s\n" % e
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

# **get_migration**
> V1Migration get_migration(namespace, name, export=export, exact=exact)

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
    api_response = api_instance.get_migration(namespace, name, export=export, exact=exact)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApiskubevirtiovalphaApi->get_migration: %s\n" % e
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

# **get_virtualmachine**
> V1VirtualMachine get_virtualmachine(namespace, name, export=export, exact=exact)

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
    api_response = api_instance.get_virtualmachine(namespace, name, export=export, exact=exact)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApiskubevirtiovalphaApi->get_virtualmachine: %s\n" % e
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

# **get_virtualmachinereplicaset**
> V1VirtualMachineReplicaSet get_virtualmachinereplicaset(namespace, name, export=export, exact=exact)

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
    api_response = api_instance.get_virtualmachinereplicaset(namespace, name, export=export, exact=exact)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApiskubevirtiovalphaApi->get_virtualmachinereplicaset: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**| Object name and auth scope, such as for teams and projects |
 **name** | **str**| Name of the resource |
 **export** | **bool**| Should this value be exported. Export strips fields that a user can not specify. | [optional]
 **exact** | **bool**| Should the export be exact. Exact export maintains cluster-specific fields like &#39;Namespace&#39; | [optional]

### Return type

[**V1VirtualMachineReplicaSet**](V1VirtualMachineReplicaSet.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
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

# **list_all_migrations**
> V1MigrationList list_all_migrations(field_selector=field_selector, label_selector=label_selector, resource_version=resource_version, timeout_seconds=timeout_seconds)

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
    api_response = api_instance.list_all_migrations(field_selector=field_selector, label_selector=label_selector, resource_version=resource_version, timeout_seconds=timeout_seconds)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApiskubevirtiovalphaApi->list_all_migrations: %s\n" % e
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

# **list_all_virtualmachinereplicasets**
> V1VirtualMachineReplicaSetList list_all_virtualmachinereplicasets(field_selector=field_selector, label_selector=label_selector, resource_version=resource_version, timeout_seconds=timeout_seconds)

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
    api_response = api_instance.list_all_virtualmachinereplicasets(field_selector=field_selector, label_selector=label_selector, resource_version=resource_version, timeout_seconds=timeout_seconds)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApiskubevirtiovalphaApi->list_all_virtualmachinereplicasets: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **field_selector** | **str**| A selector to restrict the list of returned objects by their fields. Defaults to everything. | [optional]
 **label_selector** | **str**| A selector to restrict the list of returned objects by their labels. Defaults to everything | [optional]
 **resource_version** | **str**| When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. | [optional]
 **timeout_seconds** | [**Object**](.md)| TimeoutSeconds for the list/watch call. | [optional]

### Return type

[**V1VirtualMachineReplicaSetList**](V1VirtualMachineReplicaSetList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_all_virtualmachines**
> V1VirtualMachineList list_all_virtualmachines(field_selector=field_selector, label_selector=label_selector, resource_version=resource_version, timeout_seconds=timeout_seconds)

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
    api_response = api_instance.list_all_virtualmachines(field_selector=field_selector, label_selector=label_selector, resource_version=resource_version, timeout_seconds=timeout_seconds)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApiskubevirtiovalphaApi->list_all_virtualmachines: %s\n" % e
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

# **list_migrations**
> V1MigrationList list_migrations(namespace, field_selector=field_selector, label_selector=label_selector, resource_version=resource_version, timeout_seconds=timeout_seconds)



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
    api_response = api_instance.list_migrations(namespace, field_selector=field_selector, label_selector=label_selector, resource_version=resource_version, timeout_seconds=timeout_seconds)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApiskubevirtiovalphaApi->list_migrations: %s\n" % e
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

# **list_virtualmachinereplicasets**
> V1VirtualMachineReplicaSetList list_virtualmachinereplicasets(namespace, field_selector=field_selector, label_selector=label_selector, resource_version=resource_version, timeout_seconds=timeout_seconds)



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
    api_response = api_instance.list_virtualmachinereplicasets(namespace, field_selector=field_selector, label_selector=label_selector, resource_version=resource_version, timeout_seconds=timeout_seconds)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApiskubevirtiovalphaApi->list_virtualmachinereplicasets: %s\n" % e
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

[**V1VirtualMachineReplicaSetList**](V1VirtualMachineReplicaSetList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_virtualmachines**
> V1VirtualMachineList list_virtualmachines(namespace, field_selector=field_selector, label_selector=label_selector, resource_version=resource_version, timeout_seconds=timeout_seconds)



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
    api_response = api_instance.list_virtualmachines(namespace, field_selector=field_selector, label_selector=label_selector, resource_version=resource_version, timeout_seconds=timeout_seconds)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApiskubevirtiovalphaApi->list_virtualmachines: %s\n" % e
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

# **patch_migration**
> V1Migration patch_migration()

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
    api_response = api_instance.patch_migration()
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApiskubevirtiovalphaApi->patch_migration: %s\n" % e
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

# **patch_virtualmachine**
> V1VirtualMachine patch_virtualmachine()

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
    api_response = api_instance.patch_virtualmachine()
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApiskubevirtiovalphaApi->patch_virtualmachine: %s\n" % e
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

# **patch_virtualmachinereplicaset**
> V1VirtualMachineReplicaSet patch_virtualmachinereplicaset()

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
    api_response = api_instance.patch_virtualmachinereplicaset()
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApiskubevirtiovalphaApi->patch_virtualmachinereplicaset: %s\n" % e
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**V1VirtualMachineReplicaSet**](V1VirtualMachineReplicaSet.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json-patch+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **spice**
> spice(namespace, name)

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
    api_instance.spice(namespace, name)
except ApiException as e:
    print "Exception when calling ApiskubevirtiovalphaApi->spice: %s\n" % e
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

# **update_migration**
> V1Migration update_migration(body, namespace, name)

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
    api_response = api_instance.update_migration(body, namespace, name)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApiskubevirtiovalphaApi->update_migration: %s\n" % e
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

# **update_virtualmachine**
> V1VirtualMachine update_virtualmachine(body, namespace, name)

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
    api_response = api_instance.update_virtualmachine(body, namespace, name)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApiskubevirtiovalphaApi->update_virtualmachine: %s\n" % e
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

# **update_virtualmachinereplicaset**
> V1VirtualMachineReplicaSet update_virtualmachinereplicaset(body, namespace, name)

test2

### Example
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ApiskubevirtiovalphaApi()
body = swagger_client.V1VirtualMachineReplicaSet() # V1VirtualMachineReplicaSet |
namespace = 'namespace_example' # str | Object name and auth scope, such as for teams and projects
name = 'name_example' # str | Name of the resource

try:
    # test2
    api_response = api_instance.update_virtualmachinereplicaset(body, namespace, name)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApiskubevirtiovalphaApi->update_virtualmachinereplicaset: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1VirtualMachineReplicaSet**](V1VirtualMachineReplicaSet.md)|  |
 **namespace** | **str**| Object name and auth scope, such as for teams and projects |
 **name** | **str**| Name of the resource |

### Return type

[**V1VirtualMachineReplicaSet**](V1VirtualMachineReplicaSet.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/yaml
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **watch_all_migrations**
> V1Migration watch_all_migrations(namespace, field_selector=field_selector, label_selector=label_selector, resource_version=resource_version, timeout_seconds=timeout_seconds)



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
    api_response = api_instance.watch_all_migrations(namespace, field_selector=field_selector, label_selector=label_selector, resource_version=resource_version, timeout_seconds=timeout_seconds)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApiskubevirtiovalphaApi->watch_all_migrations: %s\n" % e
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

# **watch_all_virtualmachinereplicasets**
> V1VirtualMachineReplicaSet watch_all_virtualmachinereplicasets(namespace, field_selector=field_selector, label_selector=label_selector, resource_version=resource_version, timeout_seconds=timeout_seconds)



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
    api_response = api_instance.watch_all_virtualmachinereplicasets(namespace, field_selector=field_selector, label_selector=label_selector, resource_version=resource_version, timeout_seconds=timeout_seconds)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApiskubevirtiovalphaApi->watch_all_virtualmachinereplicasets: %s\n" % e
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

[**V1VirtualMachineReplicaSet**](V1VirtualMachineReplicaSet.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **watch_all_virtualmachines**
> V1VirtualMachine watch_all_virtualmachines(namespace, field_selector=field_selector, label_selector=label_selector, resource_version=resource_version, timeout_seconds=timeout_seconds)



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
    api_response = api_instance.watch_all_virtualmachines(namespace, field_selector=field_selector, label_selector=label_selector, resource_version=resource_version, timeout_seconds=timeout_seconds)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApiskubevirtiovalphaApi->watch_all_virtualmachines: %s\n" % e
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

# **watch_migrations**
> V1Migration watch_migrations(namespace, field_selector=field_selector, label_selector=label_selector, resource_version=resource_version, timeout_seconds=timeout_seconds)



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
    api_response = api_instance.watch_migrations(namespace, field_selector=field_selector, label_selector=label_selector, resource_version=resource_version, timeout_seconds=timeout_seconds)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApiskubevirtiovalphaApi->watch_migrations: %s\n" % e
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

# **watch_virtualmachinereplicasets**
> V1VirtualMachineReplicaSet watch_virtualmachinereplicasets(namespace, field_selector=field_selector, label_selector=label_selector, resource_version=resource_version, timeout_seconds=timeout_seconds)



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
    api_response = api_instance.watch_virtualmachinereplicasets(namespace, field_selector=field_selector, label_selector=label_selector, resource_version=resource_version, timeout_seconds=timeout_seconds)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApiskubevirtiovalphaApi->watch_virtualmachinereplicasets: %s\n" % e
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

[**V1VirtualMachineReplicaSet**](V1VirtualMachineReplicaSet.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **watch_virtualmachines**
> V1VirtualMachine watch_virtualmachines(namespace, field_selector=field_selector, label_selector=label_selector, resource_version=resource_version, timeout_seconds=timeout_seconds)



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
    api_response = api_instance.watch_virtualmachines(namespace, field_selector=field_selector, label_selector=label_selector, resource_version=resource_version, timeout_seconds=timeout_seconds)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApiskubevirtiovalphaApi->watch_virtualmachines: %s\n" % e
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

