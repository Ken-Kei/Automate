# -*- coding: UTF-8 -*-


"""
Author       :  Ken-Kei
Create Date  :  2016/07/01
"""


from LoginPage import *
from OperationPage import *
import unittest
from attribute import *  # @UnusedWildImport
from LoginLocators import *
from BasePage import BasePage
import logging


class LaunchOperationCase(unittest.TestCase, BasePage):
    """家居精灵-> 运营模块 - 自动化测试用例"""
    
    def setUp(self):
        self.verificationErrors = []
        self.driver = self.get_driver()
        self.lpa = LoginPageAction(self.driver)
        self.pma = PictureManageAction(self.driver)
        self.ccpa = CardCenterPageAction(self.driver)
        self.mha = MicroHelpPageAction(self.driver)
        self.qrpa = ChannalQRCodePageAction(self.driver)

    def test_CreatePictureClassify(self):
        """创建套图分类"""

        flag = False
        logging.info("执行用例：%s" % test_CreatePictureClassify)
        try:
            self.lpa.login(pickit_manage_url, username, password)  # 打开套图管理的url并验证登录
            logging.info(loging_in % username)
            self.wait_element_load_end(LoginPageLocators.LOGOUTBUTTON)
            if self.is_element_exist(LoginPageLocators.LOGOUTBUTTON) is True:
                logging.info(LoginLogInfo.LOGINSUCCEED)
                self.pma.create_pickit_classify()  # 判断登录成功后开始创建套图分类
                if self.is_create_succeed(PMPageLocators.NEWPICTURECLASSIFY, picture_classify_name) is True:
                    logging.info(PMLogInfo.PICCLASSCREATESUCCEED)
                    self.create_screen_shot(create_pc_succeed_screenshot, tc_name=test_CreatePictureClassify)
                    flag = True
                else:
                    logging.error(PMLogInfo.PICCLASSCREATEFAILED)
                    self.create_screen_shot(create_pc_failed_screenshot, tc_name=test_CreatePictureClassify)
            else:
                logging.error(LoginLogInfo.LOGINFAILED)
                self.driver.delete_all_cookies()
        except Exception as e:
            raise e
        self.assertEqual(flag, True)

    def test_CreatePictureKit(self):
        """创建套图"""

        flag = False
        logging.info("执行用例：%s" % test_CreatePictureKit)
        # 登录
        try:
            # 打开卡券中心的url并验证登录
            self.lpa.login(pickit_url, username, password)
            logging.info(loging_in % username)
            self.wait_element_load_end(LoginPageLocators.LOGOUTBUTTON)
            if self.is_element_exist(LoginPageLocators.LOGOUTBUTTON) is True:
                logging.info(LoginLogInfo.LOGINSUCCEED)
                self.pma.create_pickit()  # 判断登录成功后开始创建套图
                if self.is_create_succeed(PMPageLocators.NEWPICTURE, picture_name) is True:
                    logging.info(PMLogInfo.PICCREATESUCCEED)
                    self.create_screen_shot(create_pk_succeed_screenshot, tc_name=test_CreatePictureKit)
                    flag = True
                else:
                    logging.error(PMLogInfo.PICCREATEFAILED)
                    self.create_screen_shot(create_pk_failed_screenshot, tc_name=test_CreatePictureKit)
            else:
                logging.error(LoginLogInfo.LOGINFAILED)
                self.driver.delete_all_cookies()
        except Exception as e:
            raise e
        self.assertEqual(flag, True)

    def test_CreateCard(self):
        """创建卡券"""

        flag = False
        logging.info("执行用例：%s " % test_CreateCard)
        try:
            self.lpa.login(card_center_url, username, password)  # 打开卡券中心的url并验证登录
            logging.info(loging_in % username)
            self.wait_element_load_end(LoginPageLocators.LOGOUTBUTTON)
            if self.is_element_exist(LoginPageLocators.LOGOUTBUTTON) is True:
                logging.info(LoginLogInfo.LOGINSUCCEED)
                self.ccpa.create_rebate_card()  # 判断登录成功后开始创建卡券
                if self.is_create_succeed(CCPageLocators.NEWCARD, card_name) is True:
                    logging.info(CCLogInfo.CARDCREATESUCCEED)
                    self.create_screen_shot(create_card_succeed_screenshot, tc_name=test_CreateCard)
                    flag = True
                else:
                    logging.error(CCLogInfo.CARDCREATEFAILED)
                    self.create_screen_shot(create_card_failed_screenshot, tc_name=test_CreateCard)
            else:
                logging.error(LoginLogInfo.LOGINFAILED)
                self.driver.delete_all_cookies()
        except Exception as e:
            raise e
        self.assertEqual(flag, True)

    def test_CreateMicroHelp(self):
        """创建微助力活动"""

        flag = False
        logging.info("执行用例：%s" % test_CreateMicroHelp)
        # 登录
        try:
            self.lpa.login(micro_help_url, username, password)  # 打开微助力的url并验证登录
            logging.info(loging_in % username)
            self.wait_element_load_end(LoginPageLocators.LOGOUTBUTTON)
            if self.is_element_exist(LoginPageLocators.LOGOUTBUTTON) is True:
                logging.info(LoginLogInfo.LOGINSUCCEED)
                self.mha.create_micro_help()  # 判断登录成功后开始创建微助力活动
                if self.is_create_succeed(MHPageLocators.NEWMICROHELP, activity_name) is True:
                    logging.info(MHLogInfo.MHCREATESUCCEED)
                    self.create_screen_shot(create_mh_succeed_screenshot, tc_name=test_CreateMicroHelp)
                    flag = True
                else:
                    logging.error(MHLogInfo.MHCREATEFAILED)
                    self.create_screen_shot(create_mh_failed_screenshot, tc_name=test_CreateMicroHelp)
            else:
                logging.error(LoginLogInfo.LOGINFAILED)
                self.driver.delete_all_cookies()
        except Exception as e:
            raise e
        self.assertEqual(flag, True)

    def test_CreateQRCode(self):
        """创建渠道二维码"""

        flag = False
        judge = ''
        logging.info("执行用例：%s" % test_CreateQRCode)
        # 登录
        try:
            self.lpa.login(qrcode_url, username, password)  # 打开渠道二维码的url并验证登录
            logging.info(loging_in % username)
            self.wait_element_load_end(LoginPageLocators.LOGOUTBUTTON)
            if self.is_element_exist(LoginPageLocators.LOGOUTBUTTON) is True:
                logging.info(LoginLogInfo.LOGINSUCCEED)
                self.qrpa.create_qrcode()  # 判断登录成功后开始创建二维码
                self.qrpa.click_qrcode_list()  # 点击二维码列表验证二维码是否创建成功
                # 当配置的类型为3时创建两种二维码
                if qrcode_type == 3:
                    judge = self.is_create_succeed(CQPageLocators.NEWQRCODE, qrcode_forever_name,
                                                   CQPageLocators.SECNEWQRCODE, qrcode_temp_name)
                # 当配置的类型为1时创建临时二维码
                elif qrcode_type == 1:
                    judge = self.is_create_succeed(CQPageLocators.SECNEWQRCODE, qrcode_temp_name)
                # 当配置的类型为2时创建永久二维码
                elif qrcode_type == 2:
                    judge = self.is_create_succeed(CQPageLocators.NEWQRCODE, qrcode_forever_name)
                if judge is True:
                    logging.info(CQLogInfo.CODECREATESUCCEED)
                    self.create_screen_shot(create_code_succeed_screenshot, tc_name=test_CreateQRCode)
                    flag = True
                else:
                    logging.error(CQLogInfo.CODECREATEFAILED)
                    self.create_screen_shot(create_code_failed_screenshot, tc_name=test_CreateQRCode)
            else:
                logging.error(LoginLogInfo.LOGINFAILED)
                self.driver.delete_all_cookies()
        except Exception as e:
            raise e
        self.assertEqual(flag, True)

    def tearDown(self):
        logging.info("用例结束")
        self.assertEqual([], self.verificationErrors)
        # 关闭浏览器
        self.driver.delete_all_cookies()
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
