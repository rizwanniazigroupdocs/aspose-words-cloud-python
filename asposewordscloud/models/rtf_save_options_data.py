# coding: utf-8
# -----------------------------------------------------------------------------------
# <copyright company="Aspose" file="rtf_save_options_data.py">
#   Copyright (c) 2020 Aspose.Words for Cloud
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
import json


class RtfSaveOptionsData(object):
    """container class for rtf save options.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'dml3_d_effects_rendering_mode': 'str',
        'dml_effects_rendering_mode': 'str',
        'dml_rendering_mode': 'str',
        'file_name': 'str',
        'save_format': 'str',
        'update_fields': 'bool',
        'update_last_printed_property': 'bool',
        'update_last_saved_time_property': 'bool',
        'update_sdt_content': 'bool',
        'zip_output': 'bool',
        'export_compact_size': 'bool',
        'export_images_for_old_readers': 'bool',
        'pretty_format': 'bool',
        'save_images_as_wmf': 'bool'
    }

    attribute_map = {
        'dml3_d_effects_rendering_mode': 'Dml3DEffectsRenderingMode',
        'dml_effects_rendering_mode': 'DmlEffectsRenderingMode',
        'dml_rendering_mode': 'DmlRenderingMode',
        'file_name': 'FileName',
        'save_format': 'SaveFormat',
        'update_fields': 'UpdateFields',
        'update_last_printed_property': 'UpdateLastPrintedProperty',
        'update_last_saved_time_property': 'UpdateLastSavedTimeProperty',
        'update_sdt_content': 'UpdateSdtContent',
        'zip_output': 'ZipOutput',
        'export_compact_size': 'ExportCompactSize',
        'export_images_for_old_readers': 'ExportImagesForOldReaders',
        'pretty_format': 'PrettyFormat',
        'save_images_as_wmf': 'SaveImagesAsWmf'
    }

    def __init__(self, dml3_d_effects_rendering_mode=None, dml_effects_rendering_mode=None, dml_rendering_mode=None, file_name=None, save_format=None, update_fields=None, update_last_printed_property=None, update_last_saved_time_property=None, update_sdt_content=None, zip_output=None, export_compact_size=None, export_images_for_old_readers=None, pretty_format=None, save_images_as_wmf=None):  # noqa: E501
        """RtfSaveOptionsData - a model defined in Swagger"""  # noqa: E501

        self._dml3_d_effects_rendering_mode = None
        self._dml_effects_rendering_mode = None
        self._dml_rendering_mode = None
        self._file_name = None
        self._save_format = None
        self._update_fields = None
        self._update_last_printed_property = None
        self._update_last_saved_time_property = None
        self._update_sdt_content = None
        self._zip_output = None
        self._export_compact_size = None
        self._export_images_for_old_readers = None
        self._pretty_format = None
        self._save_images_as_wmf = None
        self.discriminator = None

        if dml3_d_effects_rendering_mode is not None:
            self.dml3_d_effects_rendering_mode = dml3_d_effects_rendering_mode
        if dml_effects_rendering_mode is not None:
            self.dml_effects_rendering_mode = dml_effects_rendering_mode
        if dml_rendering_mode is not None:
            self.dml_rendering_mode = dml_rendering_mode
        if file_name is not None:
            self.file_name = file_name
        if save_format is not None:
            self.save_format = save_format
        if update_fields is not None:
            self.update_fields = update_fields
        if update_last_printed_property is not None:
            self.update_last_printed_property = update_last_printed_property
        if update_last_saved_time_property is not None:
            self.update_last_saved_time_property = update_last_saved_time_property
        if update_sdt_content is not None:
            self.update_sdt_content = update_sdt_content
        if zip_output is not None:
            self.zip_output = zip_output
        if export_compact_size is not None:
            self.export_compact_size = export_compact_size
        if export_images_for_old_readers is not None:
            self.export_images_for_old_readers = export_images_for_old_readers
        if pretty_format is not None:
            self.pretty_format = pretty_format
        if save_images_as_wmf is not None:
            self.save_images_as_wmf = save_images_as_wmf

    @property
    def dml3_d_effects_rendering_mode(self):
        """Gets the dml3_d_effects_rendering_mode of this RtfSaveOptionsData.  # noqa: E501

        Gets or sets a value determining how 3D effects are rendered.  # noqa: E501

        :return: The dml3_d_effects_rendering_mode of this RtfSaveOptionsData.  # noqa: E501
        :rtype: str
        """
        return self._dml3_d_effects_rendering_mode

    @dml3_d_effects_rendering_mode.setter
    def dml3_d_effects_rendering_mode(self, dml3_d_effects_rendering_mode):
        """Sets the dml3_d_effects_rendering_mode of this RtfSaveOptionsData.

        Gets or sets a value determining how 3D effects are rendered.  # noqa: E501

        :param dml3_d_effects_rendering_mode: The dml3_d_effects_rendering_mode of this RtfSaveOptionsData.  # noqa: E501
        :type: str
        """
        allowed_values = ["Basic", "Advanced"]  # noqa: E501
        if not dml3_d_effects_rendering_mode.isdigit():
            if dml3_d_effects_rendering_mode not in allowed_values:
                raise ValueError(
                    "Invalid value for `dml3_d_effects_rendering_mode` ({0}), must be one of {1}"  # noqa: E501
                    .format(dml3_d_effects_rendering_mode, allowed_values))
            self._dml3_d_effects_rendering_mode = dml3_d_effects_rendering_mode
        else:
            self._dml3_d_effects_rendering_mode = allowed_values[int(dml3_d_effects_rendering_mode) if six.PY3 else long(dml3_d_effects_rendering_mode)]

    @property
    def dml_effects_rendering_mode(self):
        """Gets the dml_effects_rendering_mode of this RtfSaveOptionsData.  # noqa: E501

        Gets or sets a value determining how DrawingML effects are rendered. { Simplified | None | Fine }.  # noqa: E501

        :return: The dml_effects_rendering_mode of this RtfSaveOptionsData.  # noqa: E501
        :rtype: str
        """
        return self._dml_effects_rendering_mode

    @dml_effects_rendering_mode.setter
    def dml_effects_rendering_mode(self, dml_effects_rendering_mode):
        """Sets the dml_effects_rendering_mode of this RtfSaveOptionsData.

        Gets or sets a value determining how DrawingML effects are rendered. { Simplified | None | Fine }.  # noqa: E501

        :param dml_effects_rendering_mode: The dml_effects_rendering_mode of this RtfSaveOptionsData.  # noqa: E501
        :type: str
        """
        self._dml_effects_rendering_mode = dml_effects_rendering_mode

    @property
    def dml_rendering_mode(self):
        """Gets the dml_rendering_mode of this RtfSaveOptionsData.  # noqa: E501

        Gets or sets a value determining how DrawingML shapes are rendered. { Fallback | DrawingML }.  # noqa: E501

        :return: The dml_rendering_mode of this RtfSaveOptionsData.  # noqa: E501
        :rtype: str
        """
        return self._dml_rendering_mode

    @dml_rendering_mode.setter
    def dml_rendering_mode(self, dml_rendering_mode):
        """Sets the dml_rendering_mode of this RtfSaveOptionsData.

        Gets or sets a value determining how DrawingML shapes are rendered. { Fallback | DrawingML }.  # noqa: E501

        :param dml_rendering_mode: The dml_rendering_mode of this RtfSaveOptionsData.  # noqa: E501
        :type: str
        """
        self._dml_rendering_mode = dml_rendering_mode

    @property
    def file_name(self):
        """Gets the file_name of this RtfSaveOptionsData.  # noqa: E501

        Gets or sets name of destination file.  # noqa: E501

        :return: The file_name of this RtfSaveOptionsData.  # noqa: E501
        :rtype: str
        """
        return self._file_name

    @file_name.setter
    def file_name(self, file_name):
        """Sets the file_name of this RtfSaveOptionsData.

        Gets or sets name of destination file.  # noqa: E501

        :param file_name: The file_name of this RtfSaveOptionsData.  # noqa: E501
        :type: str
        """
        self._file_name = file_name

    @property
    def save_format(self):
        """Gets the save_format of this RtfSaveOptionsData.  # noqa: E501

        Gets or sets format of save.  # noqa: E501

        :return: The save_format of this RtfSaveOptionsData.  # noqa: E501
        :rtype: str
        """
        return self._save_format

    @save_format.setter
    def save_format(self, save_format):
        """Sets the save_format of this RtfSaveOptionsData.

        Gets or sets format of save.  # noqa: E501

        :param save_format: The save_format of this RtfSaveOptionsData.  # noqa: E501
        :type: str
        """
        self._save_format = save_format

    @property
    def update_fields(self):
        """Gets the update_fields of this RtfSaveOptionsData.  # noqa: E501

        Gets or sets a value determining if fields should be updated before saving the document to a fixed page format. Default value for this property is. true.  # noqa: E501

        :return: The update_fields of this RtfSaveOptionsData.  # noqa: E501
        :rtype: bool
        """
        return self._update_fields

    @update_fields.setter
    def update_fields(self, update_fields):
        """Sets the update_fields of this RtfSaveOptionsData.

        Gets or sets a value determining if fields should be updated before saving the document to a fixed page format. Default value for this property is. true.  # noqa: E501

        :param update_fields: The update_fields of this RtfSaveOptionsData.  # noqa: E501
        :type: bool
        """
        self._update_fields = update_fields

    @property
    def update_last_printed_property(self):
        """Gets the update_last_printed_property of this RtfSaveOptionsData.  # noqa: E501

        Gets or sets a value determining whether the Aspose.Words.Properties.BuiltInDocumentProperties.LastPrinted property is updated before saving.  # noqa: E501

        :return: The update_last_printed_property of this RtfSaveOptionsData.  # noqa: E501
        :rtype: bool
        """
        return self._update_last_printed_property

    @update_last_printed_property.setter
    def update_last_printed_property(self, update_last_printed_property):
        """Sets the update_last_printed_property of this RtfSaveOptionsData.

        Gets or sets a value determining whether the Aspose.Words.Properties.BuiltInDocumentProperties.LastPrinted property is updated before saving.  # noqa: E501

        :param update_last_printed_property: The update_last_printed_property of this RtfSaveOptionsData.  # noqa: E501
        :type: bool
        """
        self._update_last_printed_property = update_last_printed_property

    @property
    def update_last_saved_time_property(self):
        """Gets the update_last_saved_time_property of this RtfSaveOptionsData.  # noqa: E501

        Gets or sets a value determining whether the Aspose.Words.Properties.BuiltInDocumentProperties.LastSavedTime property is updated before saving.  # noqa: E501

        :return: The update_last_saved_time_property of this RtfSaveOptionsData.  # noqa: E501
        :rtype: bool
        """
        return self._update_last_saved_time_property

    @update_last_saved_time_property.setter
    def update_last_saved_time_property(self, update_last_saved_time_property):
        """Sets the update_last_saved_time_property of this RtfSaveOptionsData.

        Gets or sets a value determining whether the Aspose.Words.Properties.BuiltInDocumentProperties.LastSavedTime property is updated before saving.  # noqa: E501

        :param update_last_saved_time_property: The update_last_saved_time_property of this RtfSaveOptionsData.  # noqa: E501
        :type: bool
        """
        self._update_last_saved_time_property = update_last_saved_time_property

    @property
    def update_sdt_content(self):
        """Gets the update_sdt_content of this RtfSaveOptionsData.  # noqa: E501

        Gets or sets value determining whether content of StructuredDocumentTag is updated before saving.  # noqa: E501

        :return: The update_sdt_content of this RtfSaveOptionsData.  # noqa: E501
        :rtype: bool
        """
        return self._update_sdt_content

    @update_sdt_content.setter
    def update_sdt_content(self, update_sdt_content):
        """Sets the update_sdt_content of this RtfSaveOptionsData.

        Gets or sets value determining whether content of StructuredDocumentTag is updated before saving.  # noqa: E501

        :param update_sdt_content: The update_sdt_content of this RtfSaveOptionsData.  # noqa: E501
        :type: bool
        """
        self._update_sdt_content = update_sdt_content

    @property
    def zip_output(self):
        """Gets the zip_output of this RtfSaveOptionsData.  # noqa: E501

        Gets or sets controls zip output or not. Default value is false.  # noqa: E501

        :return: The zip_output of this RtfSaveOptionsData.  # noqa: E501
        :rtype: bool
        """
        return self._zip_output

    @zip_output.setter
    def zip_output(self, zip_output):
        """Sets the zip_output of this RtfSaveOptionsData.

        Gets or sets controls zip output or not. Default value is false.  # noqa: E501

        :param zip_output: The zip_output of this RtfSaveOptionsData.  # noqa: E501
        :type: bool
        """
        self._zip_output = zip_output

    @property
    def export_compact_size(self):
        """Gets the export_compact_size of this RtfSaveOptionsData.  # noqa: E501

        Gets or sets allows to make output RTF documents smaller in size, but if they contain RTL (right-to-left) text, it will not be displayed correctly.  # noqa: E501

        :return: The export_compact_size of this RtfSaveOptionsData.  # noqa: E501
        :rtype: bool
        """
        return self._export_compact_size

    @export_compact_size.setter
    def export_compact_size(self, export_compact_size):
        """Sets the export_compact_size of this RtfSaveOptionsData.

        Gets or sets allows to make output RTF documents smaller in size, but if they contain RTL (right-to-left) text, it will not be displayed correctly.  # noqa: E501

        :param export_compact_size: The export_compact_size of this RtfSaveOptionsData.  # noqa: E501
        :type: bool
        """
        self._export_compact_size = export_compact_size

    @property
    def export_images_for_old_readers(self):
        """Gets the export_images_for_old_readers of this RtfSaveOptionsData.  # noqa: E501

        Gets or sets specifies whether the keywords for "old readers" are written to RTF or not.  # noqa: E501

        :return: The export_images_for_old_readers of this RtfSaveOptionsData.  # noqa: E501
        :rtype: bool
        """
        return self._export_images_for_old_readers

    @export_images_for_old_readers.setter
    def export_images_for_old_readers(self, export_images_for_old_readers):
        """Sets the export_images_for_old_readers of this RtfSaveOptionsData.

        Gets or sets specifies whether the keywords for "old readers" are written to RTF or not.  # noqa: E501

        :param export_images_for_old_readers: The export_images_for_old_readers of this RtfSaveOptionsData.  # noqa: E501
        :type: bool
        """
        self._export_images_for_old_readers = export_images_for_old_readers

    @property
    def pretty_format(self):
        """Gets the pretty_format of this RtfSaveOptionsData.  # noqa: E501

        Gets or sets specifies whether or not use pretty formats output.  # noqa: E501

        :return: The pretty_format of this RtfSaveOptionsData.  # noqa: E501
        :rtype: bool
        """
        return self._pretty_format

    @pretty_format.setter
    def pretty_format(self, pretty_format):
        """Sets the pretty_format of this RtfSaveOptionsData.

        Gets or sets specifies whether or not use pretty formats output.  # noqa: E501

        :param pretty_format: The pretty_format of this RtfSaveOptionsData.  # noqa: E501
        :type: bool
        """
        self._pretty_format = pretty_format

    @property
    def save_images_as_wmf(self):
        """Gets the save_images_as_wmf of this RtfSaveOptionsData.  # noqa: E501

        Gets or sets a value indicating whether when true all images will be saved as WMF. This option might help to avoid WordPad warning messages.  # noqa: E501

        :return: The save_images_as_wmf of this RtfSaveOptionsData.  # noqa: E501
        :rtype: bool
        """
        return self._save_images_as_wmf

    @save_images_as_wmf.setter
    def save_images_as_wmf(self, save_images_as_wmf):
        """Sets the save_images_as_wmf of this RtfSaveOptionsData.

        Gets or sets a value indicating whether when true all images will be saved as WMF. This option might help to avoid WordPad warning messages.  # noqa: E501

        :param save_images_as_wmf: The save_images_as_wmf of this RtfSaveOptionsData.  # noqa: E501
        :type: bool
        """
        self._save_images_as_wmf = save_images_as_wmf


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

    def to_json(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[self.attribute_map[attr]] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[self.attribute_map[attr]] = value.to_dict()
            elif isinstance(value, dict):
                result[self.attribute_map[attr]] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[self.attribute_map[attr]] = value

        return json.dumps(result)

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, RtfSaveOptionsData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other