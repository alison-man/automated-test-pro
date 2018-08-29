#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Alison
# @Email   : liuxq@fastweb.com.cn
# @Date    : 2018/8/23 15:20
# @Desc : --
from .driver import browser
import unittest


class MyTest(unittest.TestCase):
    def setUp(self):
        self.driver = browser()
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()
