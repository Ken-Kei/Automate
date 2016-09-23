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
            logging.error(MHLogInfo.SHARETITLENOTFOUND)
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
