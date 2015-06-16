#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" history_page.py


"""

from handler.base_page import BasePage
from model.performance_log_model import PerformanceLogModel

class HistoryPage(BasePage):
    def get(self):
        query = PerformanceLogModel.all()
        query.order('-appended')
        logs = query.fetch(limit=20)
        
        for i in range(len(logs)):
            logs[i].remote_addr = self._mask(logs[i].remote_addr)
        
        self.response.out.write(self._render('history.html', {'logs' : logs}))

    def _mask(self, addr):
        if addr.find('.') >= 0: #ipv4
            arr = addr.split(".")
            arr[-1] = 'x'
            arr[-2] = 'y'
            return '.'.join(arr)
        elif addr.find(':'): #ipv6
            arr = addr.split(":")
            arr[0] = 'y'
            arr[1] = 'x'
            return ':'.join(arr)
        else:
            return 'xxxxxxxx'
        
if __name__ == "__main__":
    pass
