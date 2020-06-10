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

class ClassifyDocumentRequest(object):
    """
    Request model for classify_document operation.
    Initializes a new instance.
    :param document_name The document name.
    :param folder Original document folder.
    :param storage Original document storage.
    :param load_encoding Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML.
    :param password Password for opening an encrypted document.
    :param best_classes_count Count of the best classes to return.
    :param taxonomy Taxonomy to use for classification return.
    """

    def __init__(self, document_name, folder=None, storage=None, load_encoding=None, password=None, best_classes_count=None, taxonomy=None):
        self.document_name = document_name
        self.folder = folder
        self.storage = storage
        self.load_encoding = load_encoding
        self.password = password
        self.best_classes_count = best_classes_count
        self.taxonomy = taxonomy
