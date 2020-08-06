import connexion
import six

from pymongo import MongoClient
from flask import jsonify


from swagger_server import util


def delete_post(post_id):  # noqa: E501
    """Delete post

    API to delete the post from database # noqa: E501

    :param post_id: Post id
    :type post_id: str

    :rtype: str
    """
    client = MongoClient('localhost', 27017)
    db = client.database
    posts = db.posts
    
    try:
    	posts.delete_one({'post_id': post_id})
    except Exception as e:
    	print('Exception:', e)
    	del posts
    	del db
    	del client
    	return jsonify({}), 501
    del posts
    del db
    del client
    return jsonify({}), 201

