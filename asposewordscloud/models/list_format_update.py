# coding: utf-8
# -----------------------------------------------------------------------------------
# <copyright company="Aspose" file="list_format_update.py">
#   Copyright (c) 2020 Aspose.Words for Cloud
# </copyright>
# <summary>
#   Permission is hereby granted, free of charge, to any person obtaining a copy
#  of this software and associated documentation files (the "Software"), to deal
#  in the Software without restriction, including without limitation the rights
#  to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#  copies of the Software, and to permit persons to whom the Software is
#  furnished to do so, subject to the following conditions:
#
#  The above copyright notice and this permission notice shall be included in all
#  copies or substantial portions of the Software.
#
#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#  IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#  OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#  SOFTWARE.
# </summary>
# -----------------------------------------------------------------------------------
import pprint
import re  # noqa: F401

import six


class ListFormatUpdate(object):
    """Paragraph list format element for update.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'list_id': 'int',
        'list_level_number': 'int'
    }

    attribute_map = {
        'list_id': 'ListId',
        'list_level_number': 'ListLevelNumber'
    }

    def __init__(self, list_id=None, list_level_number=None):  # noqa: E501
        """ListFormatUpdate - a model defined in Swagger"""  # noqa: E501

        self._list_id = None
        self._list_level_number = None
        self.discriminator = None

        if list_id is not None:
            self.list_id = list_id
        if list_level_number is not None:
            self.list_level_number = list_level_number

    @property
    def list_id(self):
        """Gets the list_id of this ListFormatUpdate.  # noqa: E501

        Gets or sets the list id of this paragraph.  # noqa: E501

        :return: The list_id of this ListFormatUpdate.  # noqa: E501
        :rtype: int
        """
        return self._list_id

    @list_id.setter
    def list_id(self, list_id):
        """Sets the list_id of this ListFormatUpdate.

        Gets or sets the list id of this paragraph.  # noqa: E501

        :param list_id: The list_id of this ListFormatUpdate.  # noqa: E501
        :type: int
        """
        self._list_id = list_id

    @property
    def list_level_number(self):
        """Gets the list_level_number of this ListFormatUpdate.  # noqa: E501

        Gets or sets the list level number (0 to 8) for the paragraph.  # noqa: E501

        :return: The list_level_number of this ListFormatUpdate.  # noqa: E501
        :rtype: int
        """
        return self._list_level_number

    @list_level_number.setter
    def list_level_number(self, list_level_number):
        """Sets the list_level_number of this ListFormatUpdate.

        Gets or sets the list level number (0 to 8) for the paragraph.  # noqa: E501

        :param list_level_number: The list_level_number of this ListFormatUpdate.  # noqa: E501
        :type: int
        """
        self._list_level_number = list_level_number


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

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ListFormatUpdate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other