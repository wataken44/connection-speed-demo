#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" performance_log_model.py


"""

from google.appengine.ext import db

class PerformanceLogModel(db.Model):
    appended = db.DateTimeProperty(auto_now_add=True)
    remote_addr = db.StringProperty(indexed=False)
    user_agent = db.StringProperty(indexed=False)
    url = db.LinkProperty(indexed=False)
    size = db.IntegerProperty(indexed=False)
    dns_time = db.FloatProperty(indexed=False)
    tcp_time = db.FloatProperty(indexed=False)
    http_rt_time = db.FloatProperty(indexed=False)
    http_res_time = db.FloatProperty(indexed=False)

