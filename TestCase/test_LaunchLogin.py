# -*- coding: UTF-8 -*-


"""
Author       :  刘建民
Create Date  :  2016/07/07
"""

from LoginPage import *
from attribute import *  # @UnusedWildImport
import unittest
import logging


class LaunchLoginCase(unittest.TestCase, BasePage):
    """家居精灵-> 登录模块 - 自动化测试用例"""

    def setUp(self):
        self.verificationErrors = []
        self.driver = self.get_driver()
        self.lp = LoginPageAction(self.driver)

    def test_LoginSucceed(self):
        """登入以及登出O2O平台成功"""

        flag = False
        logging.info("执行用例：登入以及登出O2O平台成功")
        # 登录后台
        try:
            # 打开O2O主页的url并验证登入登出
            self.lp.login(main_url, username, password)
            logging.info(loging_in % username)
            self.wait_element_load_end(LoginPageLocators.LOGOUTBUTTON)
            if self.is_element_exist(LoginPageLocators.LOGOUTBUTTON) is False:
                logging.error(LoginLogInfo.LOGINFAILED)
                self.create_screen_shot(login_failed_screenshot)
                self.driver.delete_all_cookies()
            else:
                logging.info(LoginLogInfo.LOGINSUCCEED)
                self.create_screen_shot(login_succeed_screenshot)
                time.sleep(3)
                self.lp.logout()
                self.wait_element_load_end(LoginPageLocators.LOGINBUTTON)
                if self.is_element_exist(LoginPageLocators.LOGINBUTTON) is True:
                    logging.info("账号登出成功,用例执行通过")
                    self.create_screen_shot(logout_succeed_screenshot)
                    flag = True
                else:
                    logging.error("账号登出失败，用例执行不通过")
                    self.create_screen_shot(logout_failed_screenshot)
                    self.driver.delete_all_cookies()
        except Exception as e:
            raise e
        self.assertEqual(flag, True)

    def test_LoginFailedWithWrongUser(self):
        """错误的用户名登录"""

        flag = False
        logging.info("执行用例：登入以及登出O2O平台成功")
        # 登录后台
        try:
            # 打开O2O主页的url并使用错误的用户名登录
            self.lp.login(main_url, wrong_username, password)
            logging.info(loging_in % wrong_username)
            self.wait_element_load_end(LoginPageLocators.LOGOUTBUTTON)
            if self.is_element_exist(LoginPageLocators.LOGOUTBUTTON) is False:
                logging.info(LoginLogInfo.WRONGUSERLOGINFAILED)
                self.create_screen_shot(login_failed_screenshot)
                self.driver.delete_all_cookies()
            else:
                logging.ERROR(LoginLogInfo.WRONGUSERLOGINSUCCEED)
                self.create_screen_shot(login_succeed_screenshot)
                flag = True
        except Exception as e:
            raise e
        self.assertEqual(flag, False)

    def tearDown(self):
        logging.info("用例结束")

        self.assertEqual([], self.verificationErrors)
        # 关闭浏览器、清除缓存
        self.driver.delete_all_cookies()
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
