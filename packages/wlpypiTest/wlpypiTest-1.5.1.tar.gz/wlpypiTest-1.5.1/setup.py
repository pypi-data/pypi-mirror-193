#!python
# -*- coding:utf-8 -*-
from __future__ import print_function
from setuptools import setup, find_packages
import wlpypiTest
with open("README.md", "r", encoding='utf-8') as fh:
    long_description = fh.read()

setup(
    name="wlpypiTest",
    version=wlpypiTest.__version__,
    author="wanglie",
    author_email="lie_wangxy@163.com",
    description="test",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license="MIT",
    url="http://www.baidu.com",
    packages=find_packages("commons"),
    install_requires=[

        ],
    classifiers=[
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Programming Language :: Python :: 3.7",
        'Programming Language :: Python :: Implementation :: CPython',
    ],
)
