from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

# This gets deployed when a new release is made by github actions
VERSION = '0.0.12'

# CHANGEME VARS
PACKAGE_NAME = "robotsparser"
DESCRIPTION = 'Parse robots.txt files and find indexed urls'
LONG_DESCRIPTION = 'Parse robots.txt files and find indexed urls'
AUTHOR_NAME = "Diego Velez"
AUTHOR_EMAIL = "diegovelezs94@gmail.com"
PROJECT_URL = "https://github.com/Dvelezs94/robotsparser"
REQUIRED_PACKAGES = ['bs4', 'lxml', 'cloudscraper'] # required 3rd party tools used by your package
PROJECT_KEYWORDS = ['robots.txt', 'sitemap', 'crawler', 'data mining']
# Read more about classifiers at
# https://pypi.org/classifiers/
CLASSIFIERS = [
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows"]

setup(
    name=PACKAGE_NAME,
    version=VERSION,
    author=AUTHOR_NAME,
    author_email=AUTHOR_EMAIL,
    description=DESCRIPTION,
    url = PROJECT_URL,
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages(),
    install_requires=REQUIRED_PACKAGES,
    keywords=PROJECT_KEYWORDS,
    classifiers=CLASSIFIERS
)