n
# --------------------------------------------------------------------------------
# <copyright company="Aspose" file="PostDrawingObjectRequest.py">
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


class PostDrawingObjectRequest(object):
    """
    Request model for post_drawing_object operation.
    Initializes a new instance.
    :param name The document name.
    :param drawing_object Drawing object parameters
    :param image_file File with image
    :param index Object's index
    :param folder Original document folder.
    :param storage File storage, which have to be used.
    :param load_encoding Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML.
    :param password Password for opening an encrypted document.
    :param dest_file_name Result name of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document.
    :param revision_author Initials of the author to use for revisions.If you set this parameter and then make some changes to the document programmatically, save the document and later open the document in MS Word you will see these changes as revisions.
    :param revision_date_time The date and time to use for revisions.
    :param node_path Path to node, which contains collection of drawing objects.
    """

    def __init__(self, name, drawing_object, image_file, index, folder=None, storage=None, load_encoding=None, password=None, dest_file_name=None, revision_author=None, revision_date_time=None, node_path=None):
        self.name = name
        self.drawing_object = drawing_object
        self.image_file = image_file
        self.index = index
        self.folder = folder
        self.storage = storage
        self.load_encoding = load_encoding
        self.password = password
        self.dest_file_name = dest_file_name
        self.revision_author = revision_author
        self.revision_date_time = revision_date_time
        self.node_path = node_pat