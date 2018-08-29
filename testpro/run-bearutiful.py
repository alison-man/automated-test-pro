#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Alison
# @Email   : liuxq@fastweb.com.cn
# @Date    : 2018/8/23 15:22
# @Desc : --
import unittest, time, os
from BeautifulReport import BeautifulReport
from testpro.cs.cases.localmodel.funciton import send_mail, sorted_dirfile, open_report_html
from tomorrow import threads

now = time.strftime('%Y-%m-%d %H_%M_%S')
casepath = r"D:\Program Files\phpStudy\PHPTutorial\pyproject\testpro\cs\cases"
reportpath = r"D:\Program Files\phpStudy\PHPTutorial\pyproject\testpro\cs\report"


def add_case(case_path=casepath, rule='test*.py'):
    discover = unittest.defaultTestLoader.discover(case_path, pattern=rule)
    return discover


@threads(4)  # 并发
def run_case(case, path=reportpath):
    print(now)
    result = BeautifulReport(case)  # 定义测试报告
    result.report(filename=now + "_result.html", description='测试报告', log_path=path)


if __name__ == '__main__':
    cases = add_case()
    for i in cases:
        run_case(i)

    # 打开report网页，并截图发送邮件
    report_file = sorted_dirfile(reportpath)
    open_report_html(report_file)
    report_img_file = sorted_dirfile(reportpath + "\\image\\result_img")
    body = """
    <html>
      <head></head>
      <body>
        <p>Hi!<br>
           Here is the testing report you wanted.<br>
           报告截图: <br>
          <img src="cid:image1"><br>
        </p>
      </body>
    </html>
    """

    # 读取报告自动发送邮件
    report_file = sorted_dirfile(reportpath)
    send_mail(['liuxq@fastweb.com.cn'], ['252996332@qq.com'], '自动报告', body, type='html', images=[report_img_file], attachment=[report_file])

