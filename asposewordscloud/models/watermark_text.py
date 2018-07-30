# coding: utf-8
# -----------------------------------------------------------------------------------
# <copyright company="Aspose" file="WatermarkText.py">
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


class WatermarkText(object):
    """Class for insert watermark text request building. 
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'text': 'str',
        'rotation_angle': 'float'
    }

    attribute_map = {
        'text': 'Text',
        'rotation_angle': 'RotationAngle'
    }

    def __init__(self, text=None, rotation_angle=None):  # noqa: E501
        """WatermarkText - a model defined in Swagger"""  # noqa: E501

        self._text = None
        self._rotation_angle = None
        self.discriminator = None

        if text is not None:
            self.text = text
        if rotation_angle is not None:
            self.rotation_angle = rotation_angle

    @property
    def text(self):
        """Gets the text of this WatermarkText.  # noqa: E501

        The watermark text.  # noqa: E501

        :return: The text of this WatermarkText.  # noqa: E501
        :rtype: str
        """
        return self._text

    @text.setter
    def text(self, text):
        """Sets the text of this WatermarkText.

        The watermark text.  # noqa: E501

        :param text: The text of this WatermarkText.  # noqa: E501
        :type: str
        """
        self._text = text
    @property
    def rotation_angle(self):
        """Gets the rotation_angle of this WatermarkText.  # noqa: E501

        The watermark rotation angle.  # noqa: E501

        :return: The rotation_angle of this WatermarkText.  # noqa: E501
        :rtype: float
        """
        return self._rotation_angle

    @rotation_angle.setter
    def rotation_angle(self, rotation_angle):
        """Sets the rotation_angle of this WatermarkText.

        The watermark rotation angle.  # noqa: E501

        :param rotation_angle: The rotation_angle of this WatermarkText.  # noqa: E501
        :type: float
        """
        if rotation_angle is None:
            raise ValueError("Invalid value for `rotation_angle`, must not be `None`")  # noqa: E501
        self._rotation_angle = rotation_angle
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
        if not isinstance(other, WatermarkText):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other