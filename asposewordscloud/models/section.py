# coding: utf-8
# -----------------------------------------------------------------------------------
# <copyright company="Aspose" file="Section.py">
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


class Section(object):
    """Section element.
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
        'child_nodes': 'list[NodeLink]',
        'header_footers': 'LinkElement',
        'page_setup': 'LinkElement',
        'paragraphs': 'LinkElement',
        'tables': 'LinkElement'
    }

    attribute_map = {
        'link': 'link',
        'child_nodes': 'ChildNodes',
        'header_footers': 'HeaderFooters',
        'page_setup': 'PageSetup',
        'paragraphs': 'Paragraphs',
        'tables': 'Tables'
    }

    def __init__(self, link=None, child_nodes=None, header_footers=None, page_setup=None, paragraphs=None, tables=None):  # noqa: E501
        """Section - a model defined in Swagger"""  # noqa: E501

        self._link = None
        self._child_nodes = None
        self._header_footers = None
        self._page_setup = None
        self._paragraphs = None
        self._tables = None
        self.discriminator = None

        if link is not None:
            self.link = link
        if child_nodes is not None:
            self.child_nodes = child_nodes
        if header_footers is not None:
            self.header_footers = header_footers
        if page_setup is not None:
            self.page_setup = page_setup
        if paragraphs is not None:
            self.paragraphs = paragraphs
        if tables is not None:
            self.tables = tables

    @property
    def link(self):
        """Gets the link of this Section.  # noqa: E501

        Gets or sets link.  # noqa: E501

        :return: The link of this Section.  # noqa: E501
        :rtype: WordsApiLink
        """
        return self._link

    @link.setter
    def link(self, link):
        """Sets the link of this Section.

        Gets or sets link.  # noqa: E501

        :param link: The link of this Section.  # noqa: E501
        :type: WordsApiLink
        """
        self._link = link
    @property
    def child_nodes(self):
        """Gets the child_nodes of this Section.  # noqa: E501

        Gets or sets child nodes.  # noqa: E501

        :return: The child_nodes of this Section.  # noqa: E501
        :rtype: list[NodeLink]
        """
        return self._child_nodes

    @child_nodes.setter
    def child_nodes(self, child_nodes):
        """Sets the child_nodes of this Section.

        Gets or sets child nodes.  # noqa: E501

        :param child_nodes: The child_nodes of this Section.  # noqa: E501
        :type: list[NodeLink]
        """
        self._child_nodes = child_nodes
    @property
    def header_footers(self):
        """Gets the header_footers of this Section.  # noqa: E501

        Gets or sets header_footers.  # noqa: E501

        :return: The header_footers of this Section.  # noqa: E501
        :rtype: LinkElement
        """
        return self._header_footers

    @header_footers.setter
    def header_footers(self, header_footers):
        """Sets the header_footers of this Section.

        Gets or sets header_footers.  # noqa: E501

        :param header_footers: The header_footers of this Section.  # noqa: E501
        :type: LinkElement
        """
        self._header_footers = header_footers
    @property
    def page_setup(self):
        """Gets the page_setup of this Section.  # noqa: E501

        Gets or sets page_setup.  # noqa: E501

        :return: The page_setup of this Section.  # noqa: E501
        :rtype: LinkElement
        """
        return self._page_setup

    @page_setup.setter
    def page_setup(self, page_setup):
        """Sets the page_setup of this Section.

        Gets or sets page_setup.  # noqa: E501

        :param page_setup: The page_setup of this Section.  # noqa: E501
        :type: LinkElement
        """
        self._page_setup = page_setup
    @property
    def paragraphs(self):
        """Gets the paragraphs of this Section.  # noqa: E501

        Gets or sets paragraphs.  # noqa: E501

        :return: The paragraphs of this Section.  # noqa: E501
        :rtype: LinkElement
        """
        return self._paragraphs

    @paragraphs.setter
    def paragraphs(self, paragraphs):
        """Sets the paragraphs of this Section.

        Gets or sets paragraphs.  # noqa: E501

        :param paragraphs: The paragraphs of this Section.  # noqa: E501
        :type: LinkElement
        """
        self._paragraphs = paragraphs
    @property
    def tables(self):
        """Gets the tables of this Section.  # noqa: E501

        Gets or sets tables.  # noqa: E501

        :return: The tables of this Section.  # noqa: E501
        :rtype: LinkElement
        """
        return self._tables

    @tables.setter
    def tables(self, tables):
        """Sets the tables of this Section.

        Gets or sets tables.  # noqa: E501

        :param tables: The tables of this Section.  # noqa: E501
        :type: LinkElement
        """
        self._tables = tables
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
        if not isinstance(other, Section):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
