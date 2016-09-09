# -*- coding: UTF-8 -*-

"""
Author       :  刘建民
Create Date  :  2016/07/01
"""


from attribute import *  # @UnusedWildImport
from common import CommonUtils
import unittest
import logging
from HTMLTestRunner import HTMLTestRunner
from test_LaunchOperation import LaunchOperationCase


com = CommonUtils()
# 创建log文件并初始化logging模块
com.create_log_file(launch_log_path)
com.init_logging()

logging.info("浏览器版本: %s" % com.get_browser_version())

# 初始化测试套件并添加测试用例
suite = unittest.TestSuite()
suite.addTest(LaunchOperationCase("test_CreateCard"))

# 创建存放测试报告文件的目录
path = com.create_result_path(launch_result_path)
# 找到报告的文件路径位置
file_path = os.path.abspath(path) + "\\" + time.strftime("%H%M%S") + "result.html"
discover = unittest.defaultTestLoader.discover('./', pattern='test*.py')

# 定义报告存放路径
fp = open(file_path, 'wb')
# 定义测试报告
runner = HTMLTestRunner(stream=fp,
                        title='精灵后台自动化测试报告',
                        description='环境：Windows 7   浏览器：Chrome')

# 找到最新的报告目录
new_report_path = com.find_new_report_path('./Result')
# 找到最新的报告文件路径
# new_file_path = com.find_new_report_path(new_report_path)
# 找到最新的报告文件的文件名
new_file = com.find_new_report_file(new_report_path)
runner.run(discover)
fp.close()
# 以邮件和附件形式发送用例执行结果到指定邮箱地址
com.send_email(file_path, new_file)
com.hang_program()
