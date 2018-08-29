#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Alison
# @Email   : liuxq@fastweb.com.cn
# @Date    : 2018/8/9 12:20
# @Desc : --
# coding:utf-8
import os, time
from selenium import webdriver
import logging, smtplib
from logging import handlers
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from email.header import Header
from email.utils import formataddr


# 开发一个日志系统， 既要把日志输出到控制台， 还要写入日志文件
class Logger(object):
    level_relations = {
        'debug': logging.DEBUG,
        'info': logging.INFO,
        'warning': logging.WARNING,
        'error': logging.ERROR,
        'crit': logging.CRITICAL
    }  # 日志级别关系映射

    def __init__(self, filename, level='info', when='D', backCount=3,
                 fmt='%(asctime)s - %(pathname)s[line:%(lineno)d] - %(levelname)s: %(message)s'):
        self.logger = logging.getLogger(filename)
        format_str = logging.Formatter(fmt)  # 设置日志格式
        self.logger.setLevel(self.level_relations.get(level))  # 设置日志级别
        sh = logging.StreamHandler()  # 往屏幕上输出
        sh.setFormatter(format_str)  # 设置屏幕上显示的格式
        th = handlers.TimedRotatingFileHandler(filename=filename, when=when, backupCount=backCount,
                                               encoding='utf-8')  # 往文件里写入#指定间隔时间自动生成文件的处理器
        # 实例化TimedRotatingFileHandler
        # interval是时间间隔，backupCount是备份文件的个数，如果超过这个个数，就会自动删除，when是间隔的时间单位，单位有以下几种：
        # S 秒
        # M 分
        # H 小时、
        # D 天、
        # W 每星期（interval==0时代表星期一）
        # midnight 每天凌晨
        th.setFormatter(format_str)  # 设置文件里写入的格式
        self.logger.addHandler(sh)  # 把对象加到logger里
        self.logger.addHandler(th)


def browser(browser='chrome'):
    """
    open browser "firefox"、"chrome"、"ie"、"phantomjs"
    usage:
    driver = broswer("chrome")
    """
    try:
        if browser == "firefox":
            driver = webdriver.Firefox()
            return driver
        elif browser == "chrome":
            driver = webdriver.Chrome()
            return driver
        elif browser == "ie":
            driver = webdriver.Ie()
            return driver
        elif browser == "phantomjs":
            driver = webdriver.PhantomJS()
            return driver
        else:
            print("Not found browser!You can enter 'firefox', 'chrome', 'ie' or 'phantomjs'")
    except Exception as msg:
        print("open browser error:%s" % msg)


