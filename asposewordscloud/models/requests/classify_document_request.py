# coding: utf-8
# -----------------------------------------------------------------------------------
# <copyright company="Aspose" file="classify_document_request.py">
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

class ClassifyDocumentRequest(object):
    """
    Request model for classify_document operation.
    Initializes a new instance.
    :param document_name The filename of the input document.
    :param folder Original document folder.
    :param storage Original document storage.
    :param load_encoding Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML.
    :param password Password for opening an encrypted document.
    :param best_classes_count The number of the best classes to return.
    :param taxonomy The taxonomy to use.
    """

    def __init__(self, document_name, folder=None, storage=None, load_encoding=None, password=None, best_classes_count=None, taxonomy=None):
        self.document_name = document_name
        self.folder = folder
        self.storage = storage
        self.load_encoding = load_encoding
        self.password = password
        self.best_classes_count = best_classes_count
        self.taxonomy = taxonomy

    def create_http_request(self, api_client):
        # verify the required parameter 'document_name' is set
        if self.document_name is None:
            raise ValueError("Missing the required parameter `document_name` when calling `classify_document`")  # noqa: E501

        path = '/v4.0/words/{documentName}/classify'
        path_params = {}
        if self.document_name is not None:
            path_params['documentName'] = self.document_name  # noqa: E501
        else:
            path_params['documentName'] = ''  # noqa: E501

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
        if self.best_classes_count is not None:
                query_params.append(('bestClassesCount', self.best_classes_count))  # noqa: E501
        if self.taxonomy is not None:
                query_params.append(('taxonomy', self.taxonomy))  # noqa: E501

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
            "response_type": 'ClassificationResponse'  # noqa: E501
        }

    def get_response_type(self):
        return 'ClassificationResponse'  # noqa: E501