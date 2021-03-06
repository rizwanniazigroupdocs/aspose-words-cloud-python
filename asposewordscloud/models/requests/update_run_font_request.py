# coding: utf-8
# -----------------------------------------------------------------------------------
# <copyright company="Aspose" file="update_run_font_request.py">
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

from six.moves.urllib.parse import quote

class UpdateRunFontRequest(object):
    """
    Request model for update_run_font operation.
    Initializes a new instance.
    :param name The filename of the input document.
    :param font_dto The font properties of a Run object.
    :param paragraph_path The path to the paragraph in the document tree.
    :param index Object index.
    :param folder Original document folder.
    :param storage Original document storage.
    :param load_encoding Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML.
    :param password Password for opening an encrypted document.
    :param dest_file_name Result path of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document.
    :param revision_author Initials of the author to use for revisions.If you set this parameter and then make some changes to the document programmatically, save the document and later open the document in MS Word you will see these changes as revisions.
    :param revision_date_time The date and time to use for revisions.
    """

    def __init__(self, name, font_dto, paragraph_path, index, folder=None, storage=None, load_encoding=None, password=None, dest_file_name=None, revision_author=None, revision_date_time=None):
        self.name = name
        self.font_dto = font_dto
        self.paragraph_path = paragraph_path
        self.index = index
        self.folder = folder
        self.storage = storage
        self.load_encoding = load_encoding
        self.password = password
        self.dest_file_name = dest_file_name
        self.revision_author = revision_author
        self.revision_date_time = revision_date_time

    def create_http_request(self, api_client):
        # verify the required parameter 'name' is set
        if self.name is None:
            raise ValueError("Missing the required parameter `name` when calling `update_run_font`")  # noqa: E501
        # verify the required parameter 'font_dto' is set
        if self.font_dto is None:
            raise ValueError("Missing the required parameter `font_dto` when calling `update_run_font`")  # noqa: E501
        # verify the required parameter 'paragraph_path' is set
        if self.paragraph_path is None:
            raise ValueError("Missing the required parameter `paragraph_path` when calling `update_run_font`")  # noqa: E501
        # verify the required parameter 'index' is set
        if self.index is None:
            raise ValueError("Missing the required parameter `index` when calling `update_run_font`")  # noqa: E501

        path = '/v4.0/words/{name}/{paragraphPath}/runs/{index}/font'
        path_params = {}
        if self.name is not None:
            path_params['name'] = self.name  # noqa: E501
        else:
            path_params['name'] = ''  # noqa: E501
        if self.paragraph_path is not None:
            path_params['paragraphPath'] = self.paragraph_path  # noqa: E501
        else:
            path_params['paragraphPath'] = ''  # noqa: E501
        if self.index is not None:
            path_params['index'] = self.index  # noqa: E501
        else:
            path_params['index'] = ''  # noqa: E501

        # path parameters
        collection_formats = {}
        if path_params:
            path_params = api_client.sanitize_for_serialization(path_params)
            path_params = api_client.parameters_to_tuples(path_params, collection_formats)
            for k, v in path_params:
                # specified safe chars, encode everything
                path = path.replace(
                    '{%s}' % k,
                    quote(str(v), safe=api_client.configuration.safe_chars_for_path_param)
                )

        # remove optional path parameters
        path = path.replace('//', '/')

        query_params = []
        if self.folder is not None:
                query_params.append(('folder', self.folder))  # noqa: E501
        if self.storage is not None:
                query_params.append(('storage', self.storage))  # noqa: E501
        if self.load_encoding is not None:
                query_params.append(('loadEncoding', self.load_encoding))  # noqa: E501
        if self.password is not None:
                query_params.append(('password', self.password))  # noqa: E501
        if self.dest_file_name is not None:
                query_params.append(('destFileName', self.dest_file_name))  # noqa: E501
        if self.revision_author is not None:
                query_params.append(('revisionAuthor', self.revision_author))  # noqa: E501
        if self.revision_date_time is not None:
                query_params.append(('revisionDateTime', self.revision_date_time))  # noqa: E501

        header_params = {}
        # HTTP header `Content-Type`
        header_params['Content-Type'] = api_client.select_header_content_type(  # noqa: E501
            ['application/xml', 'application/json'])  # noqa: E501

        form_params = []

        body_params = None
        if self.font_dto is not None:
            body_params = self.font_dto

        return {
            "method": "PUT",
            "path": path,
            "query_params": query_params,
            "header_params": header_params,
            "form_params": form_params,
            "body": body_params,
            "collection_formats": collection_formats,
            "response_type": 'FontResponse'  # noqa: E501
        }

    def get_response_type(self):
        return 'FontResponse'  # noqa: E501