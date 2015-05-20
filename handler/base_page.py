#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" base_page.py


"""

import jinja2
import webapp2

jinja_env = None

def init_jinja_environment(template_dir):
    global jinja_env
    jinja_env = jinja2.Environment(
            loader = jinja2.FileSystemLoader(template_dir),
            extensions=['jinja2.ext.autoescape'],
            trim_blocks=True
            )

def get_jinja_environment():
    global jinja_env
    return jinja_env

class BasePage(webapp2.RequestHandler):
    def __init__(self, *args, **kwargs):
        webapp2.RequestHandler.__init__(self, *args, **kwargs)

    def _render(self, template_file, values):
        env = get_jinja_environment()
        template = env.get_template(template_file)
        return template.render(values)
        
