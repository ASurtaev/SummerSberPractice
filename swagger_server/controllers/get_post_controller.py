import connexion
import six
import pprint
from pymongo import MongoClient
from flask import jsonify

from swagger_server.models.successfull2 import Successfull2  # noqa: E501
from swagger_server import util


def get_post(post_id):  # noqa: E501
    """Get post

    Get post&#x27;s name and photo # noqa: E501

    :param post_id: Post id
    :type post_id: str

    :rtype: Successfull2
    """
    client = MongoClient('localhost', 27017)
    db = client.database
    posts = db.posts
    post_data = posts.find_one({'post_id': int(post_id)})
    if post_data:
        #testing 2 lines
        pprint.pprint(post_data)
        print(type(post_data))
        photo = post_data.get('photo')
        del posts
        del db
        del client
        return jsonify({'name': photo}), 201
    del posts
    del db
    del client
    return jsonify({}), 501
