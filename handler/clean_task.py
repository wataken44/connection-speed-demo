#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" clean_task.py


"""

from datetime import datetime, timedelta

import webapp2
from google.appengine.ext import db

from model.performance_log_model import PerformanceLogModel

class CleanTask(webapp2.RequestHandler):
    def get(self):
        th = datetime.now() - timedelta(8) # 8 days
        query = PerformanceLogModel.all(keys_only=True)
        query.filter('appended <', th)
        query.order('appended')

        logs = query.fetch(limit = 120)
        if len(logs) <= 20:
            return

        logs = logs[:(len(logs)-20)]
        db.delete(logs)
        
if __name__ == "__main__":
    pass
