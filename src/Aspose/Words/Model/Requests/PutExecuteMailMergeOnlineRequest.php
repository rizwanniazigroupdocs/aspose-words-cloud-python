<?php
/*
 * --------------------------------------------------------------------------------------------------------------------
 * <copyright company="Aspose" file="PutExecuteMailMergeOnlineRequest.php">
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
 * Request model for putExecuteMailMergeOnline operation.
 */
class PutExecuteMailMergeOnlineRequest
{
    /*
     * File with template
     */
    public $template;
	
    /*
     * File with mailmerge data
     */
    public $data;
	
    /*
     * With regions flag.
     */
    public $with_regions;
	
    /*
     * Clean up options.
     */
    public $cleanup;
    
	
    /*
     * Initializes a new instance of the PutExecuteMailMergeOnlineRequest class.
     *  
     * @param \SplFileObject $template File with template
     * @param \SplFileObject $data File with mailmerge data
     * @param bool $with_regions With regions flag.
     * @param string $cleanup Clean up options.
     */
    public function __construct($template, $data, $with_regions = null, $cleanup = null)             
    {
        $this->template = $template;
        $this->data = $data;
        $this->with_regions = $with_regions;
        $this->cleanup = $cleanup;
    }

    /*
     * File with template
     */
    public function get_template()
    {
        return $this->template;
    }

    /*
     * File with template
     */
    public function set_template($value)
    {
        $this->template = $value;
        return $this;
    }
	
    /*
     * File with mailmerge data
     */
    public function get_data()
    {
        return $this->data;
    }

    /*
     * File with mailmerge data
     */
    public function set_data($value)
    {
        $this->data = $value;
        return $this;
    }
	
    /*
     * With regions flag.
     */
    public function get_with_regions()
    {
        return $this->with_regions;
    }

    /*
     * With regions flag.
     */
    public function set_with_regions($value)
    {
        $this->with_regions = $value;
        return $this;
    }
	
    /*
     * Clean up options.
     */
    public function get_cleanup()
    {
        return $this->cleanup;
    }

    /*
     * Clean up options.
     */
    public function set_cleanup($value)
    {
        $this->cleanup = $value;
        return $this;
    }
}