def send_mail(receiver, cc, subject, content, attachment='', images='', type='plain'):
    """
     @parameter list reveiver 收件人
     @parameter list cc 抄送人
     @parameter sting subject  主题
     @parameter sting type 类型；plain或者html
     @parameter doc content 正文
     @parameter list attachment 附件路径
     @return string message
     @usage:send_mail(['liuxq@fastweb.com.cn', 'liu.xiaoqing@21vianet.com'],['252996332@qq.com'],'测试Html报告6', html_txt, type='html',attachment=att_file,images=img_file)
    """
    smtpserver = 'smtp.163.com'
    sender = 'fastwebdomain@163.com'
    password = 'fasweb1234'
    # 收件人为多个收件人
    # receiver = ['XXX@126.com', 'XXX@126.com']
    # subject = 'Python email test'
    # 通过Header对象编码的文本，包含utf-8编码信息和Base64编码信息。以下中文名测试ok
    # subject = '中文标题'
    # subject=Header(subject, 'utf-8').encode(
    # 构造邮件对象MIMEMultipart对象
    # 下面的主题，发件人，收件人，日期是显示在邮件页面上的。
    msg = MIMEMultipart('mixed')
    msg['Subject'] = Header(subject, 'utf-8').encode()
    msg['From'] = sender
    # msg['To'] = 'XXX@126.com'
    # 收件人为多个收件人,通过join将列表转换为以;为间隔的字符串
    msg['To'] = ";".join(receiver)
    msg['Cc'] = ";".join(cc)
    # msg['Date']='2012-3-16'

    # 构造文字内容
    # text = "Hi!\nHow are you?\nHere is the link you wanted:\nhttp://www.baidu.com"
    text_plain = MIMEText(content, 'plain', 'utf-8')
    msg.attach(text_plain)
    # 构造图片链接
    if images:
        for img in images:
            sendimagefile = open(img, 'rb').read()
            image = MIMEImage(sendimagefile)
            image.add_header('Content-ID', '<image1>')
            image["Content-Disposition"] = 'attachment; filename=' + os.path.basename(img)
            msg.attach(image)
    # 构造html
    # 发送正文中的图片:由于包含未被许可的信息，网易邮箱定义为垃圾邮件，报554 DT:SPM ：<p><img src="cid:image1"></p>
    # html = """
    # <html>
    #   <head></head>
    #   <body>
    #     <p>Hi!<br>
    #        How are you?<br>
    #        Here is the <a href="http://www.baidu.com">link</a> you wanted.<br>
    #        图片演示: < br >
    #       < img src = "cid:image1" > < br >
    #     </p>
    #   </body>
    # </html>
    # """
    if type == 'html':
        text_html = MIMEText(content, 'html', 'utf-8')
        # text_html["Content-Disposition"] = 'attachment; filename="texthtml.html"'
        msg.attach(text_html)

    # 构造附件
    if attachment:
        for file in attachment:
            sendfile = open(file, 'rb').read()
            text_att = MIMEText(sendfile, 'base64', 'utf-8')
            text_att["Content-Type"] = 'application/octet-stream'
            # 以下附件可以重命名成aaa.txt
            text_att["Content-Disposition"] = 'attachment; filename=' + os.path.basename(file)
            # 另一种实现方式
            # text_att.add_header('Content-Disposition', 'attachment', filename='aaa.txt')
            # 以下中文测试不ok
            # text_att["Content-Disposition"] = u'attachment; filename="中文附件.txt"'.decode('utf-8')
            msg.attach(text_att)

    # 发送邮件
    try:
        smtp = smtplib.SMTP_SSL(smtpserver, 465)
        smtp.login(sender, 'fastweb1234')
        # 我们用set_debuglevel(1)就可以打印出和SMTP服务器交互的所有信息。
        # smtp.set_debuglevel(1)
        smtp.sendmail(sender, receiver + cc, msg.as_string())

    except smtplib.SMTPException as e:
        print("Error: %s" % (e))
    else:
        print("Mail Success To: " + ';'.join(receiver))
    finally:
        smtp.quit()


def sorted_dirfile(path):
    if os.path.isdir(path):
        files = os.listdir(path)
        files = [x for x in files if os.path.isfile(os.path.join(path, x))]
        files.sort(key=lambda x: os.path.getmtime(os.path.join(path, x)))
    return os.path.join(path, files[-1])


def bubble_sort(data):
    for i in range(len(data) - 1):  # 外循环每一次使得有序的数增加一个
        indicator = False  # 用于优化（没有交换时表示已经有序，结束循环）
        for j in range(len(data) - 1 - i):  # 内循环每次讲无序部分中的最大值放到最上面
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]
                indicator = True
        if not indicator:  # 如果没有交换说明列表已经有序，结束循环
            break


def insert_img(driver, file_name):
    base_dir = os.path.dirname(os.path.dirname(__file__))
    base_dir = str(base_dir)
    base_dir = base_dir.replace('\\', '/')
    base = base_dir.split('cases')[0]
    file_path = base + "/report/image/" + file_name
    driver.get_screenshot_as_file(file_path)


def insert_img_path(driver, path, filename):
    now = time.strftime('%Y-%m-%d %H_%M_%S')
    driver.get_screenshot_as_file(os.path.join(path, now + '_' + filename))


def open_report_html(file, which="chrome"):
    driver = browser(browser=which)
    driver.maximize_window()
    driver.get("file:///" + file)
    time.sleep(2)
    report_img_path = r"D:\Program Files\phpStudy\PHPTutorial\pyproject\testpro\cs\report\image\result_img"
    insert_img_path(driver, report_img_path, "report.png")


if __name__ == '__main__':
	print(time.strftime('%Y-%m-%d %H:%M:%S'))
    print(os.path.dirname(__file__))
