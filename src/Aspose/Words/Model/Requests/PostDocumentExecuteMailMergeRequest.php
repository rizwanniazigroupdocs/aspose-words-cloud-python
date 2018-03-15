<?php

}
/*
 * --------------------------------------------------------------------------------------------------------------------
 * <copyright company="Aspose" file="PostDocumentExecuteMailMergeRequest.php">
 *   Copyright (c) 2018 Aspose.Words for Cloud
 * </copyright>
 * <summary>
 *   Permission is hereby granted, free of charge, to any person obtaining a copy
 *  of this software and associated documentation files (the "Software"), to deal
 *  in the Software without restriction, including without limitation the rights
 *  to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
 *  copies of the Software, and to permit persons to whom the Software is
 *  furnished to do so, subject to the following conditions:
 * 
 *  The above copyright notice and this permission notice shall be included in all
 *  copies or substantial portions of the Software.
 * 
 *  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
 *  IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
 *  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
 *  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
 *  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
 *  OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
 *  SOFTWARE.
 * </summary>
 * --------------------------------------------------------------------------------------------------------------------
 */
namespace Aspose\Words\Model\Requests;

/*
 * Request model for postDocumentExecuteMailMerge" operation.
 */
class PostDocumentExecuteMailMergeRequest
{
    /*
     * Initializes a new instance of the PostDocumentExecuteMailMergeRequest class.
     *  
     * @param string $name The document name.
     * @param bool $with_regions With regions flag.
     * @param string $data Mail merge data
     * @param string $folder Original document folder.
     * @param string $storage File storage, which have to be used.
     * @param string $load_encoding Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML.
     * @param string $password Password for opening an encrypted document.
     * @param string $mail_merge_data_file Mail merge data.
     * @param string $cleanup Clean up options.
     * @param bool $use_whole_paragraph_as_region Gets or sets a value indicating whether paragraph with TableStart or              TableEnd field should be fully included into mail merge region or particular range between TableStart and TableEnd fields.              The default value is true.
     * @param string $dest_file_name Result name of the document after the operation. If this parameter is omitted then result of the operation will be saved with autogenerated name.
     */
    public function __construct($name, $with_regions, $data = null, $folder = null, $storage = null, $load_encoding = null, $password = null, $mail_merge_data_file = null, $cleanup = null, $use_whole_paragraph_as_region = null, $dest_file_name = null)             
    {
        $this->name = $name;
        $this->with_regions = $with_regions;
        $this->data = $data;
        $this->folder = $folder;
        $this->storage = $storage;
        $this->load_encoding = $load_encoding;
        $this->password = $password;
        $this->mail_merge_data_file = $mail_merge_data_file;
        $this->cleanup = $cleanup;
        $this->use_whole_paragraph_as_region = $use_whole_paragraph_as_region;
        $this->dest_file_name = $dest_file_name;
    }

    /*
     * The document name.
     */
    public $name;
	
    /*
     * With regions flag.
     */
    public $with_regions;
	
    /*
     * Mail merge data
     */
    public $data;
	
    /*
     * Original document folder.
     */
    public $folder;
	
    /*
     * File storage, which have to be used.
     */
    public $storage;
	
    /*
     * Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML.
     */
    public $load_encoding;
	
    /*
     * Password for opening an encrypted document.
     */
    public $password;
	
    /*
     * Mail merge data.
     */
    public $mail_merge_data_file;
	
    /*
     * Clean up options.
     */
    public $cleanup;
	
    /*
     * Gets or sets a value indicating whether paragraph with TableStart or              TableEnd field should be fully included into mail merge region or particular range between TableStart and TableEnd fields.              The default value is true.
     */
    public $use_whole_paragraph_as_region;
	
    /*
     * Result name of the document after the operation. If this parameter is omitted then result of the operation will be saved with autogenerated name.
     */
    public $dest_file_name;