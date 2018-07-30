#
# --------------------------------------------------------------------------------------------------------------------
# <copyright company="Aspose" file="test_drawing_objects.py">
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


class TestDrawingObjects(BaseTestContext):
    test_folder = 'DocumentElements/DrawingObjects'

    #
    # Test for getting drawing object
    #
    def test_get_document_drawing_object_by_index(self):
        filename = 'test_multi_pages.docx'
        remote_name = 'TestGetDocumentDrawingObjectByIndex.docx'
        index = 0
        with open(os.path.join(self.local_common_folder, filename), 'rb') as f:
            file = f.read()
        self.storage_api.put_create(os.path.join(self.remote_test_folder, self.test_folder, remote_name), file)
        request = asposewordscloud.models.requests.GetDocumentDrawingObjectByIndexRequest(remote_name, index,
                                                                                        os.path.join(
                                                                                            self.remote_test_folder,
                                                                                            self.test_folder),
                                                                                        node_path='sections/0')
        result = self.words_api.get_document_drawing_object_by_index(request)
        self.assertTrue(result.code == 200, 'Error has occurred while get drawing object by index')

    #
    # Test for getting drawing object image data
    #
    def test_get_document_drawing_object_image_data(self):
        filename = 'test_multi_pages.docx'
        remote_name = 'TestGetDocumentDrawingObjectImageData.docx'
        index = 0
        with open(os.path.join(self.local_common_folder, filename), 'rb') as f:
            file = f.read()
        self.storage_api.put_create(os.path.join(self.remote_test_folder, self.test_folder, remote_name), file)
        request = asposewordscloud.models.requests.GetDocumentDrawingObjectImageDataRequest(remote_name, index,
                                                                                          os.path.join(
                                                                                              self.remote_test_folder,
                                                                                              self.test_folder),
                                                                                          node_path='sections/0')
        result = self.words_api.get_document_drawing_object_image_data(request)
        self.assertTrue(len(result) > 0, 'Error has occurred while get drawing object image data')

    #
    # Test for getting drawing object ole data
    #
    def test_get_document_drawing_object_ole_data(self):
        filename = 'sample_EmbeddedOLE.docx'
        remote_name = 'TestGetDocumentDrawingObjectOleData.docx'
        index = 0
        with open(os.path.join(self.local_test_folder, self.test_folder, filename), 'rb') as f:
            file = f.read()
        self.storage_api.put_create(os.path.join(self.remote_test_folder, self.test_folder, remote_name), file)
        request = asposewordscloud.models.requests.GetDocumentDrawingObjectOleDataRequest(remote_name, index,
                                                                                        os.path.join(
                                                                                            self.remote_test_folder,
                                                                                            self.test_folder),
                                                                                        node_path='sections/0')
        result = self.words_api.get_document_drawing_object_ole_data(request)
        self.assertTrue(len(result) > 0, 'Error has occurred while get drawing object ole data')

    #
    # Test for getting drawing objects
    #
    def test_get_document_drawing_objects(self):
        filename = 'test_multi_pages.docx'
        remote_name = 'TestGetDocumentDrawingObjects.docx'
        with open(os.path.join(self.local_common_folder, filename), 'rb') as f:
            file = f.read()
        self.storage_api.put_create(os.path.join(self.remote_test_folder, self.test_folder, remote_name), file)
        request = asposewordscloud.models.requests.GetDocumentDrawingObjectsRequest(remote_name,
                                                                                  os.path.join(
                                                                                      self.remote_test_folder,
                                                                                      self.test_folder))
        result = self.words_api.get_document_drawing_objects(request)
        self.assertTrue(result.code == 200, 'Error has occurred while get drawing objects')

    #
    # Test for updating drawing object
    #
    def test_post_drawing_object(self):
        filename = 'test_multi_pages.docx'
        remote_name = 'TestPostDrawingObject.docx'
        data = os.path.join(self.local_common_folder, 'aspose-cloud.png')
        index = 0
        with open(os.path.join(self.local_common_folder, filename), 'rb') as f:
            file = f.read()
        self.storage_api.put_create(os.path.join(self.remote_test_folder, self.test_folder, remote_name), file)
        request = asposewordscloud.models.requests.PostDrawingObjectRequest(remote_name, '{"Left": 0}', data, index,
                                                                          os.path.join(
                                                                              self.remote_test_folder,
                                                                              self.test_folder))
        result = self.words_api.post_drawing_object(request)
        self.assertTrue(result.code == 200, 'Error has occurred while update drawing object')

    #
    # Test for adding drawing object
    #
    def test_put_drawing_object(self):
        filename = 'test_multi_pages.docx'
        remote_name = 'TestPutDrawingObject.docx'
        data = os.path.join(self.local_common_folder, 'aspose-cloud.png')
        with open(os.path.join(self.local_common_folder, filename), 'rb') as f:
            file = f.read()
        self.storage_api.put_create(os.path.join(self.remote_test_folder, self.test_folder, remote_name), file)
        request = asposewordscloud.models.requests.PutDrawingObjectRequest(remote_name, '{"Left": 0}', data,
                                                                         os.path.join(
                                                                             self.remote_test_folder,
                                                                             self.test_folder))
        result = self.words_api.put_drawing_object(request)
        self.assertTrue(result.code == 200, 'Error has occurred while add drawing object')

    #
    # Test for rendering drawing object
    #
    def test_render_drawing_object(self):
        filename = 'test_multi_pages.docx'
        remote_name = 'TestRenderDrawingObject.docx'
        _format = 'png'
        index = 0
        with open(os.path.join(self.local_common_folder, filename), 'rb') as f:
            file = f.read()
        self.storage_api.put_create(os.path.join(self.remote_test_folder, self.test_folder, remote_name), file)
        request = asposewordscloud.models.requests.RenderDrawingObjectRequest(remote_name, _format, index,
                                                                            os.path.join(
                                                                              self.remote_test_folder,
                                                                              self.test_folder),
                                                                            node_path='sections/0')
        result = self.words_api.render_drawing_object(request)
        self.assertTrue(len(result) > 0, 'Error has occurred while render drawing object')

    #
    # Test for removing drawing object from document
    #
    def test_delete_drawing_object(self):
        filename = 'test_multi_pages.docx'
        remote_name = 'TestDeleteDrawingObject.docx'
        index = 0
        with open(os.path.join(self.local_common_folder, filename), 'rb') as f:
            file = f.read()
        self.storage_api.put_create(os.path.join(self.remote_test_folder, self.test_folder, remote_name), file)
        request = asposewordscloud.models.requests.DeleteDrawingObjectRequest(remote_name, index,
                                                                            os.path.join(
                                                                              self.remote_test_folder,
                                                                              self.test_folder))
        result = self.words_api.delete_drawing_object(request)
        self.assertTrue(result.code == 200, 'Error has occurred while delete drawing object')