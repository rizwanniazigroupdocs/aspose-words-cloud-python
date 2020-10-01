# coding: utf-8
# -----------------------------------------------------------------------------------
# <copyright company="Aspose" file="execute_mail_merge_online_request.py">
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

class ExecuteMailMergeOnlineRequest(object):
    """
    Request model for execute_mail_merge_online operation.
    Initializes a new instance.
    :param template File with template.
    :param data File with mailmerge data.
    :param with_regions With regions flag.
    :param cleanup Clean up options.
    :param document_file_name This file name will be used when resulting document has dynamic field for document file name {filename}. If it is not set, "template" will be used instead.
    """

    def __init__(self, template, data, with_regions=None, cleanup=None, document_file_name=None):
        self.template = template
        self.data = data
        self.with_regions = with_regions
        self.cleanup = cleanup
        self.document_file_name = document_file_name

    def create_http_request(self, api_client):
        # verify the required parameter 'template' is set
        if self.template is None:
            raise ValueError("Missing the required parameter `template` when calling `execute_mail_merge_online`")  # noqa: E501
        # verify the required parameter 'data' is set
        if self.data is None:
            raise ValueError("Missing the required parameter `data` when calling `execute_mail_merge_online`")  # noqa: E501

        path = '/v4.0/words/MailMerge'
        path_params = {}

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
        if self.with_regions is not None:
                query_params.append(('withRegions', self.with_regions))  # noqa: E501
        if self.cleanup is not None:
                query_params.append(('cleanup', self.cleanup))  # noqa: E501
        if self.document_file_name is not None:
                query_params.append(('documentFileName', self.document_file_name))  # noqa: E501

        header_params = {}
        # HTTP header `Content-Type`
        header_params['Content-Type'] = api_client.select_header_content_type(  # noqa: E501
            ['multipart/form-data'])  # noqa: E501

        form_params = []
        if self.template is not None:
            form_params.append(['template', self.template, 'file'])  # noqa: E501
        if self.data is not None:
            form_params.append(['data', self.data, 'file'])  # noqa: E501

        body_params = None
        return {
            "method": "PUT",
            "path": path,
            "query_params": query_params,
            "header_params": header_params,
            "form_params": form_params,
            "body": body_params,
            "collection_formats": collection_formats,
            "response_type": 'file'  # noqa: E501
        }

    def get_response_type(self):
        return 'file'  # noqa: E501