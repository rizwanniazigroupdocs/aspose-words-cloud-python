# -----------------------------------------------------------------------------------
# <copyright company="Aspose" file="test_hyperlink.py">
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
# Example of how to work with hyperlinks.
#
class TestHyperlink(BaseTestContext):
    #
    # Test for getting hyperlink by specified index.
    #
    def test_get_document_hyperlink_by_index(self):
        remoteDataFolder = self.remote_test_folder + '/DocumentElements/Hyperlink'
        localFile = 'Common/test_doc.docx'
        remoteFileName = 'TestGetDocumentHyperlinkByIndex.docx'

        self.upload_file(remoteDataFolder + '/' + remoteFileName, open(os.path.join(self.local_test_folder, localFile), 'rb'))

        request = asposewordscloud.models.requests.GetDocumentHyperlinkByIndexRequest(name=remoteFileName, hyperlink_index=0, folder=remoteDataFolder)

        result = self.words_api.get_document_hyperlink_by_index(request)
        self.assertIsNotNone(result, 'Error has occurred.')
        self.assertIsNotNone(result.hyperlink, 'Validate GetDocumentHyperlinkByIndex response')
        self.assertIsTrue(result.hyperlink.display_text.startswith('Aspose'))

    #
    # Test for getting hyperlinks.
    #
    def test_get_document_hyperlinks(self):
        remoteDataFolder = self.remote_test_folder + '/DocumentElements/Hyperlink'
        localFile = 'Common/test_doc.docx'
        remoteFileName = 'TestGetDocumentHyperlinks.docx'

        self.upload_file(remoteDataFolder + '/' + remoteFileName, open(os.path.join(self.local_test_folder, localFile), 'rb'))

        request = asposewordscloud.models.requests.GetDocumentHyperlinksRequest(name=remoteFileName, folder=remoteDataFolder)

        result = self.words_api.get_document_hyperlinks(request)
        self.assertIsNotNone(result, 'Error has occurred.')
        self.assertIsNotNone(result.hyperlinks, 'Validate GetDocumentHyperlinks response')
        self.assertIsNotNone(result.hyperlinks.hyperlink_list, 'Validate GetDocumentHyperlinks response')
        self.assertEqual(2, len(result.hyperlinks.hyperlink_list))
        self.assertIsTrue(result.hyperlinks.hyperlink_list[0].display_text.startswith('Aspose'))
