# coding: utf-8
# -----------------------------------------------------------------------------------
# <copyright company="Aspose" file="XpsSaveOptionsData.py">
#   Copyright (c) 2018 Aspose.Words for Cloud
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


class XpsSaveOptionsData(object):
    """Container class for xps save options.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'bookmarks_outline_level': 'int',
        'headings_outline_levels': 'int',
        'outline_options': 'OutlineOptionsData',
        'use_book_fold_printing_settings': 'bool'
    }

    attribute_map = {
        'bookmarks_outline_level': 'BookmarksOutlineLevel',
        'headings_outline_levels': 'HeadingsOutlineLevels',
        'outline_options': 'OutlineOptions',
        'use_book_fold_printing_settings': 'UseBookFoldPrintingSettings'
    }

    def __init__(self, bookmarks_outline_level=None, headings_outline_levels=None, outline_options=None, use_book_fold_printing_settings=None):  # noqa: E501
        """XpsSaveOptionsData - a model defined in Swagger"""  # noqa: E501

        self._bookmarks_outline_level = None
        self._headings_outline_levels = None
        self._outline_options = None
        self._use_book_fold_printing_settings = None
        self.discriminator = None

        if bookmarks_outline_level is not None:
            self.bookmarks_outline_level = bookmarks_outline_level
        if headings_outline_levels is not None:
            self.headings_outline_levels = headings_outline_levels
        if outline_options is not None:
            self.outline_options = outline_options
        if use_book_fold_printing_settings is not None:
            self.use_book_fold_printing_settings = use_book_fold_printing_settings

    @property
    def bookmarks_outline_level(self):
        """Gets the bookmarks_outline_level of this XpsSaveOptionsData.  # noqa: E501

        Specifies the level in the XPS document outline at which to display Word bookmarks.  # noqa: E501

        :return: The bookmarks_outline_level of this XpsSaveOptionsData.  # noqa: E501
        :rtype: int
        """
        return self._bookmarks_outline_level

    @bookmarks_outline_level.setter
    def bookmarks_outline_level(self, bookmarks_outline_level):
        """Sets the bookmarks_outline_level of this XpsSaveOptionsData.

        Specifies the level in the XPS document outline at which to display Word bookmarks.  # noqa: E501

        :param bookmarks_outline_level: The bookmarks_outline_level of this XpsSaveOptionsData.  # noqa: E501
        :type: int
        """

        self._bookmarks_outline_level = bookmarks_outline_level

    @property
    def headings_outline_levels(self):
        """Gets the headings_outline_levels of this XpsSaveOptionsData.  # noqa: E501

        Specifies how many levels of headings (paragraphs formatted with the Heading styles) to include in the XPS document outline.  # noqa: E501

        :return: The headings_outline_levels of this XpsSaveOptionsData.  # noqa: E501
        :rtype: int
        """
        return self._headings_outline_levels

    @headings_outline_levels.setter
    def headings_outline_levels(self, headings_outline_levels):
        """Sets the headings_outline_levels of this XpsSaveOptionsData.

        Specifies how many levels of headings (paragraphs formatted with the Heading styles) to include in the XPS document outline.  # noqa: E501

        :param headings_outline_levels: The headings_outline_levels of this XpsSaveOptionsData.  # noqa: E501
        :type: int
        """

        self._headings_outline_levels = headings_outline_levels

    @property
    def outline_options(self):
        """Gets the outline_options of this XpsSaveOptionsData.  # noqa: E501

        Allows to specify outline options  # noqa: E501

        :return: The outline_options of this XpsSaveOptionsData.  # noqa: E501
        :rtype: OutlineOptionsData
        """
        return self._outline_options

    @outline_options.setter
    def outline_options(self, outline_options):
        """Sets the outline_options of this XpsSaveOptionsData.

        Allows to specify outline options  # noqa: E501

        :param outline_options: The outline_options of this XpsSaveOptionsData.  # noqa: E501
        :type: OutlineOptionsData
        """

        self._outline_options = outline_options

    @property
    def use_book_fold_printing_settings(self):
        """Gets the use_book_fold_printing_settings of this XpsSaveOptionsData.  # noqa: E501

        Determines whether the document should be saved using a booklet printing layout  # noqa: E501

        :return: The use_book_fold_printing_settings of this XpsSaveOptionsData.  # noqa: E501
        :rtype: bool
        """
        return self._use_book_fold_printing_settings

    @use_book_fold_printing_settings.setter
    def use_book_fold_printing_settings(self, use_book_fold_printing_settings):
        """Sets the use_book_fold_printing_settings of this XpsSaveOptionsData.

        Determines whether the document should be saved using a booklet printing layout  # noqa: E501

        :param use_book_fold_printing_settings: The use_book_fold_printing_settings of this XpsSaveOptionsData.  # noqa: E501
        :type: bool
        """

        self._use_book_fold_printing_settings = use_book_fold_printing_settings

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
        if not isinstance(other, XpsSaveOptionsData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
