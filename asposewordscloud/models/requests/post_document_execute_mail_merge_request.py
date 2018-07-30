e
# --------------------------------------------------------------------------------
# <copyright company="Aspose" file="PostDocumentExecuteMailMergeRequest.py">
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
# --------------------------------------------------------------------------------


class PostDocumentExecuteMailMergeRequest(object):
    """
    Request model for post_document_execute_mail_merge operation.
    Initializes a new instance.
    :param name The document name.
    :param data Mail merge data
    :param folder Original document folder.
    :param storage File storage, which have to be used.
    :param load_encoding Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML.
    :param password Password for opening an encrypted document.
    :param with_regions With regions flag.
    :param mail_merge_data_file Mail merge data.
    :param cleanup Clean up options.
    :param use_whole_paragraph_as_region Gets or sets a value indicating whether paragraph with TableStart or              TableEnd field should be fully included into mail merge region or particular range between TableStart and TableEnd fields.              The default value is true.
    :param dest_file_name Result name of the document after the operation. If this parameter is omitted then result of the operation will be saved with autogenerated name.
    """

    def __init__(self, name, data=None, folder=None, storage=None, load_encoding=None, password=None, with_regions=None, mail_merge_data_file=None, cleanup=None, use_whole_paragraph_as_region=None, dest_file_name=None):
        self.name = name
        self.data = data
        self.folder = folder
        self.storage = storage
        self.load_encoding = load_encoding
        self.password = password
        self.with_regions = with_regions
        self.mail_merge_data_file = mail_merge_data_file
        self.cleanup = cleanup
        self.use_whole_paragraph_as_region = use_whole_paragraph_as_region
        self.dest_file_name = dest_file_nam