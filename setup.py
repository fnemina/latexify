#!/usr/bin/env python
# coding=utf-8
# This file is part of Latexify.
#
# Copyright 2019 Francisco Nemiña

import os
from setuptools import setup


PROJECT_ROOT = os.path.dirname(__file__)


def read_file(filepath, root=PROJECT_ROOT):
    """
    Return the contents of the specified `filepath`.
    * `root` is the base path and it defaults to the `PROJECT_ROOT` directory.
    * `filepath` should be a relative path, starting from `root`.
    """
    with open(os.path.join(root, filepath)) as fd:
        text = fd.read()
    return text


LONG_DESCRIPTION = read_file("README.md")
SHORT_DESCRIPTION = "Latexify package with function from https://nipunbatra.github.io/blog/2014/latexify.html"
REQS = [
    'matplotlib'
]


setup(
    name                  = "latexify",
    packages              = ['latexify'],
    install_requires      = REQS,
    version               = "1.0",
    author                = "Francisco Nemiña",
    author_email          = "fnemina@conae.gov.ar",
    description           = SHORT_DESCRIPTION,
    license               = "GPL-3.0",
    url                   = "None",
    long_description      = LONG_DESCRIPTION,
    classifiers           = [
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering :: Atmospheric Science",
        "Topic :: Scientific/Engineering :: Physics",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3"
    ],
)
