#
# --------------------------------------------------------------------------------------------------------------------
# <copyright company="Aspose" file="test_convert_document.py">
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
# --------------------------------------------------------------------------------------------------------------------
#

import os
import wordspythonsdk.models.requests
from test.base_test_context import BaseTestContext


class TestConvertDocument(BaseTestContext):
    test_folder = 'DocumentActions/ConvertDocument'

    #
    # Test for saving document with specified format
    #
    def test_post_document_save_as(self):
        filename = 'test_multi_pages.docx'
        remote_name = 'TestPostDocumentSaveAs.docx'
        dest_name = os.path.join(self.remote_test_out, 'TestPostDocumentSaveAs.pdf')
        save_options = wordspythonsdk.SaveOptionsData(save_format='pdf', file_name=dest_name)
        with open(os.path.join(self.local_common_folder, filename), 'rb') as f:
            file = f.read()
        self.storage_api.put_create(os.path.join(self.remote_test_folder, self.test_folder, remote_name), file)

        request = wordspythonsdk.models.requests.PostDocumentSaveAsRequest(remote_name, save_options,
                                                                           os.path.join(self.remote_test_folder,
                                                                                        self.test_folder))
        result = self.words_api.post_document_save_as(request)
        self.assertTrue(result.code == 200, 'Error has occurred while convert document')

    #
    # Test for saving document with specified format
    #
    def test_post_save_document_as_from_pdf_to_doc(self):
        filename = '45.pdf'
        remote_name = 'TestPostDocumentSaveAsFromPdfToDoc.docx'
        dest_name = os.path.join(self.remote_test_out, 'TestPostDocumentSaveAs.docx')
        save_options = wordspythonsdk.SaveOptionsData(save_format='docx', file_name=dest_name)
        with open(os.path.join(self.local_test_folder, self.test_folder, filename), 'rb') as f:
            file = f.read()
        self.storage_api.put_create(os.path.join(self.remote_test_folder, self.test_folder, remote_name), file)

        request = wordspythonsdk.models.requests.PostDocumentSaveAsRequest(remote_name, save_options,
                                                                           os.path.join(self.remote_test_folder,
                                                                                        self.test_folder),
                                                                           dest_file_name=dest_name)
        result = self.words_api.post_document_save_as(request)
        self.assertTrue(result.code == 200, 'Error has occurred while convert document')

    #
    # Test for document conversion without storage
    #
    def test_put_convert_document(self):
        _format = 'pdf'
        filename = 'test_multi_pages.docx'
        request = wordspythonsdk.models.requests.PutConvertDocumentRequest(os.path.join(self.local_common_folder,
                                                                                        filename),
                                                                           _format)
        result = self.words_api.put_convert_document(request)
        self.assertTrue(len(result) > 0, 'Error has occurred while convert document')

    #
    # Test for saving document with specified format
    #
    def test_put_document_save_as_tiff(self):
        filename = '45.pdf'
        remote_name = 'TestPutDocumentSaveAsTiff.docx'
        dest_name = os.path.join(self.remote_test_out, 'TestPostDocumentSaveAsTiff.tiff')
        save_options = wordspythonsdk.SaveOptionsData(save_format='tiff', file_name=dest_name)
        with open(os.path.join(self.local_test_folder, self.test_folder, filename), 'rb') as f:
            file = f.read()
        self.storage_api.put_create(os.path.join(self.remote_test_folder, self.test_folder, remote_name), file)

        request = wordspythonsdk.models.requests.PutDocumentSaveAsTiffRequest(remote_name, save_options,
                                                                              os.path.join(self.remote_test_folder,
                                                                                           self.test_folder),
                                                                              dest_file_name=dest_name)
        result = self.words_api.put_document_save_as_tiff(request)
        self.assertTrue(result.code == 200, 'Error has occurred while convert document')

    #
    # Test for saving document with specified format
    #
    def test_get_document_with_format(self):
        filename = 'test_multi_pages.docx'
        remote_name = 'TestGetDocumentWithFormat.docx'
        _format = 'text'
        with open(os.path.join(self.local_common_folder, filename), 'rb') as f:
            file = f.read()
        self.storage_api.put_create(os.path.join(self.remote_test_folder, self.test_folder, remote_name), file)
        request = wordspythonsdk.models.requests.GetDocumentWithFormatRequest(remote_name, _format,
                                                                              os.path.join(self.remote_test_folder,
                                                                                           self.test_folder))
        result = self.words_api.get_document_with_format(request)
        self.assertTrue(len(result) > 0, 'Error has occurred while convert document')

    #
    # Test for saving document with specified format
    #
    def test_get_document_with_format_and_out_path(self):
        filename = 'test_multi_pages.docx'
        remote_name = 'TestGetDocumentWithFormat.docx'
        _format = 'text'
        out_path = os.path.join(self.remote_test_out, remote_name)
        with open(os.path.join(self.local_common_folder, filename), 'rb') as f:
            file = f.read()
        self.storage_api.put_create(os.path.join(self.remote_test_folder, self.test_folder, remote_name), file)
        request = wordspythonsdk.models.requests.GetDocumentWithFormatRequest(remote_name, _format,
                                                                              os.path.join(self.remote_test_folder,
                                                                                           self.test_folder),
                                                                              out_path=out_path)
        result = self.words_api.get_document_with_format(request)
        self.assertTrue(len(result) > 0, 'Error has occurred while convert document')
