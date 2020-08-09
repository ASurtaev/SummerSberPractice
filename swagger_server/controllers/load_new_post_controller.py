import connexion
import six
from pymongo import MongoClient
from flask import jsonify

from swagger_server.models.successfull import Successfull  # noqa: E501
from swagger_server import util


def load_new_post(photo, post_name, post_atributes=None, tag_post=None, load_data_time=None, file_size=None, file_size_pixels=None, user_id=None, geolocation=None, file_format=None):  # noqa: E501
    """Loads a new post

    API for loading a new post to the database # noqa: E501

    :param photo: Photo file in string format
    :type photo: str
    :param post_name: Name of post
    :type post_name: str
    :param post_atributes: Atributes of post, name of the attribute and it&#x27;s value are divided with &#x27;:&#x27; 
    :type post_atributes: List[str]
    :param tag_post: Tags of post
    :type tag_post: List[str]
    :param load_data_time: Time of loading post
    :type load_data_time: str
    :param file_size: Size of the photo file in bytes
    :type file_size: int
    :param file_size_pixels: Size of the photo file in pixels
    :type file_size_pixels: List[int]
    :param user_id: Id of the user which has loaded the post
    :type user_id: int
    :param geolocation: Geolocation of the user
    :type geolocation: str
    :param file_format: Format of file like JPEG,PNG,BMP or others
    :type file_format: str

    :rtype: Successfull
    """
    client = MongoClient('mongo', 27017)
    try:
        with open('idcounter.dat', 'r') as file_id_counter:
            post_id = int(file_id_counter.readline())
    except Exception as e:
        print('Exception:', e)
        del client
        return jsonify({'result': False}), 500

    db = client.database
    posts = db.posts

    post_data = {
        'photo': photo,
        'post_name': post_name,
        'post_id': post_id
    }
    if post_atributes:
        post_data['post_attributes'] = post_atributes
    if tag_post:
        post_data['tag_post'] = tag_post
    if load_data_time:
        post_data['load_data_time'] = load_data_time
    if file_size:
        post_data['file_size'] = file_size
    if file_size_pixels:
        post_data['file_size_pixels'] = file_size_pixels
    if geolocation:
        post_data['geolocation'] = geolocation
    if user_id:
        post_data['user_id'] = user_id
    if file_format:
        post_data['file_format'] = file_format

    try:
        posts.insert_one(post_data)
    except Exception as e:
        print('Exception:', e)
        del posts
        del db
        del client
        return jsonify({'result': False}), 501

    with open('idcounter.dat', 'w') as file_id_counter:
        print(post_id + 1, file=file_id_counter)

    print('added post')
    del posts
    del db
    del client
    return jsonify({'post_id': post_id, 'result': True}), 201
