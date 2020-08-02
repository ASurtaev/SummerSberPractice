import connexion
import six

from swagger_server.models.successfull3 import Successfull3  # noqa: E501
from swagger_server import util


def get_metadata_post(post_id):  # noqa: E501
    """Get metadata post

    API to get the metadata of the post # noqa: E501

    :param post_id: Post id
    :type post_id: str

    :rtype: Successfull3
    """
    return 'do some magic!'
