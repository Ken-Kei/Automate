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

    # 门店列表 - 点击门店类型下拉框
    def click_store_type_drop(self):
        try:
            self.click(SLPageLocators.STORETYPEDROP)
        except NoSuchElementException:
            logging.error(SLLogInfo.STORETYPEDROPNOTFOUND)
        except Exception as e:
            raise e

    # 门店列表 - 选择门店类型
    def select_store_type(self):
        try:
            self.click_store_type_drop()
            # 1为直营店，2为加盟店，3为虚拟门店
            if store_type in [1, 2, 3]:
                st = (By.XPATH, SLPageLocators.STORETYPE % store_type + 1)
                logging.info(SLLogInfo.SELECTSTORETYPE % self.find_element(st).text)
                self.click(st)
            else:
                logging.error(SLLogInfo.WRONGSTORETYPE)
                raise ValueError(SLLogInfo.WRONGSTORETYPE)
        except NoSuchElementException:
            logging.error(SLLogInfo.STORETYPENOTFOUND % store_type)
        except Exception as e:
            raise e
