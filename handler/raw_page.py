#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" raw_page.py


"""

import webapp2
from model.performance_log_model import PerformanceLogModel

def q(s):
    return "\"%s\"" % s

class RawPage(webapp2.RequestHandler):
    def get(self):
        self.response.headers["Content-Type"] = "text/plain"

        h = ["appended","remote_addr","user_agent", "url", "size",
             "dns_time(ms)", "tcp_time(ms)", "http_rt_time(ms)","http_res_time(ms)",
             "speed(KB/s)","speed(Kbps)"]
        for i in range(len(h)):
            h[i] = q(h[i])
        
        self.response.out.write("\t".join(h) + "\n")
        query = PerformanceLogModel.all()
        query.order('-appended')
        logs = query.fetch(limit=None)
        for log in logs:
            sp = (log.size / 1000) / (log.http_res_time / 1000)
            d = [log.appended, log.remote_addr, log.user_agent, log.url, log.size,
                 log.dns_time, log.tcp_time, log.http_rt_time, log.http_res_time,
                 sp, sp*8]
            for i in range(len(d)):
                d[i] = q(d[i])
            self.response.out.write("\t".join(d) + "\n")
