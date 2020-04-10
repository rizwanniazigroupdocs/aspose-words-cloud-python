# coding: utf-8
# -----------------------------------------------------------------------------------
# <copyright company="Aspose" file="ListLevel.py">
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


class ListLevel(object):
    """Represents a document list levels.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'start_at': 'int',
        'number_style': 'str',
        'number_format': 'str',
        'alignment': 'str',
        'is_legal': 'bool',
        'restart_after_level': 'int',
        'trailing_character': 'str',
        'font': 'Font',
        'tab_position': 'float',
        'number_position': 'float',
        'text_position': 'float',
        'linked_style': 'Style'
    }

    attribute_map = {
        'start_at': 'StartAt',
        'number_style': 'NumberStyle',
        'number_format': 'NumberFormat',
        'alignment': 'Alignment',
        'is_legal': 'IsLegal',
        'restart_after_level': 'RestartAfterLevel',
        'trailing_character': 'TrailingCharacter',
        'font': 'Font',
        'tab_position': 'TabPosition',
        'number_position': 'NumberPosition',
        'text_position': 'TextPosition',
        'linked_style': 'LinkedStyle'
    }

    def __init__(self, start_at=None, number_style=None, number_format=None, alignment=None, is_legal=None, restart_after_level=None, trailing_character=None, font=None, tab_position=None, number_position=None, text_position=None, linked_style=None):  # noqa: E501
        """ListLevel - a model defined in Swagger"""  # noqa: E501

        self._start_at = None
        self._number_style = None
        self._number_format = None
        self._alignment = None
        self._is_legal = None
        self._restart_after_level = None
        self._trailing_character = None
        self._font = None
        self._tab_position = None
        self._number_position = None
        self._text_position = None
        self._linked_style = None
        self.discriminator = None

        if start_at is not None:
            self.start_at = start_at
        if number_style is not None:
            self.number_style = number_style
        if number_format is not None:
            self.number_format = number_format
        if alignment is not None:
            self.alignment = alignment
        if is_legal is not None:
            self.is_legal = is_legal
        if restart_after_level is not None:
            self.restart_after_level = restart_after_level
        if trailing_character is not None:
            self.trailing_character = trailing_character
        if font is not None:
            self.font = font
        if tab_position is not None:
            self.tab_position = tab_position
        if number_position is not None:
            self.number_position = number_position
        if text_position is not None:
            self.text_position = text_position
        if linked_style is not None:
            self.linked_style = linked_style

    @property
    def start_at(self):
        """Gets the start_at of this ListLevel.  # noqa: E501

        Gets or sets returns or sets the starting number for this list level.  # noqa: E501

        :return: The start_at of this ListLevel.  # noqa: E501
        :rtype: int
        """
        return self._start_at

    @start_at.setter
    def start_at(self, start_at):
        """Sets the start_at of this ListLevel.

        Gets or sets returns or sets the starting number for this list level.  # noqa: E501

        :param start_at: The start_at of this ListLevel.  # noqa: E501
        :type: int
        """
        self._start_at = start_at
    @property
    def number_style(self):
        """Gets the number_style of this ListLevel.  # noqa: E501

        Gets or sets returns or sets the number style for this list level.  # noqa: E501

        :return: The number_style of this ListLevel.  # noqa: E501
        :rtype: str
        """
        return self._number_style

    @number_style.setter
    def number_style(self, number_style):
        """Sets the number_style of this ListLevel.

        Gets or sets returns or sets the number style for this list level.  # noqa: E501

        :param number_style: The number_style of this ListLevel.  # noqa: E501
        :type: str
        """
        allowed_values = ["Arabic", "UppercaseRoman", "LowercaseRoman", "UppercaseLetter", "LowercaseLetter", "Ordinal", "Number", "OrdinalText", "Hex", "ChicagoManual", "Kanji", "KanjiDigit", "AiueoHalfWidth", "IrohaHalfWidth", "ArabicFullWidth", "ArabicHalfWidth", "KanjiTraditional", "KanjiTraditional2", "NumberInCircle", "DecimalFullWidth", "Aiueo", "Iroha", "LeadingZero", "Bullet", "Ganada", "Chosung", "GB1", "GB2", "GB3", "GB4", "Zodiac1", "Zodiac2", "Zodiac3", "TradChinNum1", "TradChinNum2", "TradChinNum3", "TradChinNum4", "SimpChinNum1", "SimpChinNum2", "SimpChinNum3", "SimpChinNum4", "HanjaRead", "HanjaReadDigit", "Hangul", "Hanja", "Hebrew1", "Arabic1", "Hebrew2", "Arabic2", "HindiLetter1", "HindiLetter2", "HindiArabic", "HindiCardinalText", "ThaiLetter", "ThaiArabic", "ThaiCardinalText", "VietCardinalText", "NumberInDash", "LowercaseRussian", "UppercaseRussian", "None", "Custom"]  # noqa: E501
        if not number_style.isdigit():	
            if number_style not in allowed_values:
                raise ValueError(
                    "Invalid value for `number_style` ({0}), must be one of {1}"  # noqa: E501
                    .format(number_style, allowed_values))
            self._number_style = number_style
        else:
            self._number_style = allowed_values[int(number_style) if six.PY3 else long(number_style)]
    @property
    def number_format(self):
        """Gets the number_format of this ListLevel.  # noqa: E501

        Gets or sets returns or sets the number format for the list level.  # noqa: E501

        :return: The number_format of this ListLevel.  # noqa: E501
        :rtype: str
        """
        return self._number_format

    @number_format.setter
    def number_format(self, number_format):
        """Sets the number_format of this ListLevel.

        Gets or sets returns or sets the number format for the list level.  # noqa: E501

        :param number_format: The number_format of this ListLevel.  # noqa: E501
        :type: str
        """
        self._number_format = number_format
    @property
    def alignment(self):
        """Gets the alignment of this ListLevel.  # noqa: E501

        Gets or sets the justification of the actual number of the list item.  # noqa: E501

        :return: The alignment of this ListLevel.  # noqa: E501
        :rtype: str
        """
        return self._alignment

    @alignment.setter
    def alignment(self, alignment):
        """Sets the alignment of this ListLevel.

        Gets or sets the justification of the actual number of the list item.  # noqa: E501

        :param alignment: The alignment of this ListLevel.  # noqa: E501
        :type: str
        """
        allowed_values = ["Left", "Center", "Right"]  # noqa: E501
        if not alignment.isdigit():	
            if alignment not in allowed_values:
                raise ValueError(
                    "Invalid value for `alignment` ({0}), must be one of {1}"  # noqa: E501
                    .format(alignment, allowed_values))
            self._alignment = alignment
        else:
            self._alignment = allowed_values[int(alignment) if six.PY3 else long(alignment)]
    @property
    def is_legal(self):
        """Gets the is_legal of this ListLevel.  # noqa: E501

        Gets or sets a value indicating whether true if the level turns all inherited numbers to Arabic, false if it preserves their number style.  # noqa: E501

        :return: The is_legal of this ListLevel.  # noqa: E501
        :rtype: bool
        """
        return self._is_legal

    @is_legal.setter
    def is_legal(self, is_legal):
        """Sets the is_legal of this ListLevel.

        Gets or sets a value indicating whether true if the level turns all inherited numbers to Arabic, false if it preserves their number style.  # noqa: E501

        :param is_legal: The is_legal of this ListLevel.  # noqa: E501
        :type: bool
        """
        self._is_legal = is_legal
    @property
    def restart_after_level(self):
        """Gets the restart_after_level of this ListLevel.  # noqa: E501

        Gets or sets or returns the list level that must appear before the specified list level restarts numbering.  # noqa: E501

        :return: The restart_after_level of this ListLevel.  # noqa: E501
        :rtype: int
        """
        return self._restart_after_level

    @restart_after_level.setter
    def restart_after_level(self, restart_after_level):
        """Sets the restart_after_level of this ListLevel.

        Gets or sets or returns the list level that must appear before the specified list level restarts numbering.  # noqa: E501

        :param restart_after_level: The restart_after_level of this ListLevel.  # noqa: E501
        :type: int
        """
        self._restart_after_level = restart_after_level
    @property
    def trailing_character(self):
        """Gets the trailing_character of this ListLevel.  # noqa: E501

        Gets or sets returns or sets the character inserted after the number for the list level.  # noqa: E501

        :return: The trailing_character of this ListLevel.  # noqa: E501
        :rtype: str
        """
        return self._trailing_character

    @trailing_character.setter
    def trailing_character(self, trailing_character):
        """Sets the trailing_character of this ListLevel.

        Gets or sets returns or sets the character inserted after the number for the list level.  # noqa: E501

        :param trailing_character: The trailing_character of this ListLevel.  # noqa: E501
        :type: str
        """
        allowed_values = ["Tab", "Space", "Nothing"]  # noqa: E501
        if not trailing_character.isdigit():	
            if trailing_character not in allowed_values:
                raise ValueError(
                    "Invalid value for `trailing_character` ({0}), must be one of {1}"  # noqa: E501
                    .format(trailing_character, allowed_values))
            self._trailing_character = trailing_character
        else:
            self._trailing_character = allowed_values[int(trailing_character) if six.PY3 else long(trailing_character)]
    @property
    def font(self):
        """Gets the font of this ListLevel.  # noqa: E501

        Gets or sets font.  # noqa: E501

        :return: The font of this ListLevel.  # noqa: E501
        :rtype: Font
        """
        return self._font

    @font.setter
    def font(self, font):
        """Sets the font of this ListLevel.

        Gets or sets font.  # noqa: E501

        :param font: The font of this ListLevel.  # noqa: E501
        :type: Font
        """
        self._font = font
    @property
    def tab_position(self):
        """Gets the tab_position of this ListLevel.  # noqa: E501

        Gets or sets returns or sets the tab position (in points) for the list level.  # noqa: E501

        :return: The tab_position of this ListLevel.  # noqa: E501
        :rtype: float
        """
        return self._tab_position

    @tab_position.setter
    def tab_position(self, tab_position):
        """Sets the tab_position of this ListLevel.

        Gets or sets returns or sets the tab position (in points) for the list level.  # noqa: E501

        :param tab_position: The tab_position of this ListLevel.  # noqa: E501
        :type: float
        """
        self._tab_position = tab_position
    @property
    def number_position(self):
        """Gets the number_position of this ListLevel.  # noqa: E501

        Gets or sets returns or sets the position (in points) of the number or bullet for the list level.  # noqa: E501

        :return: The number_position of this ListLevel.  # noqa: E501
        :rtype: float
        """
        return self._number_position

    @number_position.setter
    def number_position(self, number_position):
        """Sets the number_position of this ListLevel.

        Gets or sets returns or sets the position (in points) of the number or bullet for the list level.  # noqa: E501

        :param number_position: The number_position of this ListLevel.  # noqa: E501
        :type: float
        """
        self._number_position = number_position
    @property
    def text_position(self):
        """Gets the text_position of this ListLevel.  # noqa: E501

        Gets or sets returns or sets the position (in points) for the second line of wrapping text for the list level.  # noqa: E501

        :return: The text_position of this ListLevel.  # noqa: E501
        :rtype: float
        """
        return self._text_position

    @text_position.setter
    def text_position(self, text_position):
        """Sets the text_position of this ListLevel.

        Gets or sets returns or sets the position (in points) for the second line of wrapping text for the list level.  # noqa: E501

        :param text_position: The text_position of this ListLevel.  # noqa: E501
        :type: float
        """
        self._text_position = text_position
    @property
    def linked_style(self):
        """Gets the linked_style of this ListLevel.  # noqa: E501

        Gets or sets linked_style.  # noqa: E501

        :return: The linked_style of this ListLevel.  # noqa: E501
        :rtype: Style
        """
        return self._linked_style

    @linked_style.setter
    def linked_style(self, linked_style):
        """Sets the linked_style of this ListLevel.

        Gets or sets linked_style.  # noqa: E501

        :param linked_style: The linked_style of this ListLevel.  # noqa: E501
        :type: Style
        """
        self._linked_style = linked_style
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
        if not isinstance(other, ListLevel):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
