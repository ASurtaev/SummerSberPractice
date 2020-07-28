import connexion
import six

from swagger_server.models.successfull import Successfull  # noqa: E501
from swagger_server import util


def load_new_post(photo, description_post, tag_post, load_data_time=None, file_size=None, file_size_pixels=None, geolocation=None, user_id=None, mac_adress=None, ip_adress=None, file_format=None):  # noqa: E501
    """Loads a new post

    There is description # noqa: E501

    :param photo: Photo file in base64(?) format
    :type photo: str
    :param description_post: Atributes of post. Post name is always atribute with index 0.
    :type description_post: List[str]
    :param tag_post: Atributes of post
    :type tag_post: List[str]
    :param load_data_time: Time of loading post
    :type load_data_time: str
    :param file_size: Size of the photo file in bytes
    :type file_size: int
    :param file_size_pixels: Size of the photo file in pixels
    :type file_size_pixels: List[int]
    :param geolocation: Geolocation of the user
    :type geolocation: str
    :param user_id: Id of the user
    :type user_id: str
    :param mac_adress: MAC-adress of the user device, from which was loaded the post
    :type mac_adress: str
    :param ip_adress: IP-adress of the user device, from which was loaded the post
    :type ip_adress: str
    :param file_format: Format of file like JPEG,PNG,BMP or others
    :type file_format: str

    :rtype: Successfull
    """
    return 'do some magic!'
