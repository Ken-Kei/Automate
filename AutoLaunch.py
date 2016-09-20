# -*- coding: UTF-8 -*-

"""
Author       :  Ken-Kei
Create Date  :  2016/07/01
"""


from attribute import *  # @UnusedWildImport
from common import CommonUtils
import unittest
import logging
from Lib.HTMLTestRunner import HTMLTestRunner
# from TestCase.test_LaunchOperation import LaunchOperationCase
from TestCase.test_LaunchLogin import LaunchLoginCase


com = CommonUtils()
# 创建log文件并初始化logging模块
com.create_log_file(launch_log_path)
com.init_logging()

logging.info("浏览器版本: %s" % com.get_browser_version())

# 初始化测试套件并添加测试用例
suite = unittest.TestSuite()
# suite.addTest(LaunchOperationCase("test_CreatePictureClassify"))
suite.addTest(LaunchLoginCase("test_LoginFailedWithWrongUser"))

# 创建存放测试报告文件的目录
path = com.create_result_path(launch_result_path)
file_path = os.path.abspath(path) + "\\" + time.strftime("%H%M%S") + "result.html"
# 创建测试报告文件
fp = open(file_path, 'wb')

discover = unittest.defaultTestLoader.discover('./TestCase', pattern='test*.py')
# 定义测试报告
description = '操作系统：' + operation_system + '      ' + '浏览器：' + browser
runner = HTMLTestRunner(stream=fp,
                        title='精灵后台自动化测试报告',
                        description=description)

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
