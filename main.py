#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" main.py


"""

import os
import sys
rootdir = os.path.dirname(os.path.abspath(__file__))

import webapp2

import handler.jpeg_page
handler.jpeg_page.set_base_dir(rootdir + "/file/")

import handler.base_page
handler.base_page.init_jinja_environment(rootdir + "/template/")

application = webapp2.WSGIApplication([
    ('/', 'handler.index_page.IndexPage'),
    ('/register', 'handler.register_page.RegisterPage'),
    ('/history', 'handler.history_page.HistoryPage'),
    ('/raw.txt', 'handler.raw_page.RawPage'),
    ('/task/clean', 'handler.clean_task.CleanTask'),
    ('/file/([^/]*).jpg', 'handler.jpeg_page.JPEGPage'),
])
