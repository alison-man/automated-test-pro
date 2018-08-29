#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Alison
# @Email   : liuxq@fastweb.com.cn
# @Date    : 2018/8/23 15:21
# @Desc : --
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from .base import Page
from time import sleep


class Login(Page):
    """
    用户登录页面
    """
    url = ''

    login_username_loc = (By.NAME, "username")
    login_password_loc = (By.NAME, "password")
    login_button_loc = (By.ID, "login_submit")

    # 登录用户名
    def login_username(self, username):
        self.find_element(*self.login_username_loc).send_keys(username)

    # 登录密码e
    def login_password(self, password):
        self.find_element(*self.login_password_loc).send_keys(password)

    # 登录按钮
    def login_button(self):
        self.find_element(*self.login_button_loc).click()

    # 定义统一登录入口
    def user_login(self, username='fastweb.com.cn', password='fastweb123'):
        """获取的用户名和密码"""
        self.open()
        self.login_username(username)
        self.login_password(password)
        self.login_button()
        sleep(1)

    user_error_hint_loc = (By.XPATH, "//*[@id='login-box']/div/div/form/fieldset/div[4]")
    pawd_error_hint_loc = (By.XPATH, "//*[@id='login-box']/div/div/form/fieldset/div[4]")
    user_login_success_loc = (By.XPATH, "//*[@id='main-container']/div/div[2]/div/div[2]/ul/li[1]/a/div[2]/p")

    # 用户名错误提示
    def user_error_hint(self):
        return self.find_element(*self.user_error_hint_loc).text

    # 密码错误提示
    def pawd_error_hint(self):
        return self.find_element(*self.pawd_error_hint_loc).text

    # 登录成功
    def user_login_success(self):
        return self.find_element(*self.user_login_success_loc).text
