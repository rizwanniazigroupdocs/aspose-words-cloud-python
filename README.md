
![](https://img.shields.io/badge/api-v4.0-lightgrey) ![PyPI](https://img.shields.io/pypi/v/aspose-words-cloud) ![PyPI - Python Version](https://img.shields.io/pypi/pyversions/aspose-words-cloud) ![PyPI - Implementation](https://img.shields.io/pypi/implementation/aspose-words-cloud) ![PyPI - Wheel](https://img.shields.io/pypi/wheel/aspose-words-cloud) [![GitHub license](https://img.shields.io/github/license/aspose-words-cloud/aspose-words-cloud)](https://github.com/aspose-words-cloud/aspose-words-cloud-python/blob/master/LICENSE) 
Python Cloud SDK wraps Aspose.Words Cloud API so you could seamlessly integrate Microsoft Word® file generation, manipulation, conversion & inspection features into your own python applications.

# Node.js SDK for Word Documents Processing in the Cloud
[Aspose.Words Cloud SDK for Python](https://products.aspose.cloud/words/python) allows to work with Word document headers, footers, page numbering, tables, sections, document comments, drawing objects, FormFields, fonts, hyperlinks, ranges, paragraphs, math objects, watermarks, revisions and document protection. It also assists in appending documents, splitting documents as well as converting document to other supported file formats. Please feel free to explore the [Developer's Guide](https://docs.aspose.cloud/display/wordscloud/Developer+Guide) for all possible usage scenarios. 
Feel free to explore the [Developer's Guide](https://docs.aspose.cloud/display/wordscloud/Developer+Guide) & [API Reference](https://apireference.aspose.cloud/words/) to know all about Aspose.Words Cloud API. 

## Document Processing Services in REST

- Convert between various document-related formats, including Word to PDF & vice versa.
- Mail merge and report generation in the Cloud.
- Split & merge Word documents.
- Access Word document metadata.
- Find and replace text.
- Add & remove watermarks and protection.
- Read & write access to Document Object Model.
- Get document information in JSON or XML representation.
- Convert an encrypted PDF document into Word document format.
- [Fetch statistical data](https://docs.aspose.cloud/display/wordscloud/Get+Document+Statistics) of a document.
- [Remove all macros](https://docs.aspose.cloud/display/wordscloud/Remove+all+Macros+from+Document) contained in a specific document.
- [Convert a document to desired file format](https://docs.aspose.cloud/display/wordscloud/Convert+Document+to+Destination+Format+with+Detailed+Settings+and+Save+Result+to+Storage) along with detailed settings.

Check out the [Developer's Guide](https://docs.aspose.cloud/display/wordscloud/Developer+Guide) to know more about Aspose Words Cloud REST API.


## Read & Write Document Formats

**Microsoft Word:** DOC, DOCX, RTF, DOT, DOTX, DOTM, FlatOPC (XML)
**OpenOffice:** ODT, OTT
**WordprocessingML:** XML
**Web:** HTML, MHTML, HtmlFixed
**Text:** TXT
**Fixed Layout:** PDF

## Save Document As

**Fixed Layout:** PDF/A, XPS, OpenXPS, PS
**Images:** JPEG, PNG, BMP, SVG, TIFF, EMF
**Others:** PCL

## Enhancements in Version 20.11

- In configuration json file appSid / appKey has been replaced to clientId / clientSecret.
- In Words API initialization methods clientId parameter precedes clientSecret parameter.


## Enhancements in Version 20.10

- Internal API changes.


## Enhancements in Version 20.9

- Added Batch API feature


## Enhancements in Version 20.8

- Added new api method (PUT '/words/{name}/compatibility/optimize') which is allows to optimize the document contents as well as default Aspose.Words behavior to a particular versions of MS Word
- Added 'ApplyBaseDocumentHeadersAndFootersToAppendingDocuments' option to 'DocumentEntryList' for AppendDocument API
- WithoutNodePath methods have been removed, pass null values instead


## Enhancements in Version 20.7

- Added 'Markdown' save format
- Added endpoint to update paragraph format without node path (PUT '/words/{name}/paragraphs/{index}/format')


## Enhancements in Version 20.6

- Added new methods:
  - DeleteAllParagraphTabStopsWithoutNodePath
  - DeleteParagraphTabStopWithoutNodePath
  - GetParagraphTabStopsWithoutNodePath
  - InsertOrUpdateParagraphTabStopWithoutNodePath
  - InsertParagraphWithoutNodePath
  - UpdateParagraphFormatWithoutNodePath
  - UpdateParagraphListFormatWithoutNodePath
  - DeleteParagraphListFormatWithoutNodePath
- DrawingObject related methods have been changed body content. Special request classes are introduced instead of strings.
- InsertOrUpdateParagraphTabStop, DeleteParagraphTabStop methods have been changed parameter order
- OoxmlSaveOptionsData.CompressionLevel property has been added


## Enhancements in Version 20.5

- Added methods to work with Word document lists
  - GetLists
  - GetList
  - InsertList
  - UpdateList
  - UpdateListLevel
- Added methods to work with styles
  - GetStyles
  - UpdateStyle
  - InsertStyle
  - CopyStyle
  - GetStyleFromDocumentElement
  - ApplyStyleToDocumentElement
- Added methods to work with paragraph list format
  - GetParagraphListFormat
  - GetParagraphListFormatWithoutNodePath
  - UpdateParagraphListFormat
  - DeleteParagraphListFormat
- Added methods to work with paragraph tab stops
  - GetParagraphTabStops
  - InsertOrUpdateParagraphTabStop
  - DeleteAllParagraphTabStops
  - DeleteParagraphTabStop
- Added methods to build reports
  - BuildReport
  - BuildReportOnline
- Added Shading property to ParagraphFormat


## Read & Write Document Formats

**Microsoft Word:** DOC, DOCX, RTF, DOT, DOTX, DOTM, FlatOPC (XML)
**OpenOffice:** ODT, OTT
**WordprocessingML:** XML
**Web:** HTML, MHTML, HtmlFixed
**Text:** TXT
**Fixed Layout:** PDF

## Save Document As

**Fixed Layout:** PDF/A, XPS, OpenXPS, PS
**Images:** JPEG, PNG, BMP, SVG, TIFF, EMF
**Others:** PCL

## Platform Independence

Aspose.Words Cloud’s platform independent document manipulation API is a true REST API that can be used from any platform. You can use it with any language or platform that supports REST, be it the web, desktop, mobile, or the cloud. The API integrates with other cloud services to provide you the flexibility you require for processing documents. It is suitable for the most types of businesses, documents, or content.

## Getting Started with Aspose.Words Cloud SDK for Python

Firstly, create an account at [Aspose for Cloud](https://dashboard.aspose.cloud/#/apps) to get your application information and free quota to use the API. Now execute `pip install aspose-words-cloud` from the command line to fetch the SDK. Then import the package via `import asposewordscloud`. 

### Install via Setuptools

Execute `python setup.py install --user` and import the package as `import asposewordscloud`.

The complete source code is available at [GitHub Repository](https://github.com/aspose-words-cloud/aspose-words-cloud-python).

## Delete Watermarks from Word Document via Python

```python
        # Start README example

        self.words_api = asposewordscloud.WordsApi(client_id, client_secret)
        self.words_api.api_client.configuration.host = base_url

        upload_request = asposewordscloud.models.requests.UploadFileRequest(
            open(os.path.join(local_folder, filename), 'rb'), os.path.join(remote_folder, remote_name))
        self.words_api.upload_file(upload_request)

        request = asposewordscloud.models.requests.DeleteWatermarkRequest(remote_name, remote_folder)
        self.words_api.delete_watermark(request)

        # End README example
```

## Aspose.Words Cloud SDKs in Popular Languages

| .NET | Java | PHP | Python | Ruby | Node.js | Android |
|---|---|---|---|---|---|---|
| [GitHub](https://github.com/aspose-words-cloud/aspose-words-cloud-dotnet) | [GitHub](https://github.com/aspose-words-cloud/aspose-words-cloud-java) | [GitHub](https://github.com/aspose-words-cloud/aspose-words-cloud-php) | [GitHub](https://github.com/aspose-words-cloud/aspose-words-cloud-python) | [GitHub](https://github.com/aspose-words-cloud/aspose-words-cloud-ruby)  | [GitHub](https://github.com/aspose-words-cloud/aspose-words-cloud-node) | [GitHub](https://github.com/aspose-words-cloud/aspose-words-cloud-android) |
| [NuGet](https://www.nuget.org/packages/Aspose.Words-Cloud/) | [Maven](https://repository.aspose.cloud/webapp/#/artifacts/browse/tree/General/repo/com/aspose/aspose-words-cloud) | [Composer](https://packagist.org/packages/aspose-cloud/aspose-words-cloud) | [PIP](https://pypi.org/project/aspose.words-cloud/) | [GEM](https://rubygems.org/gems/aspose_words_cloud)  | [NPM](https://www.npmjs.com/package/asposewordscloud) | [Maven](https://repository.aspose.cloud/webapp/#/artifacts/browse/tree/General/repo/com/aspose/aspose-words-cloud) | 

[Product Page](https://products.aspose.cloud/words/php) | [Documentation](https://docs.aspose.cloud/display/wordscloud/Home) | [API Reference](https://apireference.aspose.cloud/words/) | [Code Samples](https://github.com/aspose-words-cloud/aspose-words-cloud-dotnet) | [Blog](https://blog.aspose.cloud/category/words/) | [Free Support](https://forum.aspose.cloud/c/words) | [Free Trial](https://dashboard.aspose.cloud/#/apps)
