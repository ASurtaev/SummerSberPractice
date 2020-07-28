# swagger_client.EditPostApi

All URIs are relative to *https://contentmnagement.org/data/2.5/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**edit_post**](EditPostApi.md#edit_post) | **POST** /Edit_post_field | Edit post

# **edit_post**
> edit_post(post_id, index_field)

Edit post

You can change the post's atribute using it's index from GetPostAtributes

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.EditPostApi()
post_id = 'post_id_example' # str | Post id
index_field = 56 # int | Index of the required field

try:
    # Edit post
    api_instance.edit_post(post_id, index_field)
except ApiException as e:
    print("Exception when calling EditPostApi->edit_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **post_id** | **str**| Post id | 
 **index_field** | **int**| Index of the required field | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

