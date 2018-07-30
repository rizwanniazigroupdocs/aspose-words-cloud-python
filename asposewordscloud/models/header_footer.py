# coding: utf-8
# -----------------------------------------------------------------------------------
# <copyright company="Aspose" file="HeaderFooter.py">
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


class HeaderFooter(object):
    """Section element
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
        'type': 'str',
        'drawing_objects': 'LinkElement',
        'paragraphs': 'LinkElement'
    }

    attribute_map = {
        'link': 'link',
        'type': 'Type',
        'drawing_objects': 'DrawingObjects',
        'paragraphs': 'Paragraphs'
    }

    def __init__(self, link=None, type=None, drawing_objects=None, paragraphs=None):  # noqa: E501
        """HeaderFooter - a model defined in Swagger"""  # noqa: E501

        self._link = None
        self._type = None
        self._drawing_objects = None
        self._paragraphs = None
        self.discriminator = None

        if link is not None:
            self.link = link
        if type is not None:
            self.type = type
        if drawing_objects is not None:
            self.drawing_objects = drawing_objects
        if paragraphs is not None:
            self.paragraphs = paragraphs

    @property
    def link(self):
        """Gets the link of this HeaderFooter.  # noqa: E501

        Link to the document.  # noqa: E501

        :return: The link of this HeaderFooter.  # noqa: E501
        :rtype: WordsApiLink
        """
        return self._link

    @link.setter
    def link(self, link):
        """Sets the link of this HeaderFooter.

        Link to the document.  # noqa: E501

        :param link: The link of this HeaderFooter.  # noqa: E501
        :type: WordsApiLink
        """
        self._link = link
    @property
    def type(self):
        """Gets the type of this HeaderFooter.  # noqa: E501

        Paragraph's text  # noqa: E501

        :return: The type of this HeaderFooter.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this HeaderFooter.

        Paragraph's text  # noqa: E501

        :param type: The type of this HeaderFooter.  # noqa: E501
        :type: str
        """
        allowed_values = ["HeaderEven", "HeaderPrimary", "FooterEven", "FooterPrimary", "HeaderFirst", "FooterFirst"]  # noqa: E501
        if not type.isdigit():	
            if type not in allowed_values:
                raise ValueError(
                    "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                    .format(type, allowed_values))
            self._type = type
        else:
            self._type = allowed_values[int(type) if six.PY3 else long(type)]
    @property
    def drawing_objects(self):
        """Gets the drawing_objects of this HeaderFooter.  # noqa: E501

        Link to DrawingObjects resource  # noqa: E501

        :return: The drawing_objects of this HeaderFooter.  # noqa: E501
        :rtype: LinkElement
        """
        return self._drawing_objects

    @drawing_objects.setter
    def drawing_objects(self, drawing_objects):
        """Sets the drawing_objects of this HeaderFooter.

        Link to DrawingObjects resource  # noqa: E501

        :param drawing_objects: The drawing_objects of this HeaderFooter.  # noqa: E501
        :type: LinkElement
        """
        self._drawing_objects = drawing_objects
    @property
    def paragraphs(self):
        """Gets the paragraphs of this HeaderFooter.  # noqa: E501

        Link to Paragraphs resource  # noqa: E501

        :return: The paragraphs of this HeaderFooter.  # noqa: E501
        :rtype: LinkElement
        """
        return self._paragraphs

    @paragraphs.setter
    def paragraphs(self, paragraphs):
        """Sets the paragraphs of this HeaderFooter.

        Link to Paragraphs resource  # noqa: E501

        :param paragraphs: The paragraphs of this HeaderFooter.  # noqa: E501
        :type: LinkElement
        """
        self._paragraphs = paragraphs
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
        if not isinstance(other, HeaderFooter):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
