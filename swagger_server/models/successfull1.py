# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class Successfull1(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, name: str=None, atributes: List[str]=None, tag: List[str]=None):  # noqa: E501
        """Successfull1 - a model defined in Swagger

        :param name: The name of this Successfull1.  # noqa: E501
        :type name: str
        :param atributes: The atributes of this Successfull1.  # noqa: E501
        :type atributes: List[str]
        :param tag: The tag of this Successfull1.  # noqa: E501
        :type tag: List[str]
        """
        self.swagger_types = {
            'name': str,
            'atributes': List[str],
            'tag': List[str]
        }

        self.attribute_map = {
            'name': 'Name',
            'atributes': 'Atributes',
            'tag': 'Tag'
        }
        self._name = name
        self._atributes = atributes
        self._tag = tag

    @classmethod
    def from_dict(cls, dikt) -> 'Successfull1':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Successfull_1 of this Successfull1.  # noqa: E501
        :rtype: Successfull1
        """
        return util.deserialize_model(dikt, cls)

    @property
    def name(self) -> str:
        """Gets the name of this Successfull1.


        :return: The name of this Successfull1.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name: str):
        """Sets the name of this Successfull1.


        :param name: The name of this Successfull1.
        :type name: str
        """

        self._name = name

    @property
    def atributes(self) -> List[str]:
        """Gets the atributes of this Successfull1.


        :return: The atributes of this Successfull1.
        :rtype: List[str]
        """
        return self._atributes

    @atributes.setter
    def atributes(self, atributes: List[str]):
        """Sets the atributes of this Successfull1.


        :param atributes: The atributes of this Successfull1.
        :type atributes: List[str]
        """

        self._atributes = atributes

    @property
    def tag(self) -> List[str]:
        """Gets the tag of this Successfull1.


        :return: The tag of this Successfull1.
        :rtype: List[str]
        """
        return self._tag

    @tag.setter
    def tag(self, tag: List[str]):
        """Sets the tag of this Successfull1.


        :param tag: The tag of this Successfull1.
        :type tag: List[str]
        """

        self._tag = tag
