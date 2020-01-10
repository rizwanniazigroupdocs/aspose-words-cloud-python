# coding: utf-8
# -----------------------------------------------------------------------------------
# <copyright company="Aspose" file="PdfEncryptionDetailsData.py">
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


class PdfEncryptionDetailsData(object):
    """container class for details of encryption.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'encryption_algorithm': 'str',
        'owner_password': 'str',
        'permissions': 'str',
        'user_password': 'str'
    }

    attribute_map = {
        'encryption_algorithm': 'encryptionAlgorithm',
        'owner_password': 'ownerPassword',
        'permissions': 'permissions',
        'user_password': 'userPassword'
    }

    def __init__(self, encryption_algorithm=None, owner_password=None, permissions=None, user_password=None):  # noqa: E501
        """PdfEncryptionDetailsData - a model defined in Swagger"""  # noqa: E501

        self._encryption_algorithm = None
        self._owner_password = None
        self._permissions = None
        self._user_password = None
        self.discriminator = None

        if encryption_algorithm is not None:
            self.encryption_algorithm = encryption_algorithm
        if owner_password is not None:
            self.owner_password = owner_password
        if permissions is not None:
            self.permissions = permissions
        if user_password is not None:
            self.user_password = user_password

    @property
    def encryption_algorithm(self):
        """Gets the encryption_algorithm of this PdfEncryptionDetailsData.  # noqa: E501

        Gets or sets specifies the encryption algorithm to use.  # noqa: E501

        :return: The encryption_algorithm of this PdfEncryptionDetailsData.  # noqa: E501
        :rtype: str
        """
        return self._encryption_algorithm

    @encryption_algorithm.setter
    def encryption_algorithm(self, encryption_algorithm):
        """Sets the encryption_algorithm of this PdfEncryptionDetailsData.

        Gets or sets specifies the encryption algorithm to use.  # noqa: E501

        :param encryption_algorithm: The encryption_algorithm of this PdfEncryptionDetailsData.  # noqa: E501
        :type: str
        """
        self._encryption_algorithm = encryption_algorithm
    @property
    def owner_password(self):
        """Gets the owner_password of this PdfEncryptionDetailsData.  # noqa: E501

        Gets or sets specifies the owner password for the encrypted PDF document.  # noqa: E501

        :return: The owner_password of this PdfEncryptionDetailsData.  # noqa: E501
        :rtype: str
        """
        return self._owner_password

    @owner_password.setter
    def owner_password(self, owner_password):
        """Sets the owner_password of this PdfEncryptionDetailsData.

        Gets or sets specifies the owner password for the encrypted PDF document.  # noqa: E501

        :param owner_password: The owner_password of this PdfEncryptionDetailsData.  # noqa: E501
        :type: str
        """
        self._owner_password = owner_password
    @property
    def permissions(self):
        """Gets the permissions of this PdfEncryptionDetailsData.  # noqa: E501

        Gets or sets specifies the operations that are allowed to a user on an encrypted PDF document.  # noqa: E501

        :return: The permissions of this PdfEncryptionDetailsData.  # noqa: E501
        :rtype: str
        """
        return self._permissions

    @permissions.setter
    def permissions(self, permissions):
        """Sets the permissions of this PdfEncryptionDetailsData.

        Gets or sets specifies the operations that are allowed to a user on an encrypted PDF document.  # noqa: E501

        :param permissions: The permissions of this PdfEncryptionDetailsData.  # noqa: E501
        :type: str
        """
        self._permissions = permissions
    @property
    def user_password(self):
        """Gets the user_password of this PdfEncryptionDetailsData.  # noqa: E501

        Gets or sets specifies the user password required for opening the encrypted PDF document.  # noqa: E501

        :return: The user_password of this PdfEncryptionDetailsData.  # noqa: E501
        :rtype: str
        """
        return self._user_password

    @user_password.setter
    def user_password(self, user_password):
        """Sets the user_password of this PdfEncryptionDetailsData.

        Gets or sets specifies the user password required for opening the encrypted PDF document.  # noqa: E501

        :param user_password: The user_password of this PdfEncryptionDetailsData.  # noqa: E501
        :type: str
        """
        self._user_password = user_password
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
        if not isinstance(other, PdfEncryptionDetailsData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
