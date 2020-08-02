# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.successfull3 import Successfull3  # noqa: E501
from swagger_server.test import BaseTestCase


class TestGetMetadataPostController(BaseTestCase):
    """GetMetadataPostController integration test stubs"""

    def test_get_metadata_post(self):
        """Test case for get_metadata_post

        Get metadata post
        """
        query_string = [('post_id', 'post_id_example')]
        response = self.client.open(
            '/data/2.5//Get_metadata_post',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
