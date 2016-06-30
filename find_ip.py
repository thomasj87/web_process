#!/usr/bin/env python -tt
# coding=utf-8
"""
Script to search for ip addresses.
"""

__author__ = "Thomas Jongerius"
__copyright__ = "Copyright 2016, Thomas Jongerius"
__credits__ = ["Thomas Jongerius"]
__license__ = "GPL"
__version__ = "0.1"
__maintainer__ = "Thomas Jongerius"
__email__ = "thomasjongerius@yaworks.nl"
__status__ = "Development"

import logging

def application(environ, start_response):
    '''
    WSGI application for filtering and outputting IP-addresses.
    '''

    # Import system modules
    import os
    import sys

    # Add required system paths for WSGI rights.
    base_directory = os.path.dirname(__file__)
    sys.path.append(base_directory)
    sys.path.append('/data/tools-bin/web_process/NetAnalyzer/IPFinder')

    # Import required modules for HTML processing
    import html_process
    from cgi import parse_qs, escape

    # Import application required modules
    from NetAnalyzer.IPFinder import IPFinder

    # the environment variable CONTENT_LENGTH may be empty or missing
    try:
        request_body_size = int(environ.get('CONTENT_LENGTH', 0))
    except (ValueError):
        request_body_size = 0

    # HTML template file template
    html_file = base_directory + '/' + 'find_ip.html'

    # When the method is POST the variable will be sent
    # in the HTTP request body which is passed by the WSGI server
    # in the file like wsgi.input environment variable.
    request_body = environ['wsgi.input'].read(request_body_size)
    d = parse_qs(request_body)

    logging_data = d.get('logging_field', [''])[0] #Return logging data
    options = d.get('options', []) # Returns a list of options.

    # Always escape user input to avoid script injection
    logging_data = escape(logging_data)
    options = [escape(option) for option in options]

    # Launch application against input
    if logging_data:
        ips = IPFinder.getip(logging_data)
        if len(ips) < 1:
            ips = ['No IPs found!']
    else:
        ips = ['No input data!']

    html_output = html_process.html_handler.lst_to_line_by_line(ips)

    if options:
        html_output = html_output + '<br><h3>Options</h3>'
        for option in options:
            html_output = html_output + '<br>' + option

    x = html_process.html_handler(pre_set=html_file,
                                  insertion_marker='<!--PYTHON_PROCESS_OUTPUT-->',
                                  content=html_output)

    # Fill defaults and generate page
    response_body = x.generate_page() % { # Fill the above html template in
        'checked-countips': ('', 'checked')['count_ip' in options],
        'checked-include_mask': ('', 'checked')['include_mask' in options]}

    status = '200 OK'

    response_headers = [
        ('Content-Type', 'text/html'),
        ('Content-Length', str(len(response_body)))
    ]

    start_response(status, response_headers)
    return [response_body]

def main():

    logging.debug("Started")

    from wsgiref.simple_server import make_server
    httpd = make_server('localhost', 8051, application)
    httpd.serve_forever()

    logging.debug("Done")

if __name__ == '__main__':
    main()