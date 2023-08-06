#!python
# -*- coding:utf-8 -*-
from __future__ import print_function
from setuptools import setup, find_packages
import preuqests

with open("README.md", "r", encoding='utf-8') as fh:
    long_description = fh.read()

setup(
    name="preuqests",
    version=preuqests.__version__,
    author="preuqests&penr",
    author_email="1944542244@qq.com",
    description="An Base request fast prequest",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license="MIT",
    url="https://github.com/peng0928/prequests",
    packages=find_packages(),
    install_requires=[
        "request >= 2.28.2",
        ],
    classifiers=[
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
    ],
)
