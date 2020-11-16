# coding: utf-8
# -----------------------------------------------------------------------------------
# <copyright company="Aspose" file="get_document_drawing_object_by_index_request.py">
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

class GetDocumentDrawingObjectByIndexRequest(object):
    """
    Request model for get_document_drawing_object_by_index operation.
    Initializes a new instance.
    :param name The filename of the input document.
    :param index Object index.
    :param node_path The path to the node in the document tree.
    :param folder Original document folder.
    :param storage Original document storage.
    :param load_encoding Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML.
    :param password Password for opening an encrypted document.
    """

    def __init__(self, name, index, node_path=None, folder=None, storage=None, load_encoding=None, password=None):
        self.name = name
        self.index = index
        self.node_path = node_path
        self.folder = folder
        self.storage = storage
        self.load_encoding = load_encoding
        self.password = password

    def create_http_request(self, api_client):
        # verify the required parameter 'name' is set
        if self.name is None:
            raise ValueError("Missing the required parameter `name` when calling `get_document_drawing_object_by_index`")  # noqa: E501
        # verify the required parameter 'index' is set
        if self.index is None:
            raise ValueError("Missing the required parameter `index` when calling `get_document_drawing_object_by_index`")  # noqa: E501

        path = '/v4.0/words/{name}/{nodePath}/drawingObjects/{index}'
        path_params = {}
        if self.name is not None:
            path_params['name'] = self.name  # noqa: E501
        else:
            path_params['name'] = ''  # noqa: E501
        if self.index is not None:
            path_params['index'] = self.index  # noqa: E501
        else:
            path_params['index'] = ''  # noqa: E501
        if self.node_path is not None:
            path_params['nodePath'] = self.node_path  # noqa: E501
        else:
            path_params['nodePath'] = ''  # noqa: E501

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

        header_params = {}

        form_params = []

        body_params = None
        return {
            "method": "GET",
            "path": path,
            "query_params": query_params,
            "header_params": header_params,
            "form_params": form_params,
            "body": body_params,
            "collection_formats": collection_formats,
            "response_type": 'DrawingObjectResponse'  # noqa: E501
        }

    def get_response_type(self):
        return 'DrawingObjectResponse'  # noqa: E501