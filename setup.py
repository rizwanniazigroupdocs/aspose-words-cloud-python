# coding: utf-8

"""
    Aspose.Words for Cloud API Reference

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 18.5.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from setuptools import setup, find_packages  # noqa: H301

NAME = "asposewordscloud"
VERSION = "18.6"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = ["urllib3 >= 1.15", "six >= 1.10", "certifi", "python-dateutil"]
TEST_REQUIRES = ['asposestoragecloud >=1.0.5']

setup(
    name=NAME,
    version=VERSION,
    description="Aspose.Words for Cloud API Reference",
    author_email="yaroslaw.ekimov@aspose.com",
    url="https://github.com/aspose-words-cloud",
    keywords=["aspose", "python", "aspose cloud"],
    install_requires=REQUIRES,
	tests_require=TEST_REQUIRES,
    packages=find_packages(),
    include_package_data=True,
    long_description="""\
    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501
    """
)