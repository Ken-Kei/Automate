# -*- coding: UTF-8 -*-

"""
Author       :  Ken-Kei
Create Date  :  2016/09/21
"""

from selenium.common.exceptions import NoSuchElementException
from attribute import *  # @UnusedWildImport
from StoreLocators import *
from LogInfo import *
from BasePage import BasePage
import logging


class CardCenterPageAction(BasePage):
    """
    Name        :  门店 -> 门店列表
    Author      :  Ken-Kei
    Create Date :  2016/09/21
    """

    # 门店列表 - 点击新增按钮
    def click_create_store_button(self):
        try:
            self.click(SLPageLocators.CREATESTOREBUTTON)
        except NoSuchElementException:
            logging.error(SLLogInfo.CREATEBUTTONNOTFOUND)
        except Exception as e:
            raise e

    # 门店列表 - 输入门店名称
    def type_store_name(self):
        try:
            logging.info(SLLogInfo.TYPESTORENAME % store_name)
            self.type(SLPageLocators.STORENAME, store_name)
        except NoSuchElementException:
            logging.error(SLLogInfo.STORENAMENOTFOUND)
        except Exception as e:
            raise e

    # # 门店列表 - 点击门店类型下拉框
    # def click_store_type_drop(self):
    #     try:
    #         self.click(SLPageLocators.STORETYPEDROP)
    #     except NoSuchElementException:
    #         logging.error(SLLogInfo.STORETYPEDROPNOTFOUND)
    #     except Exception as e:
    #         raise e

    # 门店列表 - 选择门店类型
    def select_store_type(self):
        st = (By.XPATH, SLPageLocators.STORETYPE % store_type + 1)
        try:
            # 点击下拉框
            self.click_drop_down_list(SLPageLocators.STORETYPEDROP)
            # 1为直营店，2为加盟店，3为虚拟门店
            if store_type in range(1, 4):

                logging.info(SLLogInfo.SELECTSTORETYPE % self.find_element(st).text)
                self.click(st)
            else:
                logging.error(SLLogInfo.WRONGSTORETYPE)
                raise ValueError(SLLogInfo.WRONGSTORETYPE)
        except NoSuchElementException:
            logging.error(SLLogInfo.STORETYPENOTFOUND % self.find_element(st).text)
        except Exception as e:
            raise e

    # 门店列表 - 选择门店状态
    def select_store_status(self):
        st = (By.XPATH, SLPageLocators.STORESTATUS % store_status + 1)
        try:
            # 点击下拉框
            self.click_drop_down_list(SLPageLocators.STORESTATUSDROP)
            # 1为已经开业，2为暂停营业，3为尚在装修
            if store_status in range(1, 4):
                logging.info(SLLogInfo.SELECTSTORESTATUS % self.find_element(st).text)
                self.click(st)
            else:
                logging.error(SLLogInfo.WRONGSTORESTATUS)
                raise ValueError(SLLogInfo.WRONGSTORESTATUS)
        except NoSuchElementException:
            logging.error(SLLogInfo.STORESTATUSNOTFOUND % self.find_element(st).text)
        except Exception as e:
            raise e

    # 输入门店电话
    def type_store_phone(self):
        try:
            logging.info(SLLogInfo.TYPESTOREPHONE % store_phone)
            self.type(SLPageLocators.STOREPHONE, store_phone)
        except NoSuchElementException:
            logging.error(SLLogInfo.STOREPHONENOTFOUND)
        except Exception as e:
            raise e

    # 输入联系人
    def type_contact(self):
        try:
            logging.info(SLLogInfo.TYPECONTACT % store_contact)
            self.type(SLPageLocators.CONTACT, store_contact)
        except NoSuchElementException:
            logging.error(SLLogInfo.CONTACTNOTFOUND)
        except Exception as e:
            raise e

    # 选择经营范围
    def select_manage_scope(self):
        fms = (By.XPATH, SLPageLocators.FATHERMANAGESCOPE % father_manage_scope + 1)
        ms = (By.XPATH, SLPageLocators.MANAGESCOPE % manage_scope + 1)
        try:
            # 点击父级经营范围下拉框
            self.click_drop_down_list(SLPageLocators.FATHERMANAGESCOPEDROP)
            # 如果配置的father_manage_scope字段大于或者小于有效范围则抛出异常，目前有效范围为1
            valid_scope = 2
            if father_manage_scope in range(1, valid_scope) is False:
                logging.error(SLLogInfo.WRONGFATHERMANGESCOPE)
                raise ValueError(SLLogInfo.WRONGFATHERMANGESCOPE)
            elif father_manage_scope in range(1, 2):
                logging.info(SLLogInfo.SELECTMANAGESCOPE % self.find_element(fms).text)
                self.click(fms)
            else:
                logging.error(SLLogInfo.WRONGFATHERMANGESCOPE)
                raise ValueError(SLLogInfo.WRONGFATHERMANGESCOPE)
            # 点击子级经营范围下拉框
            self.click_drop_down_list(SLPageLocators.MANAGESCOPEDROP)
            # 1为汽车/用品/配件/改装
            if manage_scope in range(1, 2):
                logging.info(SLLogInfo.SELECTMANAGESCOPE % self.find_element(ms).text)
                self.click(ms)
            else:
                logging.error(SLLogInfo.WRONGMANGESCOPE)
                raise ValueError(SLLogInfo.WRONGMANGESCOPE)
        except NoSuchElementException:
            logging.error(SLLogInfo.MANAGESCOPENOTFOUND)
        except Exception as e:
            raise e
