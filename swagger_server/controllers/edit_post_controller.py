import connexion
import six
from pymongo import MongoClient
from flask import jsonify

from swagger_server import util


def edit_post(post_id, index_field):  # noqa: E501
    """Edit post

    You can change the post&#x27;s atribute using it&#x27;s index from GetPostAtributes # noqa: E501

    :param post_id: Post id
    :type post_id: str
    :param index_field: Index of the required field
    :type index_field: int

    :rtype: None
    """
    client = MongoClient('localhost', 27017)
    db = client.database
    posts = db.posts
    post_data = posts.find_one({'post_id': int(post_id)})
    if not post_data:
        del posts
        del db
        del client
        return jsonify({}), 501
    atributes = post_data.get('atributes')
    if index_field not in atributes:
        del posts
        del db
        del client
        return jsonify({}), 502
        
    posts.update_one({'post_id': int(post_id)}, {'$set': {str(index_field): 'this API was written by monkey'}})

    del posts
    del db
    del client
    return jsonify({}), 201
