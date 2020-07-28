# swagger_client.GetMetadataPostApi

All URIs are relative to *https://contentmnagement.org/data/2.5/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_metadata_post**](GetMetadataPostApi.md#get_metadata_post) | **GET** /Get_metadata_post | Get metadata post

# **get_metadata_post**
> Successfull3 get_metadata_post(post_id)

Get metadata post

There is description

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.GetMetadataPostApi()
post_id = 'post_id_example' # str | Post id

try:
    # Get metadata post
    api_response = api_instance.get_metadata_post(post_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GetMetadataPostApi->get_metadata_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **post_id** | **str**| Post id | 

### Return type

[**Successfull3**](Successfull3.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

