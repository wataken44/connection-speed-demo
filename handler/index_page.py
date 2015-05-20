#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" index_page.py


"""

import handler.base_page

class IndexPage(handler.base_page.BasePage):
    def get(self):
        body = self._render("index.html", {})
        self.response.out.write(body)
