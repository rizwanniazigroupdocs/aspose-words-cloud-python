# -----------------------------------------------------------------------------------
# <copyright company="Aspose" file="test_execute_mail_merge.py">
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

import os
import dateutil.parser
import asposewordscloud.models.requests
from test.base_test_context import BaseTestContext

#
# Example of how to perform mail merge.
#
class TestExecuteMailMerge(BaseTestContext):
    #
    # Test for executing mail merge online.
    #
    def test_execute_mail_merge_online(self):
        mailMergeFolder = 'DocumentActions/MailMerge'
        localDocumentFile = 'SampleExecuteTemplate.docx'
        localDataFile = 'SampleExecuteTemplateData.txt'

        request = asposewordscloud.models.requests.ExecuteMailMergeOnlineRequest(template=open(os.path.join(self.local_test_folder, mailMergeFolder + '/' + localDocumentFile), 'rb'), data=open(os.path.join(self.local_test_folder, mailMergeFolder + '/' + localDataFile), 'rb'))

        result = self.words_api.execute_mail_merge_online(request)
        self.assertIsNotNone(result, 'Error has occurred.')


    #
    # Test for executing mail merge.
    #
    def test_execute_mail_merge(self):
        remoteDataFolder = self.remote_test_folder + '/DocumentActions/MailMerge'
        mailMergeFolder = 'DocumentActions/MailMerge'
        localDocumentFile = 'SampleExecuteTemplate.docx'
        remoteFileName = 'TestExecuteMailMerge.docx'
        localDataFile = open(os.path.join(self.local_test_folder, mailMergeFolder + '/SampleMailMergeTemplateData.txt')).read()

        self.upload_file(remoteDataFolder + '/' + remoteFileName, open(os.path.join(self.local_test_folder, mailMergeFolder + '/' + localDocumentFile), 'rb'))

        request = asposewordscloud.models.requests.ExecuteMailMergeRequest(name=remoteFileName, data=localDataFile, folder=remoteDataFolder, with_regions=False, dest_file_name=self.remote_test_out + '/' + remoteFileName)

        result = self.words_api.execute_mail_merge(request)
        self.assertIsNotNone(result, 'Error has occurred.')
        self.assertIsNotNone(result.document, 'Validate ExecuteMailMerge response')
        self.assertEqual('TestExecuteMailMerge.docx', result.document.file_name)
