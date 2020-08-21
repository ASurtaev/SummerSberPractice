import connexion
import six
from pymongo import MongoClient
from flask import jsonify

from swagger_server.models.successfull3 import Successfull3  # noqa: E501
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


def get_metadata_post(post_id):  # noqa: E501
    """Get metadata post

    API to get the metadata of the post # noqa: E501

    :param post_id: Post id
    :type post_id: str

    :rtype: Successfull3
    """
    client = MongoClient('localhost', 27017)
    db = client.database
    posts = db.posts
    post_data = posts.find_one({'post_id': int(post_id)})
    if post_data:
        post_data = existing_metadata(post_data)
        post_data['result'] = True
        del posts
        del db
        del client
        return jsonify(post_data), 201
    del posts
    del db
    del client
    return jsonify({'result': False}), 501
