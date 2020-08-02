# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.test import BaseTestCase


class TestDeletePostController(BaseTestCase):
    """DeletePostController integration test stubs"""

    def test_delete_post(self):
        """Test case for delete_post

        Delete post
        """
        query_string = [('post_id', 'post_id_example')]
        response = self.client.open(
            '/data/2.5//Delete_post',
            method='DELETE',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
