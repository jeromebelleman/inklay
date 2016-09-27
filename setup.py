#!/usr/bin/env python
# coding=utf-8

import os
from distutils.core import setup

delattr(os, 'link')

setup(
    name='inklay',
    version='1.0',
    author='Jerome Belleman',
    author_email='Jerome.Belleman@gmail.com',
    url='http://cern.ch/jbl',
    description="Show layers and export PNGs or PDFs",
    long_description="Show specific layers from an Inkscape file and export PNGs or PDFs.",
    scripts=['inklay'],
    data_files=[('share/man/man1', ['inklay.1'])],
)
