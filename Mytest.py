# -*- coding: UTF-8 -*-


"""
Author       :  刘建民
Create Date  :  2016/07/01
"""


import unittest
from BasePage import BasePage
import logging


class MyUnitTest(unittest.TestCase, BasePage):

    def setUp(self):
        self.verificationErrors = []
        self.driver = self.get_driver()

    def tearDown(self):
        logging.info("用例结束")
        driver = self.driver
        self.assertEqual([], self.verificationErrors)
        # 关闭浏览器
        driver.delete_all_cookies()
        driver.quit()
