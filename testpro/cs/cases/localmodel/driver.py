#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Alison
# @Email   : liuxq@fastweb.com.cn
# @Date    : 2018/8/23 15:20
# @Desc : --
from selenium.webdriver import Remote


# 启动浏览器驱动
def browser():
    host = '192.168.107.108:4444'
    dc = {'platform': 'ANY', 'browserName': 'chrome', 'version': '', 'javascriptEnabled': True}
    driver = Remote(command_executor='http://' + host + '/wd/hub', desired_capabilities=dc)
    return driver


if __name__ == '__main__':
    dr = browser()
    dr.get("http://www.baidu.com")
    dr.quit()
