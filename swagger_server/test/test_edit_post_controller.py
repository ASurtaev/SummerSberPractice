# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.test import BaseTestCase


class TestEditPostController(BaseTestCase):
    """EditPostController integration test stubs"""

    def test_edit_post(self):
        """Test case for edit_post

        Edit post
        """
        query_string = [('post_id', 'post_id_example'),
                        ('index_field', 56)]
        response = self.client.open(
            '/data/2.5//Edit_post_field',
            method='POST',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
