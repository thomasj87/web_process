#!/usr/bin/env python -tt
"""
library to generate HTML page
"""

import os

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

    def __init__(self, pre_set=None, insertion_marker=None, content=None):

        self.insertion_marker = insertion_marker

        if pre_set and self.insertion_marker:
            try:
                with open(pre_set) as html_file:
                    self.pre_set = html_file.read()
            except BaseException as e:
                print os.path.dirname(os.path.realpath(__file__))
                print pre_set
                print e
                self.pre_set = None
        else:
            self.pre_set = None

        self.content = content

    def generate_page(self):
        """
        Function to generate HTML page.
        """
        output = str()

        if self.pre_set:
            if self.content:
                output = self.pre_set.replace(self.insertion_marker, self.content)
            else:
                output = self.pre_set
        else:
           output = "<html><body>" + self.content + "</body></html>"

        return output


