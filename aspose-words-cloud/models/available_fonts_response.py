# coding: utf-8
# -----------------------------------------------------------------------------------
# <copyright company="Aspose" file="AvailableFontsResponse.py">
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


class AvailableFontsResponse(object):
    """The list of fonts, available for document processing
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'code': 'int',
        'status': 'str',
        'additional_fonts': 'list[FontInfo]',
        'custom_fonts': 'list[FontInfo]',
        'system_fonts': 'list[FontInfo]'
    }

    attribute_map = {
        'code': 'Code',
        'status': 'Status',
        'additional_fonts': 'AdditionalFonts',
        'custom_fonts': 'CustomFonts',
        'system_fonts': 'SystemFonts'
    }

    def __init__(self, code=None, status=None, additional_fonts=None, custom_fonts=None, system_fonts=None):  # noqa: E501
        """AvailableFontsResponse - a model defined in Swagger"""  # noqa: E501

        self._code = None
        self._status = None
        self._additional_fonts = None
        self._custom_fonts = None
        self._system_fonts = None
        self.discriminator = None

        if code is not None:
            self.code = code
        if status is not None:
            self.status = status
        if additional_fonts is not None:
            self.additional_fonts = additional_fonts
        if custom_fonts is not None:
            self.custom_fonts = custom_fonts
        if system_fonts is not None:
            self.system_fonts = system_fonts

    @property
    def code(self):
        """Gets the code of this AvailableFontsResponse.  # noqa: E501

        Response status code.  # noqa: E501

        :return: The code of this AvailableFontsResponse.  # noqa: E501
        :rtype: int
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this AvailableFontsResponse.

        Response status code.  # noqa: E501

        :param code: The code of this AvailableFontsResponse.  # noqa: E501
        :type: int
        """
        if code is None:
            raise ValueError("Invalid value for `code`, must not be `None`")  # noqa: E501
        self._code = code
    @property
    def status(self):
        """Gets the status of this AvailableFontsResponse.  # noqa: E501

        Response status.  # noqa: E501

        :return: The status of this AvailableFontsResponse.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this AvailableFontsResponse.

        Response status.  # noqa: E501

        :param status: The status of this AvailableFontsResponse.  # noqa: E501
        :type: str
        """
        self._status = status
    @property
    def additional_fonts(self):
        """Gets the additional_fonts of this AvailableFontsResponse.  # noqa: E501

        The list of addititional fonts, provided by aspose team  # noqa: E501

        :return: The additional_fonts of this AvailableFontsResponse.  # noqa: E501
        :rtype: list[FontInfo]
        """
        return self._additional_fonts

    @additional_fonts.setter
    def additional_fonts(self, additional_fonts):
        """Sets the additional_fonts of this AvailableFontsResponse.

        The list of addititional fonts, provided by aspose team  # noqa: E501

        :param additional_fonts: The additional_fonts of this AvailableFontsResponse.  # noqa: E501
        :type: list[FontInfo]
        """
        self._additional_fonts = additional_fonts
    @property
    def custom_fonts(self):
        """Gets the custom_fonts of this AvailableFontsResponse.  # noqa: E501

        Custom user fonts (from user file storage). To use them, you should specify \"fontsLocation\" parameter in any request  # noqa: E501

        :return: The custom_fonts of this AvailableFontsResponse.  # noqa: E501
        :rtype: list[FontInfo]
        """
        return self._custom_fonts

    @custom_fonts.setter
    def custom_fonts(self, custom_fonts):
        """Sets the custom_fonts of this AvailableFontsResponse.

        Custom user fonts (from user file storage). To use them, you should specify \"fontsLocation\" parameter in any request  # noqa: E501

        :param custom_fonts: The custom_fonts of this AvailableFontsResponse.  # noqa: E501
        :type: list[FontInfo]
        """
        self._custom_fonts = custom_fonts
    @property
    def system_fonts(self):
        """Gets the system_fonts of this AvailableFontsResponse.  # noqa: E501

        The list of system fonts, availiable on the server  # noqa: E501

        :return: The system_fonts of this AvailableFontsResponse.  # noqa: E501
        :rtype: list[FontInfo]
        """
        return self._system_fonts

    @system_fonts.setter
    def system_fonts(self, system_fonts):
        """Sets the system_fonts of this AvailableFontsResponse.

        The list of system fonts, availiable on the server  # noqa: E501

        :param system_fonts: The system_fonts of this AvailableFontsResponse.  # noqa: E501
        :type: list[FontInfo]
        """
        self._system_fonts = system_fonts
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
        if not isinstance(other, AvailableFontsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
