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
import datetime
import time
from selenium.webdriver.common.keys import Keys


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