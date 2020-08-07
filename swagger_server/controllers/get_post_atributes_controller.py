import connexion
import six
from pymongo import MongoClient
from flask import jsonify
import pprint

from swagger_server.models.successfull1 import Successfull1  # noqa: E501
from swagger_server import util


def get_post_atributes(post_id):  # noqa: E501
    """Get post atributes

    You can get the list of the post&#x27;s atributes. # noqa: E501

    :param post_id: Post id
    :type post_id: str

    :rtype: Successfull1
    """
    client = MongoClient('localhost', 27017)
    db = client.database
    posts = db.posts
    post_data = posts.find_one({'post_id': int(post_id)})
    if post_data:
        atributes = post_data.get('post_attributes')
        pprint.pprint(atributes)
        del posts
        del db
        del client
        return jsonify({'atributes': atributes, 'result': True}), 201
    del posts
    del db
    del client
    return jsonify({'result': False}), 501
