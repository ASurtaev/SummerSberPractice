# swagger_client.LoadNewPostApi

All URIs are relative to *https://contentmnagement.org/data/2.5/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**load_new_post**](LoadNewPostApi.md#load_new_post) | **POST** /Load_new_post | Loads a new post

# **load_new_post**
> Successfull load_new_post(photo, description_post, tag_post, load_data_time=load_data_time, file_size=file_size, file_size_pixels=file_size_pixels, geolocation=geolocation, user_id=user_id, mac_adress=mac_adress, ip_adress=ip_adress, file_format=file_format)

Loads a new post

There is description

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.LoadNewPostApi()
photo = 'photo_example' # str | Photo file in base64(?) format
description_post = ['description_post_example'] # list[str] | Atributes of post. Post name is always atribute with index 0.
tag_post = ['tag_post_example'] # list[str] | Atributes of post
load_data_time = 'load_data_time_example' # str | Time of loading post (optional)
file_size = 56 # int | Size of the photo file in bytes (optional)
file_size_pixels = [56] # list[int] | Size of the photo file in pixels (optional)
geolocation = 'geolocation_example' # str | Geolocation of the user (optional)
user_id = 'user_id_example' # str | Id of the user (optional)
mac_adress = 'mac_adress_example' # str | MAC-adress of the user device, from which was loaded the post (optional)
ip_adress = 'ip_adress_example' # str | IP-adress of the user device, from which was loaded the post (optional)
file_format = 'file_format_example' # str | Format of file like JPEG,PNG,BMP or others (optional)

try:
    # Loads a new post
    api_response = api_instance.load_new_post(photo, description_post, tag_post, load_data_time=load_data_time, file_size=file_size, file_size_pixels=file_size_pixels, geolocation=geolocation, user_id=user_id, mac_adress=mac_adress, ip_adress=ip_adress, file_format=file_format)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LoadNewPostApi->load_new_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **photo** | **str**| Photo file in base64(?) format | 
 **description_post** | [**list[str]**](str.md)| Atributes of post. Post name is always atribute with index 0. | 
 **tag_post** | [**list[str]**](str.md)| Atributes of post | 
 **load_data_time** | **str**| Time of loading post | [optional] 
 **file_size** | **int**| Size of the photo file in bytes | [optional] 
 **file_size_pixels** | [**list[int]**](int.md)| Size of the photo file in pixels | [optional] 
 **geolocation** | **str**| Geolocation of the user | [optional] 
 **user_id** | **str**| Id of the user | [optional] 
 **mac_adress** | **str**| MAC-adress of the user device, from which was loaded the post | [optional] 
 **ip_adress** | **str**| IP-adress of the user device, from which was loaded the post | [optional] 
 **file_format** | **str**| Format of file like JPEG,PNG,BMP or others | [optional] 

### Return type

[**Successfull**](Successfull.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

