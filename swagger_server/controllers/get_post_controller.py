import connexion
import six
import pprint
from pymongo import MongoClient
from flask import jsonify

from swagger_server.models.successfull2 import Successfull2  # noqa: E501
from swagger_server import util


def existing_metadata(post_data):
    new_data = {}
    load_data_time = post_data.get('load_data_time', None)
    if load_data_time:
        new_data['load_data_time'] = load_data_time
    file_size = post_data.get('file_size', None)
    if file_size:
        new_data['file_size'] = file_size

    file_size_pixels = post_data.get('file_size_pixels', None)
    if file_size_pixels:
        new_data['file_size_pixels'] = file_size_pixels

    geolocation = post_data.get('geolocation', None)
    if geolocation:
        new_data['geolocation'] = geolocation

    user_id = post_data.get('user_id', None)
    if user_id:
        new_data['user_id'] = user_id

    file_format = post_data.get('file_format', None)
    if file_format:
        new_data['file_format'] = file_format
    return new_data


def get_post(post_id):  # noqa: E501
    """Get post

    Get post&#x27;s name and photo # noqa: E501

    :param post_id: Post id
    :type post_id: str

    :rtype: Successfull2
    """
    client = MongoClient('mongo', 27017)
    db = client.database
    posts = db.posts
    post_data = posts.find_one({'post_id': int(post_id)})
    if post_data:
        # testing 2 lines
        pprint.pprint(post_data)
        print(type(post_data))
        post_metadata = existing_metadata(post_data)
        photo = post_data.get('photo')
        name = post_data.get('post_name')
        post_attributes = post_data.get('post_attributes')
        tags = post_data.get('tag_post')
        del posts
        del db
        del client
        return jsonify({'photo': photo, 'name': name, 'post_attributes': post_attributes, 'tags': tags, 'post_metadata': post_metadata}), 201
    del posts
    del db
    del client
    return jsonify({}), 501
