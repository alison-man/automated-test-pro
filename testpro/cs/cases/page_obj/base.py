#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Alison
# @Email   : liuxq@fastweb.com.cn
# @Date    : 2018/8/23 16:17
# @Desc : --

class Page(object):
    """
     页面基础类，用于所有页面的继承
    """
    bbs_url = 'https://cdncs.fastweb.com.cn/Home/Sign/login.html?returnUrl=%2F'

    def __init__(self, selenium_driver, base_url=bbs_url, parent=None):
        self.base_url = base_url
        self.driver = selenium_driver
        self.timeout = 30
        self.parent = parent

    def _open(self, url):
        url = self.base_url + url
        self.driver.get(url)
        assert self.on_page(), 'Did not land on %s' % url

    def find_element(self, *loc):
        return self.driver.find_element(*loc)

    def find_elements(self, *loc):
        return self.driver.find_elements(*loc)

    def open(self):
        self._open(self.url)

    def on_page(self):
        return self.driver.current_url == (self.base_url + self.url)

    def script(self, src):
        return self.driver.execute_script(src)
