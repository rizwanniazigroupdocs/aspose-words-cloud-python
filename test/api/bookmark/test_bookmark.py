# -----------------------------------------------------------------------------------
# <copyright company="Aspose" file="test_bookmark.py">
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
# Example of how to get all bookmarks from document.
#
class TestBookmark(BaseTestContext):
    #
    # Test for getting bookmarks from document.
    #
    def test_get_bookmarks(self):
        remoteDataFolder = self.remote_test_folder + '/DocumentElements/Bookmarks'
        localFile = 'Common/test_multi_pages.docx'
        remoteFileName = 'TestGetDocumentBookmarks.docx'

        self.upload_file(remoteDataFolder + '/' + remoteFileName, open(os.path.join(self.local_test_folder, localFile), 'rb'))

        request = asposewordscloud.models.requests.GetBookmarksRequest(name=remoteFileName, folder=remoteDataFolder)

        result = self.words_api.get_bookmarks(request)
        self.assertIsNotNone(result, 'Error has occurred.')
        self.assertIsNotNone(result.bookmarks, 'Validate GetBookmarks response')
        self.assertEqual(3, len(result.bookmarks.bookmark_list))
        self.assertEqual('aspose', result.bookmarks.bookmark_list[1].name)

    #
    # Test for getting bookmark by specified name.
    #
    def test_get_bookmark_by_name(self):
        remoteDataFolder = self.remote_test_folder + '/DocumentElements/Bookmarks'
        localFile = 'Common/test_multi_pages.docx'
        remoteFileName = 'TestGetDocumentBookmarkByName.docx'
        bookmarkName = 'aspose'

        self.upload_file(remoteDataFolder + '/' + remoteFileName, open(os.path.join(self.local_test_folder, localFile), 'rb'))

        request = asposewordscloud.models.requests.GetBookmarkByNameRequest(name=remoteFileName, bookmark_name=bookmarkName, folder=remoteDataFolder)

        result = self.words_api.get_bookmark_by_name(request)
        self.assertIsNotNone(result, 'Error has occurred.')
        self.assertIsNotNone(result.bookmark, 'Validate GetBookmarkByName response')
        self.assertEqual(bookmarkName, result.bookmark.name)

    #
    # Test for updating existed bookmark.
    #
    def test_update_bookmark(self):
        remoteDataFolder = self.remote_test_folder + '/DocumentElements/Bookmarks'
        localFile = 'Common/test_multi_pages.docx'
        remoteFileName = 'TestUpdateDocumentBookmark.docx'
        bookmarkName = 'aspose'
        bookmarkText = 'This will be the text for Aspose'

        self.upload_file(remoteDataFolder + '/' + remoteFileName, open(os.path.join(self.local_test_folder, localFile), 'rb'))

        requestBookmarkData = asposewordscloud.BookmarkData(name=bookmarkName, text=bookmarkText)
        request = asposewordscloud.models.requests.UpdateBookmarkRequest(name=remoteFileName, bookmark_data=requestBookmarkData, bookmark_name=bookmarkName, folder=remoteDataFolder, dest_file_name=self.remote_test_out + '/' + remoteFileName)

        result = self.words_api.update_bookmark(request)
        self.assertIsNotNone(result, 'Error has occurred.')
        self.assertIsNotNone(result.bookmark, 'Validate UpdateBookmark response')
        self.assertEqual(bookmarkName, result.bookmark.name)
        self.assertEqual(bookmarkText, result.bookmark.text)
