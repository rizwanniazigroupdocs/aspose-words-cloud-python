# coding: utf-8
# -----------------------------------------------------------------------------------
# <copyright company="Aspose" file="PageNumber.py">
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


class PageNumber(object):
    """Class is used for insert page number request building.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'format': 'str',
        'alignment': 'str',
        'is_top': 'bool',
        'set_page_number_on_first_page': 'bool'
    }

    attribute_map = {
        'format': 'format',
        'alignment': 'alignment',
        'is_top': 'isTop',
        'set_page_number_on_first_page': 'setPageNumberOnFirstPage'
    }

    def __init__(self, format=None, alignment=None, is_top=None, set_page_number_on_first_page=None):  # noqa: E501
        """PageNumber - a model defined in Swagger"""  # noqa: E501

        self._format = None
        self._alignment = None
        self._is_top = None
        self._set_page_number_on_first_page = None
        self.discriminator = None

        if format is not None:
            self.format = format
        if alignment is not None:
            self.alignment = alignment
        if is_top is not None:
            self.is_top = is_top
        if set_page_number_on_first_page is not None:
            self.set_page_number_on_first_page = set_page_number_on_first_page

    @property
    def format(self):
        """Gets the format of this PageNumber.  # noqa: E501

        Gets or sets page number format, e.g. \"{PAGE} of {NUMPAGES}\".  # noqa: E501

        :return: The format of this PageNumber.  # noqa: E501
        :rtype: str
        """
        return self._format

    @format.setter
    def format(self, format):
        """Sets the format of this PageNumber.

        Gets or sets page number format, e.g. \"{PAGE} of {NUMPAGES}\".  # noqa: E501

        :param format: The format of this PageNumber.  # noqa: E501
        :type: str
        """
        self._format = format
    @property
    def alignment(self):
        """Gets the alignment of this PageNumber.  # noqa: E501

        Gets or sets text alignment, possible values are left, right, center or justify.  # noqa: E501

        :return: The alignment of this PageNumber.  # noqa: E501
        :rtype: str
        """
        return self._alignment

    @alignment.setter
    def alignment(self, alignment):
        """Sets the alignment of this PageNumber.

        Gets or sets text alignment, possible values are left, right, center or justify.  # noqa: E501

        :param alignment: The alignment of this PageNumber.  # noqa: E501
        :type: str
        """
        self._alignment = alignment
    @property
    def is_top(self):
        """Gets the is_top of this PageNumber.  # noqa: E501

        Gets or sets a value indicating whether if true the page number is added at the top of the page, else at the bottom.  # noqa: E501

        :return: The is_top of this PageNumber.  # noqa: E501
        :rtype: bool
        """
        return self._is_top

    @is_top.setter
    def is_top(self, is_top):
        """Sets the is_top of this PageNumber.

        Gets or sets a value indicating whether if true the page number is added at the top of the page, else at the bottom.  # noqa: E501

        :param is_top: The is_top of this PageNumber.  # noqa: E501
        :type: bool
        """
        if is_top is None:
            raise ValueError("Invalid value for `is_top`, must not be `None`")  # noqa: E501
        self._is_top = is_top
    @property
    def set_page_number_on_first_page(self):
        """Gets the set_page_number_on_first_page of this PageNumber.  # noqa: E501

        Gets or sets a value indicating whether if true the page number is added on first page too.  # noqa: E501

        :return: The set_page_number_on_first_page of this PageNumber.  # noqa: E501
        :rtype: bool
        """
        return self._set_page_number_on_first_page

    @set_page_number_on_first_page.setter
    def set_page_number_on_first_page(self, set_page_number_on_first_page):
        """Sets the set_page_number_on_first_page of this PageNumber.

        Gets or sets a value indicating whether if true the page number is added on first page too.  # noqa: E501

        :param set_page_number_on_first_page: The set_page_number_on_first_page of this PageNumber.  # noqa: E501
        :type: bool
        """
        if set_page_number_on_first_page is None:
            raise ValueError("Invalid value for `set_page_number_on_first_page`, must not be `None`")  # noqa: E501
        self._set_page_number_on_first_page = set_page_number_on_first_page
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
        if not isinstance(other, PageNumber):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
