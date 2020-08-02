# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.successfull1 import Successfull1  # noqa: E501
from swagger_server.test import BaseTestCase


class TestGetPostAtributesController(BaseTestCase):
    """GetPostAtributesController integration test stubs"""

    def test_get_post_atributes(self):
        """Test case for get_post_atributes

        Get post atributes
        """
        query_string = [('post_id', 'post_id_example')]
        response = self.client.open(
            '/Get_post_atributes',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
