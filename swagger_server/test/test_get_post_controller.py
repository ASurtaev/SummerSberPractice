# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.successfull2 import Successfull2  # noqa: E501
from swagger_server.test import BaseTestCase


class TestGetPostController(BaseTestCase):
    """GetPostController integration test stubs"""

    def test_get_post(self):
        """Test case for get_post

        Get post
        """
        query_string = [('post_id', 'post_id_example')]
        response = self.client.open(
            '/data/2.5//Get_post',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
