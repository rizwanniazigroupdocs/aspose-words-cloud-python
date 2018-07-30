# coding: utf-8
# -----------------------------------------------------------------------------------
# <copyright company="Aspose" file="SvgSaveOptionsData.py">
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


class SvgSaveOptionsData(object):
    """container class for svg save options
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
        'jpeg_quality': 'int',
        'metafile_rendering_options': 'MetafileRenderingOptionsData',
        'numeral_format': 'str',
        'optimize_output': 'bool',
        'page_count': 'int',
        'page_index': 'int',
        'export_embedded_images': 'bool',
        'fit_to_view_port': 'bool',
        'resources_folder': 'str',
        'resources_folder_alias': 'str',
        'show_page_border': 'bool',
        'text_output_mode': 'str'
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
        'jpeg_quality': 'JpegQuality',
        'metafile_rendering_options': 'MetafileRenderingOptions',
        'numeral_format': 'NumeralFormat',
        'optimize_output': 'OptimizeOutput',
        'page_count': 'PageCount',
        'page_index': 'PageIndex',
        'export_embedded_images': 'ExportEmbeddedImages',
        'fit_to_view_port': 'FitToViewPort',
        'resources_folder': 'ResourcesFolder',
        'resources_folder_alias': 'ResourcesFolderAlias',
        'show_page_border': 'ShowPageBorder',
        'text_output_mode': 'TextOutputMode'
    }

    def __init__(self, color_mode=None, save_format=None, file_name=None, dml_rendering_mode=None, dml_effects_rendering_mode=None, zip_output=None, update_last_saved_time_property=None, update_sdt_content=None, update_fields=None, jpeg_quality=None, metafile_rendering_options=None, numeral_format=None, optimize_output=None, page_count=None, page_index=None, export_embedded_images=None, fit_to_view_port=None, resources_folder=None, resources_folder_alias=None, show_page_border=None, text_output_mode=None):  # noqa: E501
        """SvgSaveOptionsData - a model defined in Swagger"""  # noqa: E501

        self._color_mode = None
        self._save_format = None
        self._file_name = None
        self._dml_rendering_mode = None
        self._dml_effects_rendering_mode = None
        self._zip_output = None
        self._update_last_saved_time_property = None
        self._update_sdt_content = None
        self._update_fields = None
        self._jpeg_quality = None
        self._metafile_rendering_options = None
        self._numeral_format = None
        self._optimize_output = None
        self._page_count = None
        self._page_index = None
        self._export_embedded_images = None
        self._fit_to_view_port = None
        self._resources_folder = None
        self._resources_folder_alias = None
        self._show_page_border = None
        self._text_output_mode = None
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
        if jpeg_quality is not None:
            self.jpeg_quality = jpeg_quality
        if metafile_rendering_options is not None:
            self.metafile_rendering_options = metafile_rendering_options
        if numeral_format is not None:
            self.numeral_format = numeral_format
        if optimize_output is not None:
            self.optimize_output = optimize_output
        if page_count is not None:
            self.page_count = page_count
        if page_index is not None:
            self.page_index = page_index
        if export_embedded_images is not None:
            self.export_embedded_images = export_embedded_images
        if fit_to_view_port is not None:
            self.fit_to_view_port = fit_to_view_port
        if resources_folder is not None:
            self.resources_folder = resources_folder
        if resources_folder_alias is not None:
            self.resources_folder_alias = resources_folder_alias
        if show_page_border is not None:
            self.show_page_border = show_page_border
        if text_output_mode is not None:
            self.text_output_mode = text_output_mode

    @property
    def color_mode(self):
        """Gets the color_mode of this SvgSaveOptionsData.  # noqa: E501

        Gets or sets a value determining how colors are rendered. { Normal | Grayscale}  # noqa: E501

        :return: The color_mode of this SvgSaveOptionsData.  # noqa: E501
        :rtype: str
        """
        return self._color_mode

    @color_mode.setter
    def color_mode(self, color_mode):
        """Sets the color_mode of this SvgSaveOptionsData.

        Gets or sets a value determining how colors are rendered. { Normal | Grayscale}  # noqa: E501

        :param color_mode: The color_mode of this SvgSaveOptionsData.  # noqa: E501
        :type: str
        """
        self._color_mode = color_mode
    @property
    def save_format(self):
        """Gets the save_format of this SvgSaveOptionsData.  # noqa: E501

        format of save  # noqa: E501

        :return: The save_format of this SvgSaveOptionsData.  # noqa: E501
        :rtype: str
        """
        return self._save_format

    @save_format.setter
    def save_format(self, save_format):
        """Sets the save_format of this SvgSaveOptionsData.

        format of save  # noqa: E501

        :param save_format: The save_format of this SvgSaveOptionsData.  # noqa: E501
        :type: str
        """
        self._save_format = save_format
    @property
    def file_name(self):
        """Gets the file_name of this SvgSaveOptionsData.  # noqa: E501

        name of destination file  # noqa: E501

        :return: The file_name of this SvgSaveOptionsData.  # noqa: E501
        :rtype: str
        """
        return self._file_name

    @file_name.setter
    def file_name(self, file_name):
        """Sets the file_name of this SvgSaveOptionsData.

        name of destination file  # noqa: E501

        :param file_name: The file_name of this SvgSaveOptionsData.  # noqa: E501
        :type: str
        """
        self._file_name = file_name
    @property
    def dml_rendering_mode(self):
        """Gets the dml_rendering_mode of this SvgSaveOptionsData.  # noqa: E501

        Gets or sets a value determining how DrawingML shapes are rendered. { Fallback | DrawingML }  # noqa: E501

        :return: The dml_rendering_mode of this SvgSaveOptionsData.  # noqa: E501
        :rtype: str
        """
        return self._dml_rendering_mode

    @dml_rendering_mode.setter
    def dml_rendering_mode(self, dml_rendering_mode):
        """Sets the dml_rendering_mode of this SvgSaveOptionsData.

        Gets or sets a value determining how DrawingML shapes are rendered. { Fallback | DrawingML }  # noqa: E501

        :param dml_rendering_mode: The dml_rendering_mode of this SvgSaveOptionsData.  # noqa: E501
        :type: str
        """
        self._dml_rendering_mode = dml_rendering_mode
    @property
    def dml_effects_rendering_mode(self):
        """Gets the dml_effects_rendering_mode of this SvgSaveOptionsData.  # noqa: E501

        Gets or sets a value determining how DrawingML effects are rendered. { Simplified | None | Fine }  # noqa: E501

        :return: The dml_effects_rendering_mode of this SvgSaveOptionsData.  # noqa: E501
        :rtype: str
        """
        return self._dml_effects_rendering_mode

    @dml_effects_rendering_mode.setter
    def dml_effects_rendering_mode(self, dml_effects_rendering_mode):
        """Sets the dml_effects_rendering_mode of this SvgSaveOptionsData.

        Gets or sets a value determining how DrawingML effects are rendered. { Simplified | None | Fine }  # noqa: E501

        :param dml_effects_rendering_mode: The dml_effects_rendering_mode of this SvgSaveOptionsData.  # noqa: E501
        :type: str
        """
        self._dml_effects_rendering_mode = dml_effects_rendering_mode
    @property
    def zip_output(self):
        """Gets the zip_output of this SvgSaveOptionsData.  # noqa: E501

        Controls zip output or not. Default value is false.  # noqa: E501

        :return: The zip_output of this SvgSaveOptionsData.  # noqa: E501
        :rtype: bool
        """
        return self._zip_output

    @zip_output.setter
    def zip_output(self, zip_output):
        """Sets the zip_output of this SvgSaveOptionsData.

        Controls zip output or not. Default value is false.  # noqa: E501

        :param zip_output: The zip_output of this SvgSaveOptionsData.  # noqa: E501
        :type: bool
        """
        self._zip_output = zip_output
    @property
    def update_last_saved_time_property(self):
        """Gets the update_last_saved_time_property of this SvgSaveOptionsData.  # noqa: E501

        Gets or sets a value determining whether the Aspose.Words.Properties.BuiltInDocumentProperties.LastSavedTime property is updated before saving.  # noqa: E501

        :return: The update_last_saved_time_property of this SvgSaveOptionsData.  # noqa: E501
        :rtype: bool
        """
        return self._update_last_saved_time_property

    @update_last_saved_time_property.setter
    def update_last_saved_time_property(self, update_last_saved_time_property):
        """Sets the update_last_saved_time_property of this SvgSaveOptionsData.

        Gets or sets a value determining whether the Aspose.Words.Properties.BuiltInDocumentProperties.LastSavedTime property is updated before saving.  # noqa: E501

        :param update_last_saved_time_property: The update_last_saved_time_property of this SvgSaveOptionsData.  # noqa: E501
        :type: bool
        """
        self._update_last_saved_time_property = update_last_saved_time_property
    @property
    def update_sdt_content(self):
        """Gets the update_sdt_content of this SvgSaveOptionsData.  # noqa: E501

        Gets or sets value determining whether content of  is updated before saving.  # noqa: E501

        :return: The update_sdt_content of this SvgSaveOptionsData.  # noqa: E501
        :rtype: bool
        """
        return self._update_sdt_content

    @update_sdt_content.setter
    def update_sdt_content(self, update_sdt_content):
        """Sets the update_sdt_content of this SvgSaveOptionsData.

        Gets or sets value determining whether content of  is updated before saving.  # noqa: E501

        :param update_sdt_content: The update_sdt_content of this SvgSaveOptionsData.  # noqa: E501
        :type: bool
        """
        self._update_sdt_content = update_sdt_content
    @property
    def update_fields(self):
        """Gets the update_fields of this SvgSaveOptionsData.  # noqa: E501

        Gets or sets a value determining if fields should be updated before saving the document to a fixed page format. Default value for this property is true  # noqa: E501

        :return: The update_fields of this SvgSaveOptionsData.  # noqa: E501
        :rtype: bool
        """
        return self._update_fields

    @update_fields.setter
    def update_fields(self, update_fields):
        """Sets the update_fields of this SvgSaveOptionsData.

        Gets or sets a value determining if fields should be updated before saving the document to a fixed page format. Default value for this property is true  # noqa: E501

        :param update_fields: The update_fields of this SvgSaveOptionsData.  # noqa: E501
        :type: bool
        """
        self._update_fields = update_fields
    @property
    def jpeg_quality(self):
        """Gets the jpeg_quality of this SvgSaveOptionsData.  # noqa: E501

        Determines the quality of the JPEG images inside PDF document.  # noqa: E501

        :return: The jpeg_quality of this SvgSaveOptionsData.  # noqa: E501
        :rtype: int
        """
        return self._jpeg_quality

    @jpeg_quality.setter
    def jpeg_quality(self, jpeg_quality):
        """Sets the jpeg_quality of this SvgSaveOptionsData.

        Determines the quality of the JPEG images inside PDF document.  # noqa: E501

        :param jpeg_quality: The jpeg_quality of this SvgSaveOptionsData.  # noqa: E501
        :type: int
        """
        self._jpeg_quality = jpeg_quality
    @property
    def metafile_rendering_options(self):
        """Gets the metafile_rendering_options of this SvgSaveOptionsData.  # noqa: E501

        Allows to specify metafile rendering options.  # noqa: E501

        :return: The metafile_rendering_options of this SvgSaveOptionsData.  # noqa: E501
        :rtype: MetafileRenderingOptionsData
        """
        return self._metafile_rendering_options

    @metafile_rendering_options.setter
    def metafile_rendering_options(self, metafile_rendering_options):
        """Sets the metafile_rendering_options of this SvgSaveOptionsData.

        Allows to specify metafile rendering options.  # noqa: E501

        :param metafile_rendering_options: The metafile_rendering_options of this SvgSaveOptionsData.  # noqa: E501
        :type: MetafileRenderingOptionsData
        """
        self._metafile_rendering_options = metafile_rendering_options
    @property
    def numeral_format(self):
        """Gets the numeral_format of this SvgSaveOptionsData.  # noqa: E501

        Indicates the symbol set that is used to represent numbers while rendering to fixed page formats  # noqa: E501

        :return: The numeral_format of this SvgSaveOptionsData.  # noqa: E501
        :rtype: str
        """
        return self._numeral_format

    @numeral_format.setter
    def numeral_format(self, numeral_format):
        """Sets the numeral_format of this SvgSaveOptionsData.

        Indicates the symbol set that is used to represent numbers while rendering to fixed page formats  # noqa: E501

        :param numeral_format: The numeral_format of this SvgSaveOptionsData.  # noqa: E501
        :type: str
        """
        self._numeral_format = numeral_format
    @property
    def optimize_output(self):
        """Gets the optimize_output of this SvgSaveOptionsData.  # noqa: E501

        Flag indicates whether it is required to optimize output of XPS.  If this flag is set redundant nested canvases and empty canvases are removed, also neighbor glyphs with the same formatting are concatenated.  Note: The accuracy of the content display may be affected if this property is set to true.  Default is false.  # noqa: E501

        :return: The optimize_output of this SvgSaveOptionsData.  # noqa: E501
        :rtype: bool
        """
        return self._optimize_output

    @optimize_output.setter
    def optimize_output(self, optimize_output):
        """Sets the optimize_output of this SvgSaveOptionsData.

        Flag indicates whether it is required to optimize output of XPS.  If this flag is set redundant nested canvases and empty canvases are removed, also neighbor glyphs with the same formatting are concatenated.  Note: The accuracy of the content display may be affected if this property is set to true.  Default is false.  # noqa: E501

        :param optimize_output: The optimize_output of this SvgSaveOptionsData.  # noqa: E501
        :type: bool
        """
        self._optimize_output = optimize_output
    @property
    def page_count(self):
        """Gets the page_count of this SvgSaveOptionsData.  # noqa: E501

        Determines number of pages to render  # noqa: E501

        :return: The page_count of this SvgSaveOptionsData.  # noqa: E501
        :rtype: int
        """
        return self._page_count

    @page_count.setter
    def page_count(self, page_count):
        """Sets the page_count of this SvgSaveOptionsData.

        Determines number of pages to render  # noqa: E501

        :param page_count: The page_count of this SvgSaveOptionsData.  # noqa: E501
        :type: int
        """
        self._page_count = page_count
    @property
    def page_index(self):
        """Gets the page_index of this SvgSaveOptionsData.  # noqa: E501

        Determines 0-based index of the first page to render  # noqa: E501

        :return: The page_index of this SvgSaveOptionsData.  # noqa: E501
        :rtype: int
        """
        return self._page_index

    @page_index.setter
    def page_index(self, page_index):
        """Sets the page_index of this SvgSaveOptionsData.

        Determines 0-based index of the first page to render  # noqa: E501

        :param page_index: The page_index of this SvgSaveOptionsData.  # noqa: E501
        :type: int
        """
        self._page_index = page_index
    @property
    def export_embedded_images(self):
        """Gets the export_embedded_images of this SvgSaveOptionsData.  # noqa: E501

        Specified whether images should be embedded into SVG document as base64  # noqa: E501

        :return: The export_embedded_images of this SvgSaveOptionsData.  # noqa: E501
        :rtype: bool
        """
        return self._export_embedded_images

    @export_embedded_images.setter
    def export_embedded_images(self, export_embedded_images):
        """Sets the export_embedded_images of this SvgSaveOptionsData.

        Specified whether images should be embedded into SVG document as base64  # noqa: E501

        :param export_embedded_images: The export_embedded_images of this SvgSaveOptionsData.  # noqa: E501
        :type: bool
        """
        self._export_embedded_images = export_embedded_images
    @property
    def fit_to_view_port(self):
        """Gets the fit_to_view_port of this SvgSaveOptionsData.  # noqa: E501

        Specifies if the output SVG should fill the available viewport area (browser window or container). When set to true width and height of output SVG are set to 100%.  # noqa: E501

        :return: The fit_to_view_port of this SvgSaveOptionsData.  # noqa: E501
        :rtype: bool
        """
        return self._fit_to_view_port

    @fit_to_view_port.setter
    def fit_to_view_port(self, fit_to_view_port):
        """Sets the fit_to_view_port of this SvgSaveOptionsData.

        Specifies if the output SVG should fill the available viewport area (browser window or container). When set to true width and height of output SVG are set to 100%.  # noqa: E501

        :param fit_to_view_port: The fit_to_view_port of this SvgSaveOptionsData.  # noqa: E501
        :type: bool
        """
        self._fit_to_view_port = fit_to_view_port
    @property
    def resources_folder(self):
        """Gets the resources_folder of this SvgSaveOptionsData.  # noqa: E501

        Specifies the physical folder where resources (images) are saved when exporting  # noqa: E501

        :return: The resources_folder of this SvgSaveOptionsData.  # noqa: E501
        :rtype: str
        """
        return self._resources_folder

    @resources_folder.setter
    def resources_folder(self, resources_folder):
        """Sets the resources_folder of this SvgSaveOptionsData.

        Specifies the physical folder where resources (images) are saved when exporting  # noqa: E501

        :param resources_folder: The resources_folder of this SvgSaveOptionsData.  # noqa: E501
        :type: str
        """
        self._resources_folder = resources_folder
    @property
    def resources_folder_alias(self):
        """Gets the resources_folder_alias of this SvgSaveOptionsData.  # noqa: E501

        Specifies the name of the folder used to construct image URIs  # noqa: E501

        :return: The resources_folder_alias of this SvgSaveOptionsData.  # noqa: E501
        :rtype: str
        """
        return self._resources_folder_alias

    @resources_folder_alias.setter
    def resources_folder_alias(self, resources_folder_alias):
        """Sets the resources_folder_alias of this SvgSaveOptionsData.

        Specifies the name of the folder used to construct image URIs  # noqa: E501

        :param resources_folder_alias: The resources_folder_alias of this SvgSaveOptionsData.  # noqa: E501
        :type: str
        """
        self._resources_folder_alias = resources_folder_alias
    @property
    def show_page_border(self):
        """Gets the show_page_border of this SvgSaveOptionsData.  # noqa: E501

        Show/hide page stepper  # noqa: E501

        :return: The show_page_border of this SvgSaveOptionsData.  # noqa: E501
        :rtype: bool
        """
        return self._show_page_border

    @show_page_border.setter
    def show_page_border(self, show_page_border):
        """Sets the show_page_border of this SvgSaveOptionsData.

        Show/hide page stepper  # noqa: E501

        :param show_page_border: The show_page_border of this SvgSaveOptionsData.  # noqa: E501
        :type: bool
        """
        self._show_page_border = show_page_border
    @property
    def text_output_mode(self):
        """Gets the text_output_mode of this SvgSaveOptionsData.  # noqa: E501

        Determines how text should be rendered  # noqa: E501

        :return: The text_output_mode of this SvgSaveOptionsData.  # noqa: E501
        :rtype: str
        """
        return self._text_output_mode

    @text_output_mode.setter
    def text_output_mode(self, text_output_mode):
        """Sets the text_output_mode of this SvgSaveOptionsData.

        Determines how text should be rendered  # noqa: E501

        :param text_output_mode: The text_output_mode of this SvgSaveOptionsData.  # noqa: E501
        :type: str
        """
        self._text_output_mode = text_output_mode
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
        if not isinstance(other, SvgSaveOptionsData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other