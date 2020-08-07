import connexion
import six
from pymongo import MongoClient
from flask import jsonify

from swagger_server import util


def edit_post(post_id, attribute_name, new_value):  # noqa: E501
    """Edit post

    Using GetPostAtributes, a list of atributes is called and the user chooses which atribute he needs to name # noqa: E501

    :param post_id: Post id
    :type post_id: str
    :param attribute_name: Attribute name
    :type attribute_name: str
    :param new_value: New value of the attribute
    :type new_value: str

    :rtype: str
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
    attributes = post_data.get('post_attributes')
    if attribute_name not in attributes:
        del posts
        del db
        del client
        return jsonify({}), 502
        
    posts.update_one({'post_id': int(post_id)}, {'$set': {str(attribute_name): new_value}})

    del posts
    del db
    del client
    return jsonify({}), 201

