#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

import os
import sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))

from szrbzl.utils.url import BaseHandler

class IndexHandler(BaseHandler):
    def get(self):

        self.render('index.html')

fe_url = [
    (r'/', IndexHandler),
]