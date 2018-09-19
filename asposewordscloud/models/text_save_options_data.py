# coding: utf-8
# -----------------------------------------------------------------------------------
# <copyright company="Aspose" file="TextSaveOptionsData.py">
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


class TextSaveOptionsData(object):
    """Container class for text save options.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'color_mode': 'str',
        'save_format': 'str',
        'file_name': 'str',
        'dml_rendering_mode': 'str',
        'dml_effects_rendering_mode': 'str',
        'zip_output': 'bool',
        'update_last_saved_time_property': 'bool',
        'update_sdt_content': 'bool',
        'update_fields': 'bool',
        'encoding': 'str',
        'export_headers_footers': 'bool',
        'force_page_breaks': 'bool',
        'paragraph_break': 'str',
        'preserve_table_layout': 'bool',
        'simplify_list_labels': 'bool'
    }

    attribute_map = {
        'color_mode': 'ColorMode',
        'save_format': 'SaveFormat',
        'file_name': 'FileName',
        'dml_rendering_mode': 'DmlRenderingMode',
        'dml_effects_rendering_mode': 'DmlEffectsRenderingMode',
        'zip_output': 'ZipOutput',
        'update_last_saved_time_property': 'UpdateLastSavedTimeProperty',
        'update_sdt_content': 'UpdateSdtContent',
        'update_fields': 'UpdateFields',
        'encoding': 'Encoding',
        'export_headers_footers': 'ExportHeadersFooters',
        'force_page_breaks': 'ForcePageBreaks',
        'paragraph_break': 'ParagraphBreak',
        'preserve_table_layout': 'PreserveTableLayout',
        'simplify_list_labels': 'SimplifyListLabels'
    }

    def __init__(self, color_mode=None, save_format=None, file_name=None, dml_rendering_mode=None, dml_effects_rendering_mode=None, zip_output=None, update_last_saved_time_property=None, update_sdt_content=None, update_fields=None, encoding=None, export_headers_footers=None, force_page_breaks=None, paragraph_break=None, preserve_table_layout=None, simplify_list_labels=None):  # noqa: E501
        """TextSaveOptionsData - a model defined in Swagger"""  # noqa: E501

        self._color_mode = None
        self._save_format = None
        self._file_name = None
        self._dml_rendering_mode = None
        self._dml_effects_rendering_mode = None
        self._zip_output = None
        self._update_last_saved_time_property = None
        self._update_sdt_content = None
        self._update_fields = None
        self._encoding = None
        self._export_headers_footers = None
        self._force_page_breaks = None
        self._paragraph_break = None
        self._preserve_table_layout = None
        self._simplify_list_labels = None
        self.discriminator = None

        if color_mode is not None:
            self.color_mode = color_mode
        if save_format is not None:
            self.save_format = save_format
        if file_name is not None:
            self.file_name = file_name
        if dml_rendering_mode is not None:
            self.dml_rendering_mode = dml_rendering_mode
        if dml_effects_rendering_mode is not None:
            self.dml_effects_rendering_mode = dml_effects_rendering_mode
        if zip_output is not None:
            self.zip_output = zip_output
        if update_last_saved_time_property is not None:
            self.update_last_saved_time_property = update_last_saved_time_property
        if update_sdt_content is not None:
            self.update_sdt_content = update_sdt_content
        if update_fields is not None:
            self.update_fields = update_fields
        if encoding is not None:
            self.encoding = encoding
        if export_headers_footers is not None:
            self.export_headers_footers = export_headers_footers
        if force_page_breaks is not None:
            self.force_page_breaks = force_page_breaks
        if paragraph_break is not None:
            self.paragraph_break = paragraph_break
        if preserve_table_layout is not None:
            self.preserve_table_layout = preserve_table_layout
        if simplify_list_labels is not None:
            self.simplify_list_labels = simplify_list_labels

    @property
    def color_mode(self):
        """Gets the color_mode of this TextSaveOptionsData.  # noqa: E501

        Gets or sets a value determining how colors are rendered. { Normal | Grayscale}  # noqa: E501

        :return: The color_mode of this TextSaveOptionsData.  # noqa: E501
        :rtype: str
        """
        return self._color_mode

    @color_mode.setter
    def color_mode(self, color_mode):
        """Sets the color_mode of this TextSaveOptionsData.

        Gets or sets a value determining how colors are rendered. { Normal | Grayscale}  # noqa: E501

        :param color_mode: The color_mode of this TextSaveOptionsData.  # noqa: E501
        :type: str
        """
        self._color_mode = color_mode
    @property
    def save_format(self):
        """Gets the save_format of this TextSaveOptionsData.  # noqa: E501

        format of save  # noqa: E501

        :return: The save_format of this TextSaveOptionsData.  # noqa: E501
        :rtype: str
        """
        return self._save_format

    @save_format.setter
    def save_format(self, save_format):
        """Sets the save_format of this TextSaveOptionsData.

        format of save  # noqa: E501

        :param save_format: The save_format of this TextSaveOptionsData.  # noqa: E501
        :type: str
        """
        self._save_format = save_format
    @property
    def file_name(self):
        """Gets the file_name of this TextSaveOptionsData.  # noqa: E501

        name of destination file  # noqa: E501

        :return: The file_name of this TextSaveOptionsData.  # noqa: E501
        :rtype: str
        """
        return self._file_name

    @file_name.setter
    def file_name(self, file_name):
        """Sets the file_name of this TextSaveOptionsData.

        name of destination file  # noqa: E501

        :param file_name: The file_name of this TextSaveOptionsData.  # noqa: E501
        :type: str
        """
        self._file_name = file_name
    @property
    def dml_rendering_mode(self):
        """Gets the dml_rendering_mode of this TextSaveOptionsData.  # noqa: E501

        Gets or sets a value determining how DrawingML shapes are rendered. { Fallback | DrawingML }  # noqa: E501

        :return: The dml_rendering_mode of this TextSaveOptionsData.  # noqa: E501
        :rtype: str
        """
        return self._dml_rendering_mode

    @dml_rendering_mode.setter
    def dml_rendering_mode(self, dml_rendering_mode):
        """Sets the dml_rendering_mode of this TextSaveOptionsData.

        Gets or sets a value determining how DrawingML shapes are rendered. { Fallback | DrawingML }  # noqa: E501

        :param dml_rendering_mode: The dml_rendering_mode of this TextSaveOptionsData.  # noqa: E501
        :type: str
        """
        self._dml_rendering_mode = dml_rendering_mode
    @property
    def dml_effects_rendering_mode(self):
        """Gets the dml_effects_rendering_mode of this TextSaveOptionsData.  # noqa: E501

        Gets or sets a value determining how DrawingML effects are rendered. { Simplified | None | Fine }  # noqa: E501

        :return: The dml_effects_rendering_mode of this TextSaveOptionsData.  # noqa: E501
        :rtype: str
        """
        return self._dml_effects_rendering_mode

    @dml_effects_rendering_mode.setter
    def dml_effects_rendering_mode(self, dml_effects_rendering_mode):
        """Sets the dml_effects_rendering_mode of this TextSaveOptionsData.

        Gets or sets a value determining how DrawingML effects are rendered. { Simplified | None | Fine }  # noqa: E501

        :param dml_effects_rendering_mode: The dml_effects_rendering_mode of this TextSaveOptionsData.  # noqa: E501
        :type: str
        """
        self._dml_effects_rendering_mode = dml_effects_rendering_mode
    @property
    def zip_output(self):
        """Gets the zip_output of this TextSaveOptionsData.  # noqa: E501

        Controls zip output or not. Default value is false.  # noqa: E501

        :return: The zip_output of this TextSaveOptionsData.  # noqa: E501
        :rtype: bool
        """
        return self._zip_output

    @zip_output.setter
    def zip_output(self, zip_output):
        """Sets the zip_output of this TextSaveOptionsData.

        Controls zip output or not. Default value is false.  # noqa: E501

        :param zip_output: The zip_output of this TextSaveOptionsData.  # noqa: E501
        :type: bool
        """
        self._zip_output = zip_output
    @property
    def update_last_saved_time_property(self):
        """Gets the update_last_saved_time_property of this TextSaveOptionsData.  # noqa: E501

        Gets or sets a value determining whether the Aspose.Words.Properties.BuiltInDocumentProperties.LastSavedTime property is updated before saving.  # noqa: E501

        :return: The update_last_saved_time_property of this TextSaveOptionsData.  # noqa: E501
        :rtype: bool
        """
        return self._update_last_saved_time_property

    @update_last_saved_time_property.setter
    def update_last_saved_time_property(self, update_last_saved_time_property):
        """Sets the update_last_saved_time_property of this TextSaveOptionsData.

        Gets or sets a value determining whether the Aspose.Words.Properties.BuiltInDocumentProperties.LastSavedTime property is updated before saving.  # noqa: E501

        :param update_last_saved_time_property: The update_last_saved_time_property of this TextSaveOptionsData.  # noqa: E501
        :type: bool
        """
        self._update_last_saved_time_property = update_last_saved_time_property
    @property
    def update_sdt_content(self):
        """Gets the update_sdt_content of this TextSaveOptionsData.  # noqa: E501

        Gets or sets value determining whether content of  is updated before saving.  # noqa: E501

        :return: The update_sdt_content of this TextSaveOptionsData.  # noqa: E501
        :rtype: bool
        """
        return self._update_sdt_content

    @update_sdt_content.setter
    def update_sdt_content(self, update_sdt_content):
        """Sets the update_sdt_content of this TextSaveOptionsData.

        Gets or sets value determining whether content of  is updated before saving.  # noqa: E501

        :param update_sdt_content: The update_sdt_content of this TextSaveOptionsData.  # noqa: E501
        :type: bool
        """
        self._update_sdt_content = update_sdt_content
    @property
    def update_fields(self):
        """Gets the update_fields of this TextSaveOptionsData.  # noqa: E501

        Gets or sets a value determining if fields should be updated before saving the document to a fixed page format. Default value for this property is true  # noqa: E501

        :return: The update_fields of this TextSaveOptionsData.  # noqa: E501
        :rtype: bool
        """
        return self._update_fields

    @update_fields.setter
    def update_fields(self, update_fields):
        """Sets the update_fields of this TextSaveOptionsData.

        Gets or sets a value determining if fields should be updated before saving the document to a fixed page format. Default value for this property is true  # noqa: E501

        :param update_fields: The update_fields of this TextSaveOptionsData.  # noqa: E501
        :type: bool
        """
        self._update_fields = update_fields
    @property
    def encoding(self):
        """Gets the encoding of this TextSaveOptionsData.  # noqa: E501

        Specifies the encoding to use when exporting in plain text format  # noqa: E501

        :return: The encoding of this TextSaveOptionsData.  # noqa: E501
        :rtype: str
        """
        return self._encoding

    @encoding.setter
    def encoding(self, encoding):
        """Sets the encoding of this TextSaveOptionsData.

        Specifies the encoding to use when exporting in plain text format  # noqa: E501

        :param encoding: The encoding of this TextSaveOptionsData.  # noqa: E501
        :type: str
        """
        self._encoding = encoding
    @property
    def export_headers_footers(self):
        """Gets the export_headers_footers of this TextSaveOptionsData.  # noqa: E501

        Specifies whether to output headers and footers when exporting in plain text format  # noqa: E501

        :return: The export_headers_footers of this TextSaveOptionsData.  # noqa: E501
        :rtype: bool
        """
        return self._export_headers_footers

    @export_headers_footers.setter
    def export_headers_footers(self, export_headers_footers):
        """Sets the export_headers_footers of this TextSaveOptionsData.

        Specifies whether to output headers and footers when exporting in plain text format  # noqa: E501

        :param export_headers_footers: The export_headers_footers of this TextSaveOptionsData.  # noqa: E501
        :type: bool
        """
        self._export_headers_footers = export_headers_footers
    @property
    def force_page_breaks(self):
        """Gets the force_page_breaks of this TextSaveOptionsData.  # noqa: E501

        Allows to specify whether the page breaks should be preserved during export. The default value is false.  # noqa: E501

        :return: The force_page_breaks of this TextSaveOptionsData.  # noqa: E501
        :rtype: bool
        """
        return self._force_page_breaks

    @force_page_breaks.setter
    def force_page_breaks(self, force_page_breaks):
        """Sets the force_page_breaks of this TextSaveOptionsData.

        Allows to specify whether the page breaks should be preserved during export. The default value is false.  # noqa: E501

        :param force_page_breaks: The force_page_breaks of this TextSaveOptionsData.  # noqa: E501
        :type: bool
        """
        self._force_page_breaks = force_page_breaks
    @property
    def paragraph_break(self):
        """Gets the paragraph_break of this TextSaveOptionsData.  # noqa: E501

        Specifies the string to use as a paragraph break when exporting in plain text format  # noqa: E501

        :return: The paragraph_break of this TextSaveOptionsData.  # noqa: E501
        :rtype: str
        """
        return self._paragraph_break

    @paragraph_break.setter
    def paragraph_break(self, paragraph_break):
        """Sets the paragraph_break of this TextSaveOptionsData.

        Specifies the string to use as a paragraph break when exporting in plain text format  # noqa: E501

        :param paragraph_break: The paragraph_break of this TextSaveOptionsData.  # noqa: E501
        :type: str
        """
        self._paragraph_break = paragraph_break
    @property
    def preserve_table_layout(self):
        """Gets the preserve_table_layout of this TextSaveOptionsData.  # noqa: E501

        Specifies whether the program should attempt to preserve layout of tables when saving in the plain text format  # noqa: E501

        :return: The preserve_table_layout of this TextSaveOptionsData.  # noqa: E501
        :rtype: bool
        """
        return self._preserve_table_layout

    @preserve_table_layout.setter
    def preserve_table_layout(self, preserve_table_layout):
        """Sets the preserve_table_layout of this TextSaveOptionsData.

        Specifies whether the program should attempt to preserve layout of tables when saving in the plain text format  # noqa: E501

        :param preserve_table_layout: The preserve_table_layout of this TextSaveOptionsData.  # noqa: E501
        :type: bool
        """
        self._preserve_table_layout = preserve_table_layout
    @property
    def simplify_list_labels(self):
        """Gets the simplify_list_labels of this TextSaveOptionsData.  # noqa: E501

        Specifies whether the program should simplify list labels in case of complex label formatting not being adequately represented by plain text  # noqa: E501

        :return: The simplify_list_labels of this TextSaveOptionsData.  # noqa: E501
        :rtype: bool
        """
        return self._simplify_list_labels

    @simplify_list_labels.setter
    def simplify_list_labels(self, simplify_list_labels):
        """Sets the simplify_list_labels of this TextSaveOptionsData.

        Specifies whether the program should simplify list labels in case of complex label formatting not being adequately represented by plain text  # noqa: E501

        :param simplify_list_labels: The simplify_list_labels of this TextSaveOptionsData.  # noqa: E501
        :type: bool
        """
        self._simplify_list_labels = simplify_list_labels
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
        if not isinstance(other, TextSaveOptionsData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other