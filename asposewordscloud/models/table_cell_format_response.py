# coding: utf-8
# -----------------------------------------------------------------------------------
# <copyright company="Aspose" file="TableCellFormatResponse.py">
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


class TableCellFormatResponse(object):
    """This response should be returned by the service when handling: GET http://api.aspose.com/v4.0/words/Test.doc/tables/{0}/rows/{1}/cells/{2}/cellformat.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'request_id': 'str',
        'cell_format': 'TableCellFormat'
    }

    attribute_map = {
        'request_id': 'RequestId',
        'cell_format': 'CellFormat'
    }

    def __init__(self, request_id=None, cell_format=None):  # noqa: E501
        """TableCellFormatResponse - a model defined in Swagger"""  # noqa: E501

        self._request_id = None
        self._cell_format = None
        self.discriminator = None

        if request_id is not None:
            self.request_id = request_id
        if cell_format is not None:
            self.cell_format = cell_format

    @property
    def request_id(self):
        """Gets the request_id of this TableCellFormatResponse.  # noqa: E501

        Gets or sets request Id.  # noqa: E501

        :return: The request_id of this TableCellFormatResponse.  # noqa: E501
        :rtype: str
        """
        return self._request_id

    @request_id.setter
    def request_id(self, request_id):
        """Sets the request_id of this TableCellFormatResponse.

        Gets or sets request Id.  # noqa: E501

        :param request_id: The request_id of this TableCellFormatResponse.  # noqa: E501
        :type: str
        """
        self._request_id = request_id
    @property
    def cell_format(self):
        """Gets the cell_format of this TableCellFormatResponse.  # noqa: E501

        Gets or sets table.  # noqa: E501

        :return: The cell_format of this TableCellFormatResponse.  # noqa: E501
        :rtype: TableCellFormat
        """
        return self._cell_format

    @cell_format.setter
    def cell_format(self, cell_format):
        """Sets the cell_format of this TableCellFormatResponse.

        Gets or sets table.  # noqa: E501

        :param cell_format: The cell_format of this TableCellFormatResponse.  # noqa: E501
        :type: TableCellFormat
        """
        self._cell_format = cell_format
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
        if not isinstance(other, TableCellFormatResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
