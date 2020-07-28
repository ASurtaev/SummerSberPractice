# coding: utf-8

"""
    CONTENT MANAGEMENT API

    CONTENT MANAGEMENT  # noqa: E501

    OpenAPI spec version: 0.1 beta
    Contact: some_email@gmail.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six


class Successfull1(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'atributes': 'list[str]',
        'result': 'bool'
    }

    attribute_map = {
        'atributes': 'Atributes',
        'result': 'Result'
    }

    def __init__(self, atributes=None, result=None):  # noqa: E501
        """Successfull1 - a model defined in Swagger"""  # noqa: E501
        self._atributes = None
        self._result = None
        self.discriminator = None
        if atributes is not None:
            self.atributes = atributes
        if result is not None:
            self.result = result

    @property
    def atributes(self):
        """Gets the atributes of this Successfull1.  # noqa: E501


        :return: The atributes of this Successfull1.  # noqa: E501
        :rtype: list[str]
        """
        return self._atributes

    @atributes.setter
    def atributes(self, atributes):
        """Sets the atributes of this Successfull1.


        :param atributes: The atributes of this Successfull1.  # noqa: E501
        :type: list[str]
        """

        self._atributes = atributes

    @property
    def result(self):
        """Gets the result of this Successfull1.  # noqa: E501


        :return: The result of this Successfull1.  # noqa: E501
        :rtype: bool
        """
        return self._result

    @result.setter
    def result(self, result):
        """Sets the result of this Successfull1.


        :param result: The result of this Successfull1.  # noqa: E501
        :type: bool
        """

        self._result = result

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(Successfull1, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Successfull1):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
