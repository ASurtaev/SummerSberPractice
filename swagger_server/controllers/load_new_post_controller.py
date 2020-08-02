import connexion
import six

from swagger_server.models.successfull import Successfull  # noqa: E501
from swagger_server import util


def load_new_post(photo, description_post, tag_post, load_data_time=None, file_size=None, file_size_pixels=None, user_id=None, geolocation=None, file_format=None):  # noqa: E501
    """Loads a new post

    API for loading a new post to the database # noqa: E501

    :param photo: Photo file in string format
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
    :param user_id: Id of the user which has loaded the post
    :type user_id: int
    :param geolocation: Geolocation of the user
    :type geolocation: str
    :param file_format: Format of file like JPEG,PNG,BMP or others
    :type file_format: str

    :rtype: Successfull
    """
    client = MongoClient('localhost', 27017)
    db = client.database
    posts = db.posts
    post_data = {
        'photo': photo,
        'description_post': description_post,
        'tag_post': tag_post
    }
    if load_data_time:
        post_data['load_data_time'] = load_data_time
    if file_size:
        post_data['file_size'] = file_size
    if file_size_pixels:
        post_data['file_size_pixels'] = file_size_pixels
    if geolocation:
        post_data['geolocation'] = geolocation
    if user_id:
        post_data['user_id'] = user_id
    if file_format:
        post_data['file_format'] = file_format

    try:
        result = posts.insert_one(post_data)
    except (Exception,writeConcernError) as ex:
        del post_data
        del posts
        del db
        del client
        return 501

    del post_data
    del posts
    del db
    del client
    return 201
