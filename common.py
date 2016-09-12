# -*- coding: UTF-8 -*-


"""
Author       :  刘建民
Create Date  :  2016/07/01
"""


from selenium import webdriver
from attribute import *  # @UnusedWildImport
import logging
import sys
import smtplib
import time
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header


class CommonUtils:

    """
    Name         :  公共方法 - 工具类
    Author       :  刘建民
    Create Date  :  2016/08/24
    """

    # get the browser version
    @staticmethod
    def get_browser_version():
        browser_version = ""
        if browser.lower() == "ie":
            os.environ['webdriver.chrome.driver'] = ie_driver_path
            my_driver = webdriver.Ie(ie_driver_path)
            browser_version = my_driver.capabilities['version']
            my_driver.close()
        elif browser.lower() == "chrome":
            os.environ['webdriver.chrome.driver'] = chrome_driver_path
            my_driver = webdriver.Chrome(chrome_driver_path)
            browser_version = my_driver.capabilities['version']
            my_driver.close()
        elif browser.lower() == "firefox":
            my_driver = webdriver.Firefox()
            browser_version = my_driver.capabilities['version']
            my_driver.close()
        return browser_version

    # create a directory
    @staticmethod
    def create_path(report_path):
        report_path = os.path.join(os.path.curdir, report_path)
        #        print os.path.isdir(report_path)
        if not os.path.isdir(report_path):
            os.makedirs(report_path)
        return report_path

    # 配置logging模块将log同时输出到控制台和log文件
    def init_logging(self):
        logging.basicConfig(
            level=logging.INFO,
            format="%(levelname)s - %(asctime)s - %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S",
            filename=self.find_new_report_path(self.find_new_report_path('./Log')),
            filemode='w')
        # define a Handler which writes INFO messages or higher to the sys.stderr
        console = logging.StreamHandler()
        console.setLevel(logging.INFO)
        # set a format which is simpler for console use
        formatter = logging.Formatter("%(levelname)s - %(asctime)s - %(message)s", "%Y-%m-%d %H:%M:%S")
        # tell the handler to use this format
        console.setFormatter(formatter)
        logging.getLogger('').addHandler(console)

    def create_log_file(self, log_path):
        log_path = self.create_path(log_path)
        report = os.path.join(log_path, "log_%s.log") % time.strftime("%H%M%S")
        if not os.path.isfile(report):
            open(report, "w")
        # logger = logging.getLogger()
        # logger.setLevel(logging.INFO)
        # rh = logging.FileHandler(report)
        # fm = logging.Formatter("%(levelname)s - %(asctime)s - %(message)s", "%Y-%m-%d %H:%M:%S")
        # rh.setFormatter(fm)
        # logger.addHandler(rh)
        # return report

    # create a handler to show the log on console board
    @ staticmethod
    def create_console_log():
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        hdr = logging.StreamHandler()
        formatter = logging.Formatter("%(levelname)s - %(asctime)s - %(message)s", "%Y-%m-%d %H:%M:%S")
        hdr.setFormatter(formatter)
        logger.addHandler(hdr)
        return logger

    # # 截图
    # def create_screen_shot(self, driver, screenshot_path):
    #     try:
    #         if need_screenshot.lower() == 'n':
    #             return None
    #         elif need_screenshot.lower() == 'y':
    #             screenshot_path = self.create_path(screenshot_path)
    #             screenshot = os.path.join(screenshot_path, "screenshot_%s.jpg") % time.strftime("%H%M%S")
    #             time.sleep(3)
    #             driver.save_screenshot(screenshot)
    #     except Exception as e:
    #         raise e

    # 创建自动化测试用例报告文件路径
    def create_result_path(self, result_path):
        path = self.create_path(result_path)
        # report = os.path.join(result_path, "Automation_Case_Result_%s.html") % time.strftime("%H%M%S")
        return path

    # 找到最新的报告目录路径
    @staticmethod
    def find_new_report_path(result_path):
        lists = os.listdir(result_path)
        lists.sort(key=lambda fn: os.path.getmtime(result_path + "\\" + fn))
        file_new = os.path.join(result_path, lists[-1])
        # logging.info(file_new)
        return file_new

    # 找到最新的报告文件
    @staticmethod
    def find_new_report_file(result_path):
        lists = os.listdir(result_path)
        lists.sort(key=lambda fn: os.path.getmtime(result_path + "\\" + fn))
        # logging.info(lists[-1])
        return lists[-1]

    # to hang the program instead of shut it down immediately
    @staticmethod
    def hang_program():
        print("*****************Press Enter to exit program.*****************")
        input()
        sys.exit()

    # to add the "https://" string when the given url doesn't contain it.
    @staticmethod
    def merge_launch_url(hosturl):
        if "http://" not in hosturl:
            hosturl = "http://" + hosturl
        return hosturl

    @staticmethod
    def kill_process(driver):
        try:
            try:
                driver.close()
            except:
                pass
            if browser.lower() == "ie":
                os.popen("taskkill /F /im IEDriverServer.exe")
                # os.popen("taskkill /F /im iexplore.exe")
            elif browser.lower() == "chrome":
                os.popen("taskkill /F /im chromedriver.exe")
                # os.popen("taskkill /F /im chrome.exe")
        except:
            pass

    # 发送邮件
    @staticmethod
    def send_email(file_path, att_file):
        try:
            msg = MIMEMultipart('related')

            # 附上正文
            part = MIMEText(main_body, 'plain', 'utf-8')
            msg.attach(part)

            # 邮件标题、收发、抄送地址
            msg['Subject'] = Header(subject, 'utf-8')
            msg['From'] = from_email_address
            msg['To'] = ','.join(to_mail_address)
            msg['Cc'] = ','.join(cc_mail_address)
            to_mail_list = to_mail_address + cc_mail_address

            # 添加附件
            send_file = open(file_path, 'rb').read()
            attach = MIMEText(send_file, 'base64', 'utf-8')
            attach["Content-Type"] = 'application/octet-stream'
            attach["Content-Disposition"] = 'attachment; filename=%s' % att_file
            msg.attach(attach)

            # 连接到smtp服务器并发送邮件
            handle = smtplib.SMTP()
            # handle.set_debuglevel(1)
            handle.connect(smtp_server, smtp_server_port)
            handle.login(from_email_address, from_email_address_pwd)
            handle.sendmail(from_email_address, to_mail_list, msg.as_string())
            handle.quit()
        except Exception as e:
            raise e

    # 定时器
    @staticmethod
    def cron_job_set():
        #         SECONDS_PER_DAY = 24 * 60 * 60
        iso_time_format = '%Y-%m-%d %H:%M:%S'
        msg = 'Please set a later timing'
        curtime = time.time()
        timearray = time.strptime(time_set, iso_time_format)
        timestamp = int(time.mktime(timearray))
        if curtime > timestamp:
            #             print ("Must sleep %d seconds" % skipSeconds)
            print(msg)
        else:
            skip_seconds = timestamp - curtime
            print(round(skip_seconds, 3))
            return time.sleep(skip_seconds)
