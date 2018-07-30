#
# --------------------------------------------------------------------------------------------------------------------
# <copyright company="Aspose" file="test_mail_merge_fields.py">
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
import asposewordscloud.models.requests
from test.base_test_context import BaseTestContext


class TestMailMergeFields(BaseTestContext):
    test_folder = 'DocumentActions/MailMerge'

    #
    # Test for getting document field names
    #
    def test_get_document_field_names(self):
        filename = 'test_multi_pages.docx'
        remote_name = 'TestGetDocumentFieldNames.docx'
        with open(os.path.join(self.local_common_folder, filename), 'rb') as f:
            file = f.read()
        self.storage_api.put_create(os.path.join(self.remote_test_folder, self.test_folder, remote_name), file)
        request = asposewordscloud.models.requests.GetDocumentFieldNamesRequest(remote_name,
                                                                              os.path.join(
                                                                                  self.remote_test_folder,
                                                                                  self.test_folder))
        result = self.words_api.get_document_field_names(request)
        self.assertTrue(result.code == 200, 'Error has occurred while get document field names')

    #
    # Test for inserting document field names
    #
    def test_put_document_field_names(self):
        file = os.path.join(self.local_test_folder, self.test_folder, 'SampleExecuteTemplate.docx')
        request = asposewordscloud.models.requests.PutDocumentFieldNamesRequest(file, True)
        result = self.words_api.put_document_field_names(request)
        self.assertTrue(result.code == 200, 'Error has occurred while put document field')