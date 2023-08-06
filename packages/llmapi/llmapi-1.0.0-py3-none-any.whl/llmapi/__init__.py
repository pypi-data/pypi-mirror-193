#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    llmapi
    ~~~~

    llms api

    :date:      02/22/2023
    :author:    llmapi <llmapi@163.com>
    :homepage:  https://github.com/whlook/
    :license:   MIT, see LICENSE for more details.
    :copyright: Copyright (c) 2023 llmapi. All rights reserved
"""
from __future__ import unicode_literals
import sys
import json
import re

__name__ = 'llmapi'
__version__ = '1.0.0'
__description__ = 'llms api'
__keywords__ = 'llm openapi'
__author__ = 'llmapi'
__contact__ = 'llmapi@163.com'
__url__ = 'https://github.com/whlook/'
__license__ = 'MIT'

try:
    # For Python 3.0 and later
    from urllib.request import urlopen
    from urllib.parse import quote
except ImportError:
    # Fall back to Python 2's urllib2
    from urllib2 import urlopen
    from urllib import quote


class Dict:

    def __init__(self, argv):
        message = ''
        if len(argv) > 0:
            print(argv)
        else:
            print('Usage: llmapi test')
    def test(self):
        print('test')

def main():
    Dict(sys.argv[1:])


if __name__ == '__main__':
    main()
