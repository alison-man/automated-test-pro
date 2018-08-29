#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Alison
# @Email   : liuxq@fastweb.com.cn
# @Date    : 2018/8/28 14:38
# @Desc : --
# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Alison
# @Email   : liuxq@fastweb.com.cn
# @Date    : 2018/8/23 15:22
# @Desc : --
import unittest, time
from HTMLTestRunner import HTMLTestRunner
from testpro.cs.cases.localmodel.funciton import send_mail, sorted_dirfile
from tomorrow import threads

now = time.strftime('%Y-%m-%d %H_%M_%S')
casepath = r"D:\Program Files\phpStudy\PHPTutorial\pyproject\testpro\cs\cases"
reportpath = r"D:\Program Files\phpStudy\PHPTutorial\pyproject\testpro\cs\report"


def add_case(case_path=casepath, rule='test*.py'):
    discover = unittest.defaultTestLoader.discover(case_path, pattern=rule)
    return discover


# @threads(4)  # 并发
def run_case(case):
    fp = open(reportpath + '\\' + now + '_result.html', 'wb')  # 定义报告存放路径
    runner = HTMLTestRunner(stream=fp, title='HtmlRunner测试报告', description='用例执行情况：')  # 定义测试报告
    runner.run(case)  # 运行测试用例
    fp.close()  # 关闭报告文件


if __name__ == '__main__':
    # cases = add_case()
    # for i in cases:
    #     run_case(i)

    # 读取报告自动发送邮件
    report_file = sorted_dirfile(reportpath)
    body = open(report_file, 'rb').read()
    send_mail(['liuxq@fastweb.com.cn'], ['252996332@qq.com'], '自动化测试报告', body, type='html')
