#
# --------------------------------------------------------------------------------------------------------------------
# <copyright company="Aspose" file="test_runs.py">
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


class TestRuns(BaseTestContext):
    test_folder = 'DocumentElements/Runs'

    #
    # Test for removing run
    #
    def test_delete_run(self):
        filename = 'Run.doc'
        remote_name = 'TestDeleteRun.docx'
        index = 0
        paragraph_path = 'paragraphs/1'

        with open(os.path.join(self.local_test_folder, self.test_folder, filename), 'rb') as f:
            file = f.read()
        self.storage_api.put_create(os.path.join(self.remote_test_folder, self.test_folder, remote_name), file)
        request = asposewordscloud.models.requests.DeleteRunRequest(remote_name, paragraph_path, index,
                                                                  os.path.join(
                                                                      self.remote_test_folder,
                                                                      self.test_folder))
        result = self.words_api.delete_run(request)
        self.assertTrue(result.code == 200, 'Error has occurred while delete run')

    #
    # Test for updating run
    #
    def test_post_run(self):
        filename = 'Run.doc'
        remote_name = 'TestPostRun.docx'
        index = 0
        paragraph_path = 'paragraphs/1'
        body = asposewordscloud.Run(text='Run with text')

        with open(os.path.join(self.local_test_folder, self.test_folder, filename), 'rb') as f:
            file = f.read()
        self.storage_api.put_create(os.path.join(self.remote_test_folder, self.test_folder, remote_name), file)
        request = asposewordscloud.models.requests.PostRunRequest(remote_name, body, paragraph_path, index,
                                                                os.path.join(
                                                                    self.remote_test_folder,
                                                                    self.test_folder))
        result = self.words_api.post_run(request)
        self.assertTrue(result.code == 200, 'Error has occurred while update run')

    #
    # Test for updating run
    #
    def test_put_run(self):
        filename = 'Run.doc'
        remote_name = 'TestPutRun.docx'
        paragraph_path = 'paragraphs/1'
        body = asposewordscloud.Run(text='Run with text')

        with open(os.path.join(self.local_test_folder, self.test_folder, filename), 'rb') as f:
            file = f.read()
        self.storage_api.put_create(os.path.join(self.remote_test_folder, self.test_folder, remote_name), file)
        request = asposewordscloud.models.requests.PutRunRequest(remote_name, paragraph_path, body,
                                                               os.path.join(
                                                                   self.remote_test_folder,
                                                                   self.test_folder))
        result = self.words_api.put_run(request)
        self.assertTrue(result.code == 200, 'Error has occurred while insert run')