import connexion
import six
import pprint

from swagger_server.models.successfull2 import Successfull2  # noqa: E501
from swagger_server import util


def get_post(post_id):  # noqa: E501
    """Get post

    Get post by it&#x27;s atributes # noqa: E501

    :param post_id: Post id
    :type post_id: str

    :rtype: Successfull2
    """
    client = MongoClient('localhost', 27017)
    db = client.database
    posts = db.posts
    post_data = posts.find_one({"_id": post_id})
    if post_data:
    	pprint.pprint(post_data)
    	post_data.pop("_id")
    	return (201, post_data)
    return (501, -1)
