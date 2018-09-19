# coding: utf-8
# -----------------------------------------------------------------------------------
# <copyright company="Aspose" file="EpubSaveOptionsData.py">
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


class EpubSaveOptionsData(object):
    """Container class for epub save options.
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
        'allow_negative_indent': 'bool',
        'css_class_name_prefix': 'str',
        'css_style_sheet_file_name': 'str',
        'css_style_sheet_type': 'str',
        'document_split_criteria': 'str',
        'document_split_heading_level': 'int',
        'encoding': 'str',
        'export_document_properties': 'bool',
        'export_drop_down_form_field_as_text': 'bool',
        'export_font_resources': 'bool',
        'export_fonts_as_base64': 'bool',
        'export_headers_footers_mode': 'str',
        'export_images_as_base64': 'bool',
        'export_language_information': 'bool',
        'export_list_labels': 'str',
        'export_original_url_for_linked_images': 'bool',
        'export_page_margins': 'bool',
        'export_page_setup': 'bool',
        'export_relative_font_size': 'bool',
        'export_roundtrip_information': 'bool',
        'export_text_box_as_svg': 'bool',
        'export_text_input_form_field_as_text': 'bool',
        'export_toc_page_numbers': 'bool',
        'export_xhtml_transitional': 'bool',
        'font_resources_subsetting_size_threshold': 'int',
        'fonts_folder': 'str',
        'fonts_folder_alias': 'str',
        'html_version': 'str',
        'image_resolution': 'int',
        'images_folder': 'str',
        'images_folder_alias': 'str',
        'metafile_format': 'str',
        'office_math_output_mode': 'str',
        'pretty_format': 'bool',
        'resource_folder': 'str',
        'resource_folder_alias': 'str',
        'scale_image_to_shape_size': 'bool',
        'table_width_output_mode': 'str',
        'epub_navigation_map_level': 'int'
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
        'allow_negative_indent': 'AllowNegativeIndent',
        'css_class_name_prefix': 'CssClassNamePrefix',
        'css_style_sheet_file_name': 'CssStyleSheetFileName',
        'css_style_sheet_type': 'CssStyleSheetType',
        'document_split_criteria': 'DocumentSplitCriteria',
        'document_split_heading_level': 'DocumentSplitHeadingLevel',
        'encoding': 'Encoding',
        'export_document_properties': 'ExportDocumentProperties',
        'export_drop_down_form_field_as_text': 'ExportDropDownFormFieldAsText',
        'export_font_resources': 'ExportFontResources',
        'export_fonts_as_base64': 'ExportFontsAsBase64',
        'export_headers_footers_mode': 'ExportHeadersFootersMode',
        'export_images_as_base64': 'ExportImagesAsBase64',
        'export_language_information': 'ExportLanguageInformation',
        'export_list_labels': 'ExportListLabels',
        'export_original_url_for_linked_images': 'ExportOriginalUrlForLinkedImages',
        'export_page_margins': 'ExportPageMargins',
        'export_page_setup': 'ExportPageSetup',
        'export_relative_font_size': 'ExportRelativeFontSize',
        'export_roundtrip_information': 'ExportRoundtripInformation',
        'export_text_box_as_svg': 'ExportTextBoxAsSvg',
        'export_text_input_form_field_as_text': 'ExportTextInputFormFieldAsText',
        'export_toc_page_numbers': 'ExportTocPageNumbers',
        'export_xhtml_transitional': 'ExportXhtmlTransitional',
        'font_resources_subsetting_size_threshold': 'FontResourcesSubsettingSizeThreshold',
        'fonts_folder': 'FontsFolder',
        'fonts_folder_alias': 'FontsFolderAlias',
        'html_version': 'HtmlVersion',
        'image_resolution': 'ImageResolution',
        'images_folder': 'ImagesFolder',
        'images_folder_alias': 'ImagesFolderAlias',
        'metafile_format': 'MetafileFormat',
        'office_math_output_mode': 'OfficeMathOutputMode',
        'pretty_format': 'PrettyFormat',
        'resource_folder': 'ResourceFolder',
        'resource_folder_alias': 'ResourceFolderAlias',
        'scale_image_to_shape_size': 'ScaleImageToShapeSize',
        'table_width_output_mode': 'TableWidthOutputMode',
        'epub_navigation_map_level': 'EpubNavigationMapLevel'
    }

    def __init__(self, color_mode=None, save_format=None, file_name=None, dml_rendering_mode=None, dml_effects_rendering_mode=None, zip_output=None, update_last_saved_time_property=None, update_sdt_content=None, update_fields=None, allow_negative_indent=None, css_class_name_prefix=None, css_style_sheet_file_name=None, css_style_sheet_type=None, document_split_criteria=None, document_split_heading_level=None, encoding=None, export_document_properties=None, export_drop_down_form_field_as_text=None, export_font_resources=None, export_fonts_as_base64=None, export_headers_footers_mode=None, export_images_as_base64=None, export_language_information=None, export_list_labels=None, export_original_url_for_linked_images=None, export_page_margins=None, export_page_setup=None, export_relative_font_size=None, export_roundtrip_information=None, export_text_box_as_svg=None, export_text_input_form_field_as_text=None, export_toc_page_numbers=None, export_xhtml_transitional=None, font_resources_subsetting_size_threshold=None, fonts_folder=None, fonts_folder_alias=None, html_version=None, image_resolution=None, images_folder=None, images_folder_alias=None, metafile_format=None, office_math_output_mode=None, pretty_format=None, resource_folder=None, resource_folder_alias=None, scale_image_to_shape_size=None, table_width_output_mode=None, epub_navigation_map_level=None):  # noqa: E501
        """EpubSaveOptionsData - a model defined in Swagger"""  # noqa: E501

        self._color_mode = None
        self._save_format = None
        self._file_name = None
        self._dml_rendering_mode = None
        self._dml_effects_rendering_mode = None
        self._zip_output = None
        self._update_last_saved_time_property = None
        self._update_sdt_content = None
        self._update_fields = None
        self._allow_negative_indent = None
        self._css_class_name_prefix = None
        self._css_style_sheet_file_name = None
        self._css_style_sheet_type = None
        self._document_split_criteria = None
        self._document_split_heading_level = None
        self._encoding = None
        self._export_document_properties = None
        self._export_drop_down_form_field_as_text = None
        self._export_font_resources = None
        self._export_fonts_as_base64 = None
        self._export_headers_footers_mode = None
        self._export_images_as_base64 = None
        self._export_language_information = None
        self._export_list_labels = None
        self._export_original_url_for_linked_images = None
        self._export_page_margins = None
        self._export_page_setup = None
        self._export_relative_font_size = None
        self._export_roundtrip_information = None
        self._export_text_box_as_svg = None
        self._export_text_input_form_field_as_text = None
        self._export_toc_page_numbers = None
        self._export_xhtml_transitional = None
        self._font_resources_subsetting_size_threshold = None
        self._fonts_folder = None
        self._fonts_folder_alias = None
        self._html_version = None
        self._image_resolution = None
        self._images_folder = None
        self._images_folder_alias = None
        self._metafile_format = None
        self._office_math_output_mode = None
        self._pretty_format = None
        self._resource_folder = None
        self._resource_folder_alias = None
        self._scale_image_to_shape_size = None
        self._table_width_output_mode = None
        self._epub_navigation_map_level = None
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
        if allow_negative_indent is not None:
            self.allow_negative_indent = allow_negative_indent
        if css_class_name_prefix is not None:
            self.css_class_name_prefix = css_class_name_prefix
        if css_style_sheet_file_name is not None:
            self.css_style_sheet_file_name = css_style_sheet_file_name
        if css_style_sheet_type is not None:
            self.css_style_sheet_type = css_style_sheet_type
        if document_split_criteria is not None:
            self.document_split_criteria = document_split_criteria
        if document_split_heading_level is not None:
            self.document_split_heading_level = document_split_heading_level
        if encoding is not None:
            self.encoding = encoding
        if export_document_properties is not None:
            self.export_document_properties = export_document_properties
        if export_drop_down_form_field_as_text is not None:
            self.export_drop_down_form_field_as_text = export_drop_down_form_field_as_text
        if export_font_resources is not None:
            self.export_font_resources = export_font_resources
        if export_fonts_as_base64 is not None:
            self.export_fonts_as_base64 = export_fonts_as_base64
        if export_headers_footers_mode is not None:
            self.export_headers_footers_mode = export_headers_footers_mode
        if export_images_as_base64 is not None:
            self.export_images_as_base64 = export_images_as_base64
        if export_language_information is not None:
            self.export_language_information = export_language_information
        if export_list_labels is not None:
            self.export_list_labels = export_list_labels
        if export_original_url_for_linked_images is not None:
            self.export_original_url_for_linked_images = export_original_url_for_linked_images
        if export_page_margins is not None:
            self.export_page_margins = export_page_margins
        if export_page_setup is not None:
            self.export_page_setup = export_page_setup
        if export_relative_font_size is not None:
            self.export_relative_font_size = export_relative_font_size
        if export_roundtrip_information is not None:
            self.export_roundtrip_information = export_roundtrip_information
        if export_text_box_as_svg is not None:
            self.export_text_box_as_svg = export_text_box_as_svg
        if export_text_input_form_field_as_text is not None:
            self.export_text_input_form_field_as_text = export_text_input_form_field_as_text
        if export_toc_page_numbers is not None:
            self.export_toc_page_numbers = export_toc_page_numbers
        if export_xhtml_transitional is not None:
            self.export_xhtml_transitional = export_xhtml_transitional
        if font_resources_subsetting_size_threshold is not None:
            self.font_resources_subsetting_size_threshold = font_resources_subsetting_size_threshold
        if fonts_folder is not None:
            self.fonts_folder = fonts_folder
        if fonts_folder_alias is not None:
            self.fonts_folder_alias = fonts_folder_alias
        if html_version is not None:
            self.html_version = html_version
        if image_resolution is not None:
            self.image_resolution = image_resolution
        if images_folder is not None:
            self.images_folder = images_folder
        if images_folder_alias is not None:
            self.images_folder_alias = images_folder_alias
        if metafile_format is not None:
            self.metafile_format = metafile_format
        if office_math_output_mode is not None:
            self.office_math_output_mode = office_math_output_mode
        if pretty_format is not None:
            self.pretty_format = pretty_format
        if resource_folder is not None:
            self.resource_folder = resource_folder
        if resource_folder_alias is not None:
            self.resource_folder_alias = resource_folder_alias
        if scale_image_to_shape_size is not None:
            self.scale_image_to_shape_size = scale_image_to_shape_size
        if table_width_output_mode is not None:
            self.table_width_output_mode = table_width_output_mode
        if epub_navigation_map_level is not None:
            self.epub_navigation_map_level = epub_navigation_map_level

    @property
    def color_mode(self):
        """Gets the color_mode of this EpubSaveOptionsData.  # noqa: E501

        Gets or sets a value determining how colors are rendered. { Normal | Grayscale}  # noqa: E501

        :return: The color_mode of this EpubSaveOptionsData.  # noqa: E501
        :rtype: str
        """
        return self._color_mode

    @color_mode.setter
    def color_mode(self, color_mode):
        """Sets the color_mode of this EpubSaveOptionsData.

        Gets or sets a value determining how colors are rendered. { Normal | Grayscale}  # noqa: E501

        :param color_mode: The color_mode of this EpubSaveOptionsData.  # noqa: E501
        :type: str
        """
        self._color_mode = color_mode
    @property
    def save_format(self):
        """Gets the save_format of this EpubSaveOptionsData.  # noqa: E501

        format of save  # noqa: E501

        :return: The save_format of this EpubSaveOptionsData.  # noqa: E501
        :rtype: str
        """
        return self._save_format

    @save_format.setter
    def save_format(self, save_format):
        """Sets the save_format of this EpubSaveOptionsData.

        format of save  # noqa: E501

        :param save_format: The save_format of this EpubSaveOptionsData.  # noqa: E501
        :type: str
        """
        self._save_format = save_format
    @property
    def file_name(self):
        """Gets the file_name of this EpubSaveOptionsData.  # noqa: E501

        name of destination file  # noqa: E501

        :return: The file_name of this EpubSaveOptionsData.  # noqa: E501
        :rtype: str
        """
        return self._file_name

    @file_name.setter
    def file_name(self, file_name):
        """Sets the file_name of this EpubSaveOptionsData.

        name of destination file  # noqa: E501

        :param file_name: The file_name of this EpubSaveOptionsData.  # noqa: E501
        :type: str
        """
        self._file_name = file_name
    @property
    def dml_rendering_mode(self):
        """Gets the dml_rendering_mode of this EpubSaveOptionsData.  # noqa: E501

        Gets or sets a value determining how DrawingML shapes are rendered. { Fallback | DrawingML }  # noqa: E501

        :return: The dml_rendering_mode of this EpubSaveOptionsData.  # noqa: E501
        :rtype: str
        """
        return self._dml_rendering_mode

    @dml_rendering_mode.setter
    def dml_rendering_mode(self, dml_rendering_mode):
        """Sets the dml_rendering_mode of this EpubSaveOptionsData.

        Gets or sets a value determining how DrawingML shapes are rendered. { Fallback | DrawingML }  # noqa: E501

        :param dml_rendering_mode: The dml_rendering_mode of this EpubSaveOptionsData.  # noqa: E501
        :type: str
        """
        self._dml_rendering_mode = dml_rendering_mode
    @property
    def dml_effects_rendering_mode(self):
        """Gets the dml_effects_rendering_mode of this EpubSaveOptionsData.  # noqa: E501

        Gets or sets a value determining how DrawingML effects are rendered. { Simplified | None | Fine }  # noqa: E501

        :return: The dml_effects_rendering_mode of this EpubSaveOptionsData.  # noqa: E501
        :rtype: str
        """
        return self._dml_effects_rendering_mode

    @dml_effects_rendering_mode.setter
    def dml_effects_rendering_mode(self, dml_effects_rendering_mode):
        """Sets the dml_effects_rendering_mode of this EpubSaveOptionsData.

        Gets or sets a value determining how DrawingML effects are rendered. { Simplified | None | Fine }  # noqa: E501

        :param dml_effects_rendering_mode: The dml_effects_rendering_mode of this EpubSaveOptionsData.  # noqa: E501
        :type: str
        """
        self._dml_effects_rendering_mode = dml_effects_rendering_mode
    @property
    def zip_output(self):
        """Gets the zip_output of this EpubSaveOptionsData.  # noqa: E501

        Controls zip output or not. Default value is false.  # noqa: E501

        :return: The zip_output of this EpubSaveOptionsData.  # noqa: E501
        :rtype: bool
        """
        return self._zip_output

    @zip_output.setter
    def zip_output(self, zip_output):
        """Sets the zip_output of this EpubSaveOptionsData.

        Controls zip output or not. Default value is false.  # noqa: E501

        :param zip_output: The zip_output of this EpubSaveOptionsData.  # noqa: E501
        :type: bool
        """
        self._zip_output = zip_output
    @property
    def update_last_saved_time_property(self):
        """Gets the update_last_saved_time_property of this EpubSaveOptionsData.  # noqa: E501

        Gets or sets a value determining whether the Aspose.Words.Properties.BuiltInDocumentProperties.LastSavedTime property is updated before saving.  # noqa: E501

        :return: The update_last_saved_time_property of this EpubSaveOptionsData.  # noqa: E501
        :rtype: bool
        """
        return self._update_last_saved_time_property

    @update_last_saved_time_property.setter
    def update_last_saved_time_property(self, update_last_saved_time_property):
        """Sets the update_last_saved_time_property of this EpubSaveOptionsData.

        Gets or sets a value determining whether the Aspose.Words.Properties.BuiltInDocumentProperties.LastSavedTime property is updated before saving.  # noqa: E501

        :param update_last_saved_time_property: The update_last_saved_time_property of this EpubSaveOptionsData.  # noqa: E501
        :type: bool
        """
        self._update_last_saved_time_property = update_last_saved_time_property
    @property
    def update_sdt_content(self):
        """Gets the update_sdt_content of this EpubSaveOptionsData.  # noqa: E501

        Gets or sets value determining whether content of  is updated before saving.  # noqa: E501

        :return: The update_sdt_content of this EpubSaveOptionsData.  # noqa: E501
        :rtype: bool
        """
        return self._update_sdt_content

    @update_sdt_content.setter
    def update_sdt_content(self, update_sdt_content):
        """Sets the update_sdt_content of this EpubSaveOptionsData.

        Gets or sets value determining whether content of  is updated before saving.  # noqa: E501

        :param update_sdt_content: The update_sdt_content of this EpubSaveOptionsData.  # noqa: E501
        :type: bool
        """
        self._update_sdt_content = update_sdt_content
    @property
    def update_fields(self):
        """Gets the update_fields of this EpubSaveOptionsData.  # noqa: E501

        Gets or sets a value determining if fields should be updated before saving the document to a fixed page format. Default value for this property is true  # noqa: E501

        :return: The update_fields of this EpubSaveOptionsData.  # noqa: E501
        :rtype: bool
        """
        return self._update_fields

    @update_fields.setter
    def update_fields(self, update_fields):
        """Sets the update_fields of this EpubSaveOptionsData.

        Gets or sets a value determining if fields should be updated before saving the document to a fixed page format. Default value for this property is true  # noqa: E501

        :param update_fields: The update_fields of this EpubSaveOptionsData.  # noqa: E501
        :type: bool
        """
        self._update_fields = update_fields
    @property
    def allow_negative_indent(self):
        """Gets the allow_negative_indent of this EpubSaveOptionsData.  # noqa: E501

        Specifies whether negative left and right indents of paragraphs are allowed (not normalized)  # noqa: E501

        :return: The allow_negative_indent of this EpubSaveOptionsData.  # noqa: E501
        :rtype: bool
        """
        return self._allow_negative_indent

    @allow_negative_indent.setter
    def allow_negative_indent(self, allow_negative_indent):
        """Sets the allow_negative_indent of this EpubSaveOptionsData.

        Specifies whether negative left and right indents of paragraphs are allowed (not normalized)  # noqa: E501

        :param allow_negative_indent: The allow_negative_indent of this EpubSaveOptionsData.  # noqa: E501
        :type: bool
        """
        self._allow_negative_indent = allow_negative_indent
    @property
    def css_class_name_prefix(self):
        """Gets the css_class_name_prefix of this EpubSaveOptionsData.  # noqa: E501

        Specifies a prefix which is added to all CSS class names. Default value is an empty string and generated CSS class names have no common prefix.  If this value is not empty, all CSS classes generated by Aspose.Words will start with the specified prefix.This might be useful, for example, if you add custom CSS to generated documents and want to prevent class name conflicts. If the value is not null or empty, it must be a valid CSS identifier.  # noqa: E501

        :return: The css_class_name_prefix of this EpubSaveOptionsData.  # noqa: E501
        :rtype: str
        """
        return self._css_class_name_prefix

    @css_class_name_prefix.setter
    def css_class_name_prefix(self, css_class_name_prefix):
        """Sets the css_class_name_prefix of this EpubSaveOptionsData.

        Specifies a prefix which is added to all CSS class names. Default value is an empty string and generated CSS class names have no common prefix.  If this value is not empty, all CSS classes generated by Aspose.Words will start with the specified prefix.This might be useful, for example, if you add custom CSS to generated documents and want to prevent class name conflicts. If the value is not null or empty, it must be a valid CSS identifier.  # noqa: E501

        :param css_class_name_prefix: The css_class_name_prefix of this EpubSaveOptionsData.  # noqa: E501
        :type: str
        """
        self._css_class_name_prefix = css_class_name_prefix
    @property
    def css_style_sheet_file_name(self):
        """Gets the css_style_sheet_file_name of this EpubSaveOptionsData.  # noqa: E501

        Specifies the name of the CSS file written when the document is exported to HTML  # noqa: E501

        :return: The css_style_sheet_file_name of this EpubSaveOptionsData.  # noqa: E501
        :rtype: str
        """
        return self._css_style_sheet_file_name

    @css_style_sheet_file_name.setter
    def css_style_sheet_file_name(self, css_style_sheet_file_name):
        """Sets the css_style_sheet_file_name of this EpubSaveOptionsData.

        Specifies the name of the CSS file written when the document is exported to HTML  # noqa: E501

        :param css_style_sheet_file_name: The css_style_sheet_file_name of this EpubSaveOptionsData.  # noqa: E501
        :type: str
        """
        self._css_style_sheet_file_name = css_style_sheet_file_name
    @property
    def css_style_sheet_type(self):
        """Gets the css_style_sheet_type of this EpubSaveOptionsData.  # noqa: E501

        Specifies how CSS styles are exported  # noqa: E501

        :return: The css_style_sheet_type of this EpubSaveOptionsData.  # noqa: E501
        :rtype: str
        """
        return self._css_style_sheet_type

    @css_style_sheet_type.setter
    def css_style_sheet_type(self, css_style_sheet_type):
        """Sets the css_style_sheet_type of this EpubSaveOptionsData.

        Specifies how CSS styles are exported  # noqa: E501

        :param css_style_sheet_type: The css_style_sheet_type of this EpubSaveOptionsData.  # noqa: E501
        :type: str
        """
        self._css_style_sheet_type = css_style_sheet_type
    @property
    def document_split_criteria(self):
        """Gets the document_split_criteria of this EpubSaveOptionsData.  # noqa: E501

        Specifies how the document should be split when saving  # noqa: E501

        :return: The document_split_criteria of this EpubSaveOptionsData.  # noqa: E501
        :rtype: str
        """
        return self._document_split_criteria

    @document_split_criteria.setter
    def document_split_criteria(self, document_split_criteria):
        """Sets the document_split_criteria of this EpubSaveOptionsData.

        Specifies how the document should be split when saving  # noqa: E501

        :param document_split_criteria: The document_split_criteria of this EpubSaveOptionsData.  # noqa: E501
        :type: str
        """
        self._document_split_criteria = document_split_criteria
    @property
    def document_split_heading_level(self):
        """Gets the document_split_heading_level of this EpubSaveOptionsData.  # noqa: E501

        Specifies the maximum level of headings at which to split the document  # noqa: E501

        :return: The document_split_heading_level of this EpubSaveOptionsData.  # noqa: E501
        :rtype: int
        """
        return self._document_split_heading_level

    @document_split_heading_level.setter
    def document_split_heading_level(self, document_split_heading_level):
        """Sets the document_split_heading_level of this EpubSaveOptionsData.

        Specifies the maximum level of headings at which to split the document  # noqa: E501

        :param document_split_heading_level: The document_split_heading_level of this EpubSaveOptionsData.  # noqa: E501
        :type: int
        """
        self._document_split_heading_level = document_split_heading_level
    @property
    def encoding(self):
        """Gets the encoding of this EpubSaveOptionsData.  # noqa: E501

        Specifies the encoding to use when exporting  # noqa: E501

        :return: The encoding of this EpubSaveOptionsData.  # noqa: E501
        :rtype: str
        """
        return self._encoding

    @encoding.setter
    def encoding(self, encoding):
        """Sets the encoding of this EpubSaveOptionsData.

        Specifies the encoding to use when exporting  # noqa: E501

        :param encoding: The encoding of this EpubSaveOptionsData.  # noqa: E501
        :type: str
        """
        self._encoding = encoding
    @property
    def export_document_properties(self):
        """Gets the export_document_properties of this EpubSaveOptionsData.  # noqa: E501

        Specifies whether to export built-in and custom document properties  # noqa: E501

        :return: The export_document_properties of this EpubSaveOptionsData.  # noqa: E501
        :rtype: bool
        """
        return self._export_document_properties

    @export_document_properties.setter
    def export_document_properties(self, export_document_properties):
        """Sets the export_document_properties of this EpubSaveOptionsData.

        Specifies whether to export built-in and custom document properties  # noqa: E501

        :param export_document_properties: The export_document_properties of this EpubSaveOptionsData.  # noqa: E501
        :type: bool
        """
        self._export_document_properties = export_document_properties
    @property
    def export_drop_down_form_field_as_text(self):
        """Gets the export_drop_down_form_field_as_text of this EpubSaveOptionsData.  # noqa: E501

        Controls how drop-down form fields are saved to HTML. Default value is false.  # noqa: E501

        :return: The export_drop_down_form_field_as_text of this EpubSaveOptionsData.  # noqa: E501
        :rtype: bool
        """
        return self._export_drop_down_form_field_as_text

    @export_drop_down_form_field_as_text.setter
    def export_drop_down_form_field_as_text(self, export_drop_down_form_field_as_text):
        """Sets the export_drop_down_form_field_as_text of this EpubSaveOptionsData.

        Controls how drop-down form fields are saved to HTML. Default value is false.  # noqa: E501

        :param export_drop_down_form_field_as_text: The export_drop_down_form_field_as_text of this EpubSaveOptionsData.  # noqa: E501
        :type: bool
        """
        self._export_drop_down_form_field_as_text = export_drop_down_form_field_as_text
    @property
    def export_font_resources(self):
        """Gets the export_font_resources of this EpubSaveOptionsData.  # noqa: E501

        Specifies whether font resources should be exported  # noqa: E501

        :return: The export_font_resources of this EpubSaveOptionsData.  # noqa: E501
        :rtype: bool
        """
        return self._export_font_resources

    @export_font_resources.setter
    def export_font_resources(self, export_font_resources):
        """Sets the export_font_resources of this EpubSaveOptionsData.

        Specifies whether font resources should be exported  # noqa: E501

        :param export_font_resources: The export_font_resources of this EpubSaveOptionsData.  # noqa: E501
        :type: bool
        """
        self._export_font_resources = export_font_resources
    @property
    def export_fonts_as_base64(self):
        """Gets the export_fonts_as_base64 of this EpubSaveOptionsData.  # noqa: E501

        Specifies whether fonts resources should be embedded to HTML in Base64 encoding.  Default is false.  # noqa: E501

        :return: The export_fonts_as_base64 of this EpubSaveOptionsData.  # noqa: E501
        :rtype: bool
        """
        return self._export_fonts_as_base64

    @export_fonts_as_base64.setter
    def export_fonts_as_base64(self, export_fonts_as_base64):
        """Sets the export_fonts_as_base64 of this EpubSaveOptionsData.

        Specifies whether fonts resources should be embedded to HTML in Base64 encoding.  Default is false.  # noqa: E501

        :param export_fonts_as_base64: The export_fonts_as_base64 of this EpubSaveOptionsData.  # noqa: E501
        :type: bool
        """
        self._export_fonts_as_base64 = export_fonts_as_base64
    @property
    def export_headers_footers_mode(self):
        """Gets the export_headers_footers_mode of this EpubSaveOptionsData.  # noqa: E501

        Specifies how headers and footers are output  # noqa: E501

        :return: The export_headers_footers_mode of this EpubSaveOptionsData.  # noqa: E501
        :rtype: str
        """
        return self._export_headers_footers_mode

    @export_headers_footers_mode.setter
    def export_headers_footers_mode(self, export_headers_footers_mode):
        """Sets the export_headers_footers_mode of this EpubSaveOptionsData.

        Specifies how headers and footers are output  # noqa: E501

        :param export_headers_footers_mode: The export_headers_footers_mode of this EpubSaveOptionsData.  # noqa: E501
        :type: str
        """
        self._export_headers_footers_mode = export_headers_footers_mode
    @property
    def export_images_as_base64(self):
        """Gets the export_images_as_base64 of this EpubSaveOptionsData.  # noqa: E501

        Specifies whether images are saved in Base64 format  # noqa: E501

        :return: The export_images_as_base64 of this EpubSaveOptionsData.  # noqa: E501
        :rtype: bool
        """
        return self._export_images_as_base64

    @export_images_as_base64.setter
    def export_images_as_base64(self, export_images_as_base64):
        """Sets the export_images_as_base64 of this EpubSaveOptionsData.

        Specifies whether images are saved in Base64 format  # noqa: E501

        :param export_images_as_base64: The export_images_as_base64 of this EpubSaveOptionsData.  # noqa: E501
        :type: bool
        """
        self._export_images_as_base64 = export_images_as_base64
    @property
    def export_language_information(self):
        """Gets the export_language_information of this EpubSaveOptionsData.  # noqa: E501

        Specifies whether language information is exported  # noqa: E501

        :return: The export_language_information of this EpubSaveOptionsData.  # noqa: E501
        :rtype: bool
        """
        return self._export_language_information

    @export_language_information.setter
    def export_language_information(self, export_language_information):
        """Sets the export_language_information of this EpubSaveOptionsData.

        Specifies whether language information is exported  # noqa: E501

        :param export_language_information: The export_language_information of this EpubSaveOptionsData.  # noqa: E501
        :type: bool
        """
        self._export_language_information = export_language_information
    @property
    def export_list_labels(self):
        """Gets the export_list_labels of this EpubSaveOptionsData.  # noqa: E501

        Controls how list labels are output  # noqa: E501

        :return: The export_list_labels of this EpubSaveOptionsData.  # noqa: E501
        :rtype: str
        """
        return self._export_list_labels

    @export_list_labels.setter
    def export_list_labels(self, export_list_labels):
        """Sets the export_list_labels of this EpubSaveOptionsData.

        Controls how list labels are output  # noqa: E501

        :param export_list_labels: The export_list_labels of this EpubSaveOptionsData.  # noqa: E501
        :type: str
        """
        self._export_list_labels = export_list_labels
    @property
    def export_original_url_for_linked_images(self):
        """Gets the export_original_url_for_linked_images of this EpubSaveOptionsData.  # noqa: E501

        Specifies whether original URL should be used as the URL of the linked images. Default value is false.  # noqa: E501

        :return: The export_original_url_for_linked_images of this EpubSaveOptionsData.  # noqa: E501
        :rtype: bool
        """
        return self._export_original_url_for_linked_images

    @export_original_url_for_linked_images.setter
    def export_original_url_for_linked_images(self, export_original_url_for_linked_images):
        """Sets the export_original_url_for_linked_images of this EpubSaveOptionsData.

        Specifies whether original URL should be used as the URL of the linked images. Default value is false.  # noqa: E501

        :param export_original_url_for_linked_images: The export_original_url_for_linked_images of this EpubSaveOptionsData.  # noqa: E501
        :type: bool
        """
        self._export_original_url_for_linked_images = export_original_url_for_linked_images
    @property
    def export_page_margins(self):
        """Gets the export_page_margins of this EpubSaveOptionsData.  # noqa: E501

        Specifies whether page margins is exported to HTML, MHTML or EPUB. Default is false.  # noqa: E501

        :return: The export_page_margins of this EpubSaveOptionsData.  # noqa: E501
        :rtype: bool
        """
        return self._export_page_margins

    @export_page_margins.setter
    def export_page_margins(self, export_page_margins):
        """Sets the export_page_margins of this EpubSaveOptionsData.

        Specifies whether page margins is exported to HTML, MHTML or EPUB. Default is false.  # noqa: E501

        :param export_page_margins: The export_page_margins of this EpubSaveOptionsData.  # noqa: E501
        :type: bool
        """
        self._export_page_margins = export_page_margins
    @property
    def export_page_setup(self):
        """Gets the export_page_setup of this EpubSaveOptionsData.  # noqa: E501

        Specifies whether page setup is exported  # noqa: E501

        :return: The export_page_setup of this EpubSaveOptionsData.  # noqa: E501
        :rtype: bool
        """
        return self._export_page_setup

    @export_page_setup.setter
    def export_page_setup(self, export_page_setup):
        """Sets the export_page_setup of this EpubSaveOptionsData.

        Specifies whether page setup is exported  # noqa: E501

        :param export_page_setup: The export_page_setup of this EpubSaveOptionsData.  # noqa: E501
        :type: bool
        """
        self._export_page_setup = export_page_setup
    @property
    def export_relative_font_size(self):
        """Gets the export_relative_font_size of this EpubSaveOptionsData.  # noqa: E501

        Specifies whether font sizes should be output in relative units when saving  # noqa: E501

        :return: The export_relative_font_size of this EpubSaveOptionsData.  # noqa: E501
        :rtype: bool
        """
        return self._export_relative_font_size

    @export_relative_font_size.setter
    def export_relative_font_size(self, export_relative_font_size):
        """Sets the export_relative_font_size of this EpubSaveOptionsData.

        Specifies whether font sizes should be output in relative units when saving  # noqa: E501

        :param export_relative_font_size: The export_relative_font_size of this EpubSaveOptionsData.  # noqa: E501
        :type: bool
        """
        self._export_relative_font_size = export_relative_font_size
    @property
    def export_roundtrip_information(self):
        """Gets the export_roundtrip_information of this EpubSaveOptionsData.  # noqa: E501

        Specifies whether to write the roundtrip information when saving to HTML Default value is true.  # noqa: E501

        :return: The export_roundtrip_information of this EpubSaveOptionsData.  # noqa: E501
        :rtype: bool
        """
        return self._export_roundtrip_information

    @export_roundtrip_information.setter
    def export_roundtrip_information(self, export_roundtrip_information):
        """Sets the export_roundtrip_information of this EpubSaveOptionsData.

        Specifies whether to write the roundtrip information when saving to HTML Default value is true.  # noqa: E501

        :param export_roundtrip_information: The export_roundtrip_information of this EpubSaveOptionsData.  # noqa: E501
        :type: bool
        """
        self._export_roundtrip_information = export_roundtrip_information
    @property
    def export_text_box_as_svg(self):
        """Gets the export_text_box_as_svg of this EpubSaveOptionsData.  # noqa: E501

        Controls how textboxes represented by Aspose.Words.Drawing.Shape are saved to HTML, MHTML or EPUB. Default value is false.    When set to true, exports textboxes as inline \"svg\" elements. When false, exports as \"image\" elements.  # noqa: E501

        :return: The export_text_box_as_svg of this EpubSaveOptionsData.  # noqa: E501
        :rtype: bool
        """
        return self._export_text_box_as_svg

    @export_text_box_as_svg.setter
    def export_text_box_as_svg(self, export_text_box_as_svg):
        """Sets the export_text_box_as_svg of this EpubSaveOptionsData.

        Controls how textboxes represented by Aspose.Words.Drawing.Shape are saved to HTML, MHTML or EPUB. Default value is false.    When set to true, exports textboxes as inline \"svg\" elements. When false, exports as \"image\" elements.  # noqa: E501

        :param export_text_box_as_svg: The export_text_box_as_svg of this EpubSaveOptionsData.  # noqa: E501
        :type: bool
        """
        self._export_text_box_as_svg = export_text_box_as_svg
    @property
    def export_text_input_form_field_as_text(self):
        """Gets the export_text_input_form_field_as_text of this EpubSaveOptionsData.  # noqa: E501

        Controls how text input form fields are saved  # noqa: E501

        :return: The export_text_input_form_field_as_text of this EpubSaveOptionsData.  # noqa: E501
        :rtype: bool
        """
        return self._export_text_input_form_field_as_text

    @export_text_input_form_field_as_text.setter
    def export_text_input_form_field_as_text(self, export_text_input_form_field_as_text):
        """Sets the export_text_input_form_field_as_text of this EpubSaveOptionsData.

        Controls how text input form fields are saved  # noqa: E501

        :param export_text_input_form_field_as_text: The export_text_input_form_field_as_text of this EpubSaveOptionsData.  # noqa: E501
        :type: bool
        """
        self._export_text_input_form_field_as_text = export_text_input_form_field_as_text
    @property
    def export_toc_page_numbers(self):
        """Gets the export_toc_page_numbers of this EpubSaveOptionsData.  # noqa: E501

        Specifies whether to write page numbers to table of contents when saving  # noqa: E501

        :return: The export_toc_page_numbers of this EpubSaveOptionsData.  # noqa: E501
        :rtype: bool
        """
        return self._export_toc_page_numbers

    @export_toc_page_numbers.setter
    def export_toc_page_numbers(self, export_toc_page_numbers):
        """Sets the export_toc_page_numbers of this EpubSaveOptionsData.

        Specifies whether to write page numbers to table of contents when saving  # noqa: E501

        :param export_toc_page_numbers: The export_toc_page_numbers of this EpubSaveOptionsData.  # noqa: E501
        :type: bool
        """
        self._export_toc_page_numbers = export_toc_page_numbers
    @property
    def export_xhtml_transitional(self):
        """Gets the export_xhtml_transitional of this EpubSaveOptionsData.  # noqa: E501

        Specifies whether to write the DOCTYPE declaration when saving  # noqa: E501

        :return: The export_xhtml_transitional of this EpubSaveOptionsData.  # noqa: E501
        :rtype: bool
        """
        return self._export_xhtml_transitional

    @export_xhtml_transitional.setter
    def export_xhtml_transitional(self, export_xhtml_transitional):
        """Sets the export_xhtml_transitional of this EpubSaveOptionsData.

        Specifies whether to write the DOCTYPE declaration when saving  # noqa: E501

        :param export_xhtml_transitional: The export_xhtml_transitional of this EpubSaveOptionsData.  # noqa: E501
        :type: bool
        """
        self._export_xhtml_transitional = export_xhtml_transitional
    @property
    def font_resources_subsetting_size_threshold(self):
        """Gets the font_resources_subsetting_size_threshold of this EpubSaveOptionsData.  # noqa: E501

        Controls which font resources need subsetting when saving  # noqa: E501

        :return: The font_resources_subsetting_size_threshold of this EpubSaveOptionsData.  # noqa: E501
        :rtype: int
        """
        return self._font_resources_subsetting_size_threshold

    @font_resources_subsetting_size_threshold.setter
    def font_resources_subsetting_size_threshold(self, font_resources_subsetting_size_threshold):
        """Sets the font_resources_subsetting_size_threshold of this EpubSaveOptionsData.

        Controls which font resources need subsetting when saving  # noqa: E501

        :param font_resources_subsetting_size_threshold: The font_resources_subsetting_size_threshold of this EpubSaveOptionsData.  # noqa: E501
        :type: int
        """
        self._font_resources_subsetting_size_threshold = font_resources_subsetting_size_threshold
    @property
    def fonts_folder(self):
        """Gets the fonts_folder of this EpubSaveOptionsData.  # noqa: E501

        Specifies the physical folder where fonts are saved when exporting a document  # noqa: E501

        :return: The fonts_folder of this EpubSaveOptionsData.  # noqa: E501
        :rtype: str
        """
        return self._fonts_folder

    @fonts_folder.setter
    def fonts_folder(self, fonts_folder):
        """Sets the fonts_folder of this EpubSaveOptionsData.

        Specifies the physical folder where fonts are saved when exporting a document  # noqa: E501

        :param fonts_folder: The fonts_folder of this EpubSaveOptionsData.  # noqa: E501
        :type: str
        """
        self._fonts_folder = fonts_folder
    @property
    def fonts_folder_alias(self):
        """Gets the fonts_folder_alias of this EpubSaveOptionsData.  # noqa: E501

        Specifies the name of the folder used to construct font URIs  # noqa: E501

        :return: The fonts_folder_alias of this EpubSaveOptionsData.  # noqa: E501
        :rtype: str
        """
        return self._fonts_folder_alias

    @fonts_folder_alias.setter
    def fonts_folder_alias(self, fonts_folder_alias):
        """Sets the fonts_folder_alias of this EpubSaveOptionsData.

        Specifies the name of the folder used to construct font URIs  # noqa: E501

        :param fonts_folder_alias: The fonts_folder_alias of this EpubSaveOptionsData.  # noqa: E501
        :type: str
        """
        self._fonts_folder_alias = fonts_folder_alias
    @property
    def html_version(self):
        """Gets the html_version of this EpubSaveOptionsData.  # noqa: E501

        Specifies version of HTML standard that should be used when saving the document to HTML or MHTML.   Default value is Aspose.Words.Saving.HtmlVersion.Xhtml.  # noqa: E501

        :return: The html_version of this EpubSaveOptionsData.  # noqa: E501
        :rtype: str
        """
        return self._html_version

    @html_version.setter
    def html_version(self, html_version):
        """Sets the html_version of this EpubSaveOptionsData.

        Specifies version of HTML standard that should be used when saving the document to HTML or MHTML.   Default value is Aspose.Words.Saving.HtmlVersion.Xhtml.  # noqa: E501

        :param html_version: The html_version of this EpubSaveOptionsData.  # noqa: E501
        :type: str
        """
        allowed_values = ["Xhtml", "Html5"]  # noqa: E501
        if not html_version.isdigit():	
            if html_version not in allowed_values:
                raise ValueError(
                    "Invalid value for `html_version` ({0}), must be one of {1}"  # noqa: E501
                    .format(html_version, allowed_values))
            self._html_version = html_version
        else:
            self._html_version = allowed_values[int(html_version) if six.PY3 else long(html_version)]
    @property
    def image_resolution(self):
        """Gets the image_resolution of this EpubSaveOptionsData.  # noqa: E501

        Specifies the output resolution for images when exporting  # noqa: E501

        :return: The image_resolution of this EpubSaveOptionsData.  # noqa: E501
        :rtype: int
        """
        return self._image_resolution

    @image_resolution.setter
    def image_resolution(self, image_resolution):
        """Sets the image_resolution of this EpubSaveOptionsData.

        Specifies the output resolution for images when exporting  # noqa: E501

        :param image_resolution: The image_resolution of this EpubSaveOptionsData.  # noqa: E501
        :type: int
        """
        self._image_resolution = image_resolution
    @property
    def images_folder(self):
        """Gets the images_folder of this EpubSaveOptionsData.  # noqa: E501

        Specifies the physical folder where images are saved when exporting a document  # noqa: E501

        :return: The images_folder of this EpubSaveOptionsData.  # noqa: E501
        :rtype: str
        """
        return self._images_folder

    @images_folder.setter
    def images_folder(self, images_folder):
        """Sets the images_folder of this EpubSaveOptionsData.

        Specifies the physical folder where images are saved when exporting a document  # noqa: E501

        :param images_folder: The images_folder of this EpubSaveOptionsData.  # noqa: E501
        :type: str
        """
        self._images_folder = images_folder
    @property
    def images_folder_alias(self):
        """Gets the images_folder_alias of this EpubSaveOptionsData.  # noqa: E501

        Specifies the name of the folder used to construct image URIs  # noqa: E501

        :return: The images_folder_alias of this EpubSaveOptionsData.  # noqa: E501
        :rtype: str
        """
        return self._images_folder_alias

    @images_folder_alias.setter
    def images_folder_alias(self, images_folder_alias):
        """Sets the images_folder_alias of this EpubSaveOptionsData.

        Specifies the name of the folder used to construct image URIs  # noqa: E501

        :param images_folder_alias: The images_folder_alias of this EpubSaveOptionsData.  # noqa: E501
        :type: str
        """
        self._images_folder_alias = images_folder_alias
    @property
    def metafile_format(self):
        """Gets the metafile_format of this EpubSaveOptionsData.  # noqa: E501

        Specifies in what format metafiles are saved when exporting to HTML, MHTML, or EPUB.  Default value is Aspose.Words.Saving.HtmlMetafileFormat.Png, meaning that metafiles are rendered to raster PNG images.  Metafiles are not natively displayed by HTML browsers. By default, Aspose.Words converts WMF and EMF images into PNG files when exporting to HTML.Other options are to convert metafiles to SVG images or to export them as is without conversion. Some image transforms, in particular image cropping, will not be applied to metafile images if they are exported to HTML without conversion.  # noqa: E501

        :return: The metafile_format of this EpubSaveOptionsData.  # noqa: E501
        :rtype: str
        """
        return self._metafile_format

    @metafile_format.setter
    def metafile_format(self, metafile_format):
        """Sets the metafile_format of this EpubSaveOptionsData.

        Specifies in what format metafiles are saved when exporting to HTML, MHTML, or EPUB.  Default value is Aspose.Words.Saving.HtmlMetafileFormat.Png, meaning that metafiles are rendered to raster PNG images.  Metafiles are not natively displayed by HTML browsers. By default, Aspose.Words converts WMF and EMF images into PNG files when exporting to HTML.Other options are to convert metafiles to SVG images or to export them as is without conversion. Some image transforms, in particular image cropping, will not be applied to metafile images if they are exported to HTML without conversion.  # noqa: E501

        :param metafile_format: The metafile_format of this EpubSaveOptionsData.  # noqa: E501
        :type: str
        """
        allowed_values = ["Png", "Svg", "EmfOrWmf"]  # noqa: E501
        if not metafile_format.isdigit():	
            if metafile_format not in allowed_values:
                raise ValueError(
                    "Invalid value for `metafile_format` ({0}), must be one of {1}"  # noqa: E501
                    .format(metafile_format, allowed_values))
            self._metafile_format = metafile_format
        else:
            self._metafile_format = allowed_values[int(metafile_format) if six.PY3 else long(metafile_format)]
    @property
    def office_math_output_mode(self):
        """Gets the office_math_output_mode of this EpubSaveOptionsData.  # noqa: E501

        Controls how OfficeMath objects are exported to HTML, MHTML or EPUB.  Default value is HtmlOfficeMathOutputMode.Image.  # noqa: E501

        :return: The office_math_output_mode of this EpubSaveOptionsData.  # noqa: E501
        :rtype: str
        """
        return self._office_math_output_mode

    @office_math_output_mode.setter
    def office_math_output_mode(self, office_math_output_mode):
        """Sets the office_math_output_mode of this EpubSaveOptionsData.

        Controls how OfficeMath objects are exported to HTML, MHTML or EPUB.  Default value is HtmlOfficeMathOutputMode.Image.  # noqa: E501

        :param office_math_output_mode: The office_math_output_mode of this EpubSaveOptionsData.  # noqa: E501
        :type: str
        """
        allowed_values = ["Image", "MathML", "Text"]  # noqa: E501
        if not office_math_output_mode.isdigit():	
            if office_math_output_mode not in allowed_values:
                raise ValueError(
                    "Invalid value for `office_math_output_mode` ({0}), must be one of {1}"  # noqa: E501
                    .format(office_math_output_mode, allowed_values))
            self._office_math_output_mode = office_math_output_mode
        else:
            self._office_math_output_mode = allowed_values[int(office_math_output_mode) if six.PY3 else long(office_math_output_mode)]
    @property
    def pretty_format(self):
        """Gets the pretty_format of this EpubSaveOptionsData.  # noqa: E501

        Specifies whether or not use pretty formats output  # noqa: E501

        :return: The pretty_format of this EpubSaveOptionsData.  # noqa: E501
        :rtype: bool
        """
        return self._pretty_format

    @pretty_format.setter
    def pretty_format(self, pretty_format):
        """Sets the pretty_format of this EpubSaveOptionsData.

        Specifies whether or not use pretty formats output  # noqa: E501

        :param pretty_format: The pretty_format of this EpubSaveOptionsData.  # noqa: E501
        :type: bool
        """
        self._pretty_format = pretty_format
    @property
    def resource_folder(self):
        """Gets the resource_folder of this EpubSaveOptionsData.  # noqa: E501

        Specifies a physical folder where all resources like images, fonts, and external CSS are saved when a document is exported to HTML. Default is an empty string.  # noqa: E501

        :return: The resource_folder of this EpubSaveOptionsData.  # noqa: E501
        :rtype: str
        """
        return self._resource_folder

    @resource_folder.setter
    def resource_folder(self, resource_folder):
        """Sets the resource_folder of this EpubSaveOptionsData.

        Specifies a physical folder where all resources like images, fonts, and external CSS are saved when a document is exported to HTML. Default is an empty string.  # noqa: E501

        :param resource_folder: The resource_folder of this EpubSaveOptionsData.  # noqa: E501
        :type: str
        """
        self._resource_folder = resource_folder
    @property
    def resource_folder_alias(self):
        """Gets the resource_folder_alias of this EpubSaveOptionsData.  # noqa: E501

        Specifies the name of the folder used to construct URIs of all resources written into an HTML document.  Default is an empty string.  # noqa: E501

        :return: The resource_folder_alias of this EpubSaveOptionsData.  # noqa: E501
        :rtype: str
        """
        return self._resource_folder_alias

    @resource_folder_alias.setter
    def resource_folder_alias(self, resource_folder_alias):
        """Sets the resource_folder_alias of this EpubSaveOptionsData.

        Specifies the name of the folder used to construct URIs of all resources written into an HTML document.  Default is an empty string.  # noqa: E501

        :param resource_folder_alias: The resource_folder_alias of this EpubSaveOptionsData.  # noqa: E501
        :type: str
        """
        self._resource_folder_alias = resource_folder_alias
    @property
    def scale_image_to_shape_size(self):
        """Gets the scale_image_to_shape_size of this EpubSaveOptionsData.  # noqa: E501

        Specifies whether images are scaled by Aspose.Words to the bounding shape size when exporting  # noqa: E501

        :return: The scale_image_to_shape_size of this EpubSaveOptionsData.  # noqa: E501
        :rtype: bool
        """
        return self._scale_image_to_shape_size

    @scale_image_to_shape_size.setter
    def scale_image_to_shape_size(self, scale_image_to_shape_size):
        """Sets the scale_image_to_shape_size of this EpubSaveOptionsData.

        Specifies whether images are scaled by Aspose.Words to the bounding shape size when exporting  # noqa: E501

        :param scale_image_to_shape_size: The scale_image_to_shape_size of this EpubSaveOptionsData.  # noqa: E501
        :type: bool
        """
        self._scale_image_to_shape_size = scale_image_to_shape_size
    @property
    def table_width_output_mode(self):
        """Gets the table_width_output_mode of this EpubSaveOptionsData.  # noqa: E501

        Controls how table, row and cell widths are exported  # noqa: E501

        :return: The table_width_output_mode of this EpubSaveOptionsData.  # noqa: E501
        :rtype: str
        """
        return self._table_width_output_mode

    @table_width_output_mode.setter
    def table_width_output_mode(self, table_width_output_mode):
        """Sets the table_width_output_mode of this EpubSaveOptionsData.

        Controls how table, row and cell widths are exported  # noqa: E501

        :param table_width_output_mode: The table_width_output_mode of this EpubSaveOptionsData.  # noqa: E501
        :type: str
        """
        self._table_width_output_mode = table_width_output_mode
    @property
    def epub_navigation_map_level(self):
        """Gets the epub_navigation_map_level of this EpubSaveOptionsData.  # noqa: E501

        Specifies the maximum level of headings populated to the navigation map when exporting  # noqa: E501

        :return: The epub_navigation_map_level of this EpubSaveOptionsData.  # noqa: E501
        :rtype: int
        """
        return self._epub_navigation_map_level

    @epub_navigation_map_level.setter
    def epub_navigation_map_level(self, epub_navigation_map_level):
        """Sets the epub_navigation_map_level of this EpubSaveOptionsData.

        Specifies the maximum level of headings populated to the navigation map when exporting  # noqa: E501

        :param epub_navigation_map_level: The epub_navigation_map_level of this EpubSaveOptionsData.  # noqa: E501
        :type: int
        """
        self._epub_navigation_map_level = epub_navigation_map_level
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
        if not isinstance(other, EpubSaveOptionsData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other