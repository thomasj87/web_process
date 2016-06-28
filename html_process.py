#!/usr/bin/env python -tt
"""
library to generate HTML page
"""

import logging

__author__ = "Thomas Jongerius"
__copyright__ = "Copyright 2016, Thomas Jongerius"
__credits__ = ["Thomas Jongerius"]
__license__ = "GPL"
__version__ = "0.1"
__maintainer__ = "Thomas Jongerius"
__email__ = "thomasjongerius@yaworks.nl"
__status__ = "Development"


class html_handler(object):
    """
    Module to generate HTML page based on input (example page) with begin and end marker.
    If none is give, generate input on blank page.
    """

    def __init__(self, pre_set=None, start_marker=None, end_marker=None, content=None):

        if pre_set:
            self.pre_set = None
        else:
            self.pre_set = None
        self.start_marker = start_marker
        self.end_marker = end_marker
        self.content = content

    def generate_page(self):
        """
        Function to generate HTML page.
        """
        output = self.content

        return output


