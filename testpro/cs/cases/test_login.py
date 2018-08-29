#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Alison
# @Email   : liuxq@fastweb.com.cn
# @Date    : 2018/8/23 16:59
# @Desc : --
from time import sleep
import unittest, random, sys
from testpro.cs.cases.localmodel import myunit, funciton
from testpro.cs.cases.page_obj.loginPage import Login


class loginTest(myunit.MyTest):
    """登录测试"""

    def user_login_verify(self, username="", password=""):
        Login(self.driver).user_login(username, password)

    def test_login_1(self):
        """用户名和密码为空登录"""
        self.user_login_verify()
        po = Login(self.driver)
        self.assertEqual(po.user_error_hint(), "用户名必填")
        funciton.insert_img(self.driver, "user_empty.png")

    def test_login_2(self):
        """用户名正确，密码为空"""
        self.user_login_verify(username="fastweb.com.cn")
        po = Login(self.driver)
        self.assertEqual(po.pawd_error_hint(), "密码必填")
        funciton.insert_img(self.driver, "pawd_empty.png")

    def test_login_3(self):
        """用户名和密码不匹配"""
        character = random.choice('abcdeserislxns.dierkshdgf.gsdf')
        username = "zhangsan" + character
        self.user_login_verify(username=username, password="fastweb123")
        po = Login(self.driver)
        self.assertEqual(po.pawd_error_hint(), "用户名或者密码错误")
        funciton.insert_img(self.driver, "user_pawd_error.png")

    def test_login_4(self):
        """用户名和密码正确"""
        self.user_login_verify(username="fastweb.com.cn", password="fastweb123")
        po = Login(self.driver)
        self.assertEqual(po.user_login_success(), "报表分析")
        funciton.insert_img(self.driver, "user_pawd_success.png")


if __name__ == '__main_':
    unittest.main()
