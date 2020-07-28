# swagger_client.GetPostApi

All URIs are relative to *https://contentmnagement.org/data/2.5/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_post**](GetPostApi.md#get_post) | **GET** /Get_post | Get post

# **get_post**
> Successfull2 get_post(post_id)

Get post

Get post by it's atributes

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.GetPostApi()
post_id = 'post_id_example' # str | Post id

try:
    # Get post
    api_response = api_instance.get_post(post_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GetPostApi->get_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **post_id** | **str**| Post id | 

### Return type

[**Successfull2**](Successfull2.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

