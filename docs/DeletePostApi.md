# swagger_client.DeletePostApi

All URIs are relative to *https://contentmnagement.org/data/2.5/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_post**](DeletePostApi.md#delete_post) | **DELETE** /Delete_post | Delete post

# **delete_post**
> str delete_post(post_id)

Delete post

There is description

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DeletePostApi()
post_id = 'post_id_example' # str | Post id

try:
    # Delete post
    api_response = api_instance.delete_post(post_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeletePostApi->delete_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **post_id** | **str**| Post id | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

