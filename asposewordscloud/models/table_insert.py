# coding: utf-8
# -----------------------------------------------------------------------------------
# <copyright company="Aspose" file="table_insert.py">
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


class TableInsert(object):
    """Table element.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'columns_count': 'int',
        'position': 'DocumentPosition',
        'rows_count': 'int'
    }

    attribute_map = {
        'columns_count': 'ColumnsCount',
        'position': 'Position',
        'rows_count': 'RowsCount'
    }

    def __init__(self, columns_count=None, position=None, rows_count=None):  # noqa: E501
        """TableInsert - a model defined in Swagger"""  # noqa: E501

        self._columns_count = None
        self._position = None
        self._rows_count = None
        self.discriminator = None

        if columns_count is not None:
            self.columns_count = columns_count
        if position is not None:
            self.position = position
        if rows_count is not None:
            self.rows_count = rows_count

    @property
    def columns_count(self):
        """Gets the columns_count of this TableInsert.  # noqa: E501

        Gets or sets count of columns. Default is 2.  # noqa: E501

        :return: The columns_count of this TableInsert.  # noqa: E501
        :rtype: int
        """
        return self._columns_count

    @columns_count.setter
    def columns_count(self, columns_count):
        """Sets the columns_count of this TableInsert.

        Gets or sets count of columns. Default is 2.  # noqa: E501

        :param columns_count: The columns_count of this TableInsert.  # noqa: E501
        :type: int
        """
        self._columns_count = columns_count

    @property
    def position(self):
        """Gets the position of this TableInsert.  # noqa: E501

        Gets or sets table will be inserted before specified position.  # noqa: E501

        :return: The position of this TableInsert.  # noqa: E501
        :rtype: DocumentPosition
        """
        return self._position

    @position.setter
    def position(self, position):
        """Sets the position of this TableInsert.

        Gets or sets table will be inserted before specified position.  # noqa: E501

        :param position: The position of this TableInsert.  # noqa: E501
        :type: DocumentPosition
        """
        self._position = position

    @property
    def rows_count(self):
        """Gets the rows_count of this TableInsert.  # noqa: E501

        Gets or sets count of rows. Default is 2.  # noqa: E501

        :return: The rows_count of this TableInsert.  # noqa: E501
        :rtype: int
        """
        return self._rows_count

    @rows_count.setter
    def rows_count(self, rows_count):
        """Sets the rows_count of this TableInsert.

        Gets or sets count of rows. Default is 2.  # noqa: E501

        :param rows_count: The rows_count of this TableInsert.  # noqa: E501
        :type: int
        """
        self._rows_count = rows_count


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
        if not isinstance(other, TableInsert):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other