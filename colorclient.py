# -*- coding: utf-8 -*-
#
#  colorclient.py
#  colordb
#

"""
A basic Python client for the colordb REST API.
"""

import json

import requests

class APIError(Exception):
    pass

class ColorDBClient(object):
    def __init__(self, host):
        self.host = host

    def add_colors(self, entryid, colors):
        url = 'http://%s/entries?entryid=%d&colors=%s' % (
                self.host,
                int(entryid),
                ','.join(c.lstrip('#') for c in colors)
            )
        response = requests.post(url)

        if response.status_code != 200:
            raise APIError('got HTTP %s response with content: %s' % (
                    response.status_code,
                    response.content,
                ))

    def nearest(self, color):
        url = 'http://%s/%s' % (self.host, color.lstrip('#'))
        response = requests.get(url)
        if response.status_code != 200:
            raise APIError('got HTTP %s response with content: %s' % (
                    response.status_code,
                    response.content,
                ))

        return json.loads(response.content)

