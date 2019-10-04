# coding: utf-8

"""
    Aspose.Words for Cloud API Reference

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 18.5.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from setuptools import setup, find_packages  # noqa: H301

NAME = "aspose-words-cloud"
VERSION = "19.9.2"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = ["urllib3 >= 1.16", "six >= 1.10", "certifi", "python-dateutil"]
TEST_REQUIRES = ['asposestoragecloud >=1.0.5']

from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), 'r') as f:
    long_description = f.read()

setup(
    name=NAME,
    version=VERSION,
    description="Aspose.Words for Cloud API Reference",
    author='Yaroslaw Ekimov',
    author_email="yaroslaw.ekimov@aspose.com",
    url="https://github.com/aspose-words-cloud/aspose-words-cloud-python",
	classifiers=[
		'Development Status :: 5 - Production/Stable',
		'Intended Audience :: Developers',
        'Topic :: Office/Business :: Office Suites',
		'Topic :: Software Development :: Libraries',
		'License :: OSI Approved :: MIT License',
		'Programming Language :: Python :: 2.7',
		'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
	],
    keywords=["aspose", "python", "aspose cloud", "word"],
    install_requires=REQUIRES,
	tests_require=TEST_REQUIRES,
    packages=find_packages(),
    include_package_data=True,
    long_description=long_description,
    long_description_content_type="text/markdown"
)
