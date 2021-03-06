# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class Successfull(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, post_id: int=None, result: bool=None):  # noqa: E501
        """Successfull - a model defined in Swagger

        :param post_id: The post_id of this Successfull.  # noqa: E501
        :type post_id: int
        :param result: The result of this Successfull.  # noqa: E501
        :type result: bool
        """
        self.swagger_types = {
            'post_id': int,
            'result': bool
        }

        self.attribute_map = {
            'post_id': 'PostID',
            'result': 'Result'
        }
        self._post_id = post_id
        self._result = result

    @classmethod
    def from_dict(cls, dikt) -> 'Successfull':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Successfull of this Successfull.  # noqa: E501
        :rtype: Successfull
        """
        return util.deserialize_model(dikt, cls)

    @property
    def post_id(self) -> int:
        """Gets the post_id of this Successfull.


        :return: The post_id of this Successfull.
        :rtype: int
        """
        return self._post_id

    @post_id.setter
    def post_id(self, post_id: int):
        """Sets the post_id of this Successfull.


        :param post_id: The post_id of this Successfull.
        :type post_id: int
        """

        self._post_id = post_id

    @property
    def result(self) -> bool:
        """Gets the result of this Successfull.


        :return: The result of this Successfull.
        :rtype: bool
        """
        return self._result

    @result.setter
    def result(self, result: bool):
        """Sets the result of this Successfull.


        :param result: The result of this Successfull.
        :type result: bool
        """

        self._result = result
