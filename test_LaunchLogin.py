# -*- coding: UTF-8 -*-


"""
Author       :  刘建民
Create Date  :  2016/7/7
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
        flag = False
        logging.info("执行用例：登入以及登出O2O平台")
        # 登录后台
        try:
            # 打开O2O主页的url并验证登入登出
            action.login(main_url, username, password)
            logging.info(loging_in % username)
            self.wait_element_load_end(logout_button)
            if self.is_element_exist(logout_button) is False:
                logging.error(login_failed)
                self.create_screen_shot(launch_screenshot_path)
                self.driver.delete_all_cookies()
            else:
                logging.info(login_succeed)
                self.create_screen_shot(launch_screenshot_path)
                time.sleep(3)
                action.logout()
                self.wait_element_load_end(login_button)
                if self.is_element_exist(login_button) is True:
                    logging.info("账号登出成功,用例执行通过")
                    self.create_screen_shot(launch_screenshot_path)
                    flag = True
                else:
                    logging.error("账号登出失败，用例执行不通过")
                    self.create_screen_shot(launch_screenshot_path)
                    self.driver.delete_all_cookies()
        except Exception as e:
            raise e
        self.assertEqual(flag, True)

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
