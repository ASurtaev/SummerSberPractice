# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.successfull import Successfull  # noqa: E501
from swagger_server.test import BaseTestCase


class TestLoadNewPostController(BaseTestCase):
    """LoadNewPostController integration test stubs"""

    def test_load_new_post(self):
        """Test case for load_new_post

        Loads a new post
        """
        query_string = [('photo', 'photo_example'),
                        ('post_name', 'post_name_example'),
                        ('post_atributes', 'post_atributes_example'),
                        ('tag_post', 'tag_post_example'),
                        ('load_data_time', 'load_data_time_example'),
                        ('file_size', 56),
                        ('file_size_pixels', 56),
                        ('user_id', 56),
                        ('geolocation', 'geolocation_example'),
                        ('file_format', 'file_format_example')]
        response = self.client.open(
            '/data/2.5//Load_new_post',
            method='POST',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
