# coding: utf-8
# -----------------------------------------------------------------------------------
# <copyright company="Aspose" file="SectionLinkCollection.py">
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


class SectionLinkCollection(object):
    """Collection of links to sections
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'link': 'WordsApiLink',
        'section_link_list': 'list[SectionLink]'
    }

    attribute_map = {
        'link': 'link',
        'section_link_list': 'SectionLinkList'
    }

    def __init__(self, link=None, section_link_list=None):  # noqa: E501
        """SectionLinkCollection - a model defined in Swagger"""  # noqa: E501

        self._link = None
        self._section_link_list = None
        self.discriminator = None

        if link is not None:
            self.link = link
        if section_link_list is not None:
            self.section_link_list = section_link_list

    @property
    def link(self):
        """Gets the link of this SectionLinkCollection.  # noqa: E501

        Link to the document.  # noqa: E501

        :return: The link of this SectionLinkCollection.  # noqa: E501
        :rtype: WordsApiLink
        """
        return self._link

    @link.setter
    def link(self, link):
        """Sets the link of this SectionLinkCollection.

        Link to the document.  # noqa: E501

        :param link: The link of this SectionLinkCollection.  # noqa: E501
        :type: WordsApiLink
        """
        self._link = link
    @property
    def section_link_list(self):
        """Gets the section_link_list of this SectionLinkCollection.  # noqa: E501

        Collection of section's links  # noqa: E501

        :return: The section_link_list of this SectionLinkCollection.  # noqa: E501
        :rtype: list[SectionLink]
        """
        return self._section_link_list

    @section_link_list.setter
    def section_link_list(self, section_link_list):
        """Sets the section_link_list of this SectionLinkCollection.

        Collection of section's links  # noqa: E501

        :param section_link_list: The section_link_list of this SectionLinkCollection.  # noqa: E501
        :type: list[SectionLink]
        """
        self._section_link_list = section_link_list
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
        if not isinstance(other, SectionLinkCollection):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other