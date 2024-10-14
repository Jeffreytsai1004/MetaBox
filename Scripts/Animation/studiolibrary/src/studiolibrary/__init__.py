#!/usr/bin/env python
# -*- coding: utf-8 -*-


__version__ = "2.17.0"


def version():
    """
    Return the current version of the Studio Library

    :rtype: str
    """
    return __version__


from studiolibrary import config
from studiolibrary import resource
from studiolibrary.utils import *
from studiolibrary.library import Library
from studiolibrary.libraryitem import LibraryItem
from studiolibrary.main import main
