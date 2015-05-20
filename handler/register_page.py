#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" register_page.py


"""

from handler.base_page import BasePage
from model.performance_log_model import PerformanceLogModel

class RegisterPage(BasePage):
    def post(self):
        p = PerformanceLogModel(
            remote_addr = self.request.remote_addr,
            user_agent = self.request.headers.get('User-Agent'),
            url = self.request.get('name'),
            size = int(self.request.get('size')),
            dns_time = float(self.request.get('dns_time')),
            tcp_time = float(self.request.get('tcp_time')),
            http_rt_time = float(self.request.get('http_rt_time')),
            http_res_time = float(self.request.get('http_res_time'))
        )
        
        p.put()
