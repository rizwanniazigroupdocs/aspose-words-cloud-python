# coding: utf-8
# -----------------------------------------------------------------------------------
# <copyright company="Aspose" file="CompareData.py">
#   Copyright (c) 2019 Aspose.Words for Cloud
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


class CompareData(object):
    """Container class for compare documents.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'comparing_with_document': 'str',
        'author': 'str',
        'date_time': 'datetime'
    }

    attribute_map = {
        'comparing_with_document': 'ComparingWithDocument',
        'author': 'Author',
        'date_time': 'DateTime'
    }

    def __init__(self, comparing_with_document=None, author=None, date_time=None):  # noqa: E501
        """CompareData - a model defined in Swagger"""  # noqa: E501

        self._comparing_with_document = None
        self._author = None
        self._date_time = None
        self.discriminator = None

        if comparing_with_document is not None:
            self.comparing_with_document = comparing_with_document
        if author is not None:
            self.author = author
        if date_time is not None:
            self.date_time = date_time

    @property
    def comparing_with_document(self):
        """Gets the comparing_with_document of this CompareData.  # noqa: E501

        Gets or sets path to document to compare at the server.  # noqa: E501

        :return: The comparing_with_document of this CompareData.  # noqa: E501
        :rtype: str
        """
        return self._comparing_with_document

    @comparing_with_document.setter
    def comparing_with_document(self, comparing_with_document):
        """Sets the comparing_with_document of this CompareData.

        Gets or sets path to document to compare at the server.  # noqa: E501

        :param comparing_with_document: The comparing_with_document of this CompareData.  # noqa: E501
        :type: str
        """
        self._comparing_with_document = comparing_with_document
    @property
    def author(self):
        """Gets the author of this CompareData.  # noqa: E501

        Gets or sets initials of the author to use for revisions.  # noqa: E501

        :return: The author of this CompareData.  # noqa: E501
        :rtype: str
        """
        return self._author

    @author.setter
    def author(self, author):
        """Sets the author of this CompareData.

        Gets or sets initials of the author to use for revisions.  # noqa: E501

        :param author: The author of this CompareData.  # noqa: E501
        :type: str
        """
        self._author = author
    @property
    def date_time(self):
        """Gets the date_time of this CompareData.  # noqa: E501

        Gets or sets the date and time to use for revisions.               # noqa: E501

        :return: The date_time of this CompareData.  # noqa: E501
        :rtype: datetime
        """
        return self._date_time

    @date_time.setter
    def date_time(self, date_time):
        """Sets the date_time of this CompareData.

        Gets or sets the date and time to use for revisions.               # noqa: E501

        :param date_time: The date_time of this CompareData.  # noqa: E501
        :type: datetime
        """
        self._date_time = date_time
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
        if not isinstance(other, CompareData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
