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

        self.response.out.write(self._render('history.html', {'logs' : logs}))

if __name__ == "__main__":
    pass
