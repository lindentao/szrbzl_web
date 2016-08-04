#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

from url import BaseHandler

class AdminIndexHandler(BaseHandler):
    def get(self):
        self.render('admin/index.html')

admin_url = [
    (r'/admin', AdminIndexHandler),
]