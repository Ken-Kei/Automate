# -*- coding: UTF-8 -*-


"""
Author       :  刘建民
Create Date  :  2016/7/1
"""


from LoginPage import LoginPageAction
from OperationPage import OperationPageAction
import unittest
from attribute import *  # @UnusedWildImport
from BasePage import BasePage
from common import CommonUtils
import logging


com = CommonUtils()


class LaunchOperationCase(unittest.TestCase, BasePage):
    """家居精灵-> 运营模块 - 自动化测试用例"""
    
    def setUp(self):
        self.verificationErrors = []
        self.driver = self.get_driver()
        self.action = LoginPageAction(self.driver)
        self.oa = OperationPageAction(self.driver)

    def test_CreatePictureKitClassify(self):
        """创建套图分类"""

        action = self.action
        oa = self.oa
        flag = False
        logging.info("执行用例：创建套图分类")
        # 如果登录失败的话就重新尝试登录，一共尝试3次
        try:
            action.login(pickit_manage_url, username, password)  # 打开套图管理的url并验证登录
            logging.info(loging_in % username)
            self.wait_element_load_end(logout_button)
            if self.is_element_exist(logout_button) is True:
                logging.info(login_succeed)
                oa.create_pickit_classify()  # 判断登录成功后开始创建套图分类
                if oa.is_pickit_classify_create_succeed() is True:
                    logging.info("套图分类创建成功，用例通过")
                    self.create_screen_shot(launch_screenshot_path)
                    flag = True
                else:
                    logging.error("没有找到套图分类，用例执行不通过")
                    self.create_screen_shot(launch_screenshot_path)
            else:
                logging.error(login_failed)
                self.create_screen_shot(launch_screenshot_path)
                self.driver.delete_all_cookies()
        except Exception as e:
            raise e
        self.assertEqual(flag, True)

    def test_CreateCard(self):
        """创建卡券"""

        action = self.action
        oa = self.oa
        flag = False
        logging.info("执行用例：创建卡券")
        # 如果登录失败的话就重新尝试登录，一共尝试3
        try:
            action.login(card_center_url, username, password)  # 打开卡券中心的url并验证登录
            logging.info(loging_in % username)
            self.wait_element_load_end(logout_button)
            if self.is_element_exist(logout_button) is True:
                logging.info(login_succeed)
                oa.create_rebate_card()  # 判断登录成功后开始创建卡券
                if oa.is_card_create_succeed() is True:
                    logging.info("卡券创建成功,用例执行通过")
                    self.create_screen_shot(launch_screenshot_path)
                    flag = True
                else:
                    logging.error("没有找到卡券，用例执行不通过")
                    self.create_screen_shot(launch_screenshot_path)
            else:
                logging.error(login_failed)
                self.create_screen_shot(launch_screenshot_path)
                self.driver.delete_all_cookies()
        except Exception as e:
            raise e
        self.assertEqual(flag, True)

    def test_CreatePictureKit(self):
        """创建套图"""

        action = self.action
        oa = self.oa
        flag = False
        logging.info("执行用例：创建套图")
        # 登录
        try:
            action.login(pickit_url, username, password)  # 打开卡券中心的url并验证登录
            logging.info(loging_in % username)
            self.wait_element_load_end(logout_button)
            if self.is_element_exist(logout_button) is True:
                logging.info(login_succeed)
                oa.create_pickit()  # 判断登录成功后开始创建套图
                if oa.is_pickit_create_succeed() is True:
                    logging.info("套图创建成功，用例通过")
                    self.create_screen_shot(launch_screenshot_path)
                    flag = True
                else:
                    logging.error("没有找到套图，用例执行不通过")
                    self.create_screen_shot(launch_screenshot_path)
            else:
                logging.error(login_failed)
                self.create_screen_shot(launch_screenshot_path)
                self.driver.delete_all_cookies()
        except Exception as e:
            raise e
        self.assertEqual(flag, True)

    def test_CreateMicroHelp(self):
        """创建微助力活动"""

        action = self.action
        oa = self.oa
        flag = False
        logging.info("执行用例：创建微助力活动")
        # 登录
        try:
            action.login(micro_help_url, username, password)  # 打开微助力的url并验证登录
            logging.info(loging_in % username)
            self.wait_element_load_end(logout_button)
            if self.is_element_exist(logout_button) is True:
                logging.info(login_succeed)
                oa.create_micro_help()  # 判断登录成功后开始创建微助力活动
                if oa.is_mh_create_succeed() is True:
                    logging.info("微助力活动创建成功，用例通过")
                    self.create_screen_shot(launch_screenshot_path)
                    flag = True
                else:
                    logging.error("没有找到微助力活动，用例执行不通过")
                    self.create_screen_shot(launch_screenshot_path)
            else:
                logging.error(login_failed)
                self.create_screen_shot(launch_screenshot_path)
                self.driver.delete_all_cookies()
        except Exception as e:
            raise e
        self.assertEqual(flag, True)

    def tearDown(self):
        logging.info("用例结束")
        driver = self.driver
        self.assertEqual([], self.verificationErrors)
        # 关闭浏览器
        driver.delete_all_cookies()
        driver.close()
        driver.quit()

if __name__ == '__main__':
    unittest.main()
