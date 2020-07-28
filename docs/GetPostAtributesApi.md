# swagger_client.GetPostAtributesApi

All URIs are relative to *https://contentmnagement.org/data/2.5/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_post_atributes**](GetPostAtributesApi.md#get_post_atributes) | **GET** /Get_post_atributes | Get post atributes

# **get_post_atributes**
> Successfull1 get_post_atributes(post_id)

Get post atributes

You can get the list of the post's indexes, name of the post always has index 0

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.GetPostAtributesApi()
post_id = 'post_id_example' # str | Post id

try:
    # Get post atributes
    api_response = api_instance.get_post_atributes(post_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GetPostAtributesApi->get_post_atributes: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **post_id** | **str**| Post id | 

### Return type

[**Successfull1**](Successfull1.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

