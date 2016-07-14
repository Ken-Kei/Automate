# -*- coding: UTF-8 -*-


"""
Author       :  刘建民
Create Date  :  2016/7/7
Edit Date    :  2016/7/8
"""

from LoginPage import LoginPageAction
import unittest
from attribute import *  # @UnusedWildImport
from BasePage import BasePage
from common import CommonUtils
import logging

com = CommonUtils()


class LaunchOperationCase(unittest.TestCase, BasePage):
    """家居精灵-> 登录模块 - 自动化测试用例"""

    def setUp(self):
        self.verificationErrors = []
        self.driver = self.get_driver()
        self.action = LoginPageAction(self.driver)

    def test_Login(self):
        """登入以及登出O2O平台"""

        action = self.action
        logging.info("执行用例：登入以及登出O2O平台")
        # 如果登录失败的话就重新尝试登录，一共尝试3次
        for i in range(0, 3):
            try:
                # 打开O2O主页的url并验证登入登出
                action.login(main_url, username, password)
                logging.info(loging_in % username)
                self.wait_element_load_end(logout_button)
                if self.is_element_exist(*logout_button) is True:
                    logging.info(login_succeed)
                    time.sleep(3)
                    action.logout()
                    self.wait_element_load_end(login_button)
                    if self.is_element_exist(*login_button) is True:
                        logging.info("账号登出成功,用例执行通过")
                        self.assertEqual(self.is_element_exist(*login_button), True)
                    break
                else:
                    logging.error(login_failed)
                    self.driver.delete_all_cookies()
                    time.sleep(i * 2)
            except Exception as e:
                raise e

    def tearDown(self):
        logging.info("用例结束")
        driver = self.driver
        self.assertEqual([], self.verificationErrors)
        # 关闭浏览器、清除缓存
        driver.delete_all_cookies()
        driver.close()
        driver.quit()

if __name__ == '__main__':
    unittest.main()
