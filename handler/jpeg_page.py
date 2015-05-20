#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" jpeg_page.py


"""

import webapp2
import os

base_dir = ""

def set_base_dir(d):
    global base_dir
    base_dir = d

class JPEGPage(webapp2.RequestHandler):
    def get(self, name):
        jpg = base_dir + name + ".jpg"
        if not os.path.exists(jpg):
            name = "neko"
            jpg = base_dir + name + ".jpg"

        self.response.headers["Content-Type"] = "image/jpeg"
        self.response.headers["Cache-Control"] = "no-cache"

        fp = open(jpg, 'rb')
        self.response.out.write(fp.read())
        fp.close()
        
        
