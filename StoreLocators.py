# -*- coding: UTF-8 -*-


"""
Author       :  Ken-Kei
Create Date  :  2016/09/21
"""


from selenium.webdriver.common.by import By


class SLPageLocators:

    """
    Name         :  门店 - 门店列表 - 元素定位
    Author       :  Ken-Kei
    Create Date  :  2016/09/21
    """

    CREATESTOREBUTTON           = (By.XPATH, ".//*[@id='form']/div[6]/input[2]")
    STORENAME                   = (By.ID, "storeName")
    STORETYPEDROP               = (By.XPATH, ".//*[@id='storeEdit']/table/tbody/tr[1]/td[2]/div/select")
    STORETYPE                   = ".//*[@id='storeEdit']/table/tbody/tr[1]/td[2]/div/select/option[%d]"
    STORESTATUSDROP             = (By.ID, "storeStatus")
    STORESTATUS                 = ".//*[@id='storeStatus']/option[%d]"
    STOREPHONE                  = (By.NAME, 'storePhone')
    CONTACT                     = (By.NAME, 'contactStaff')
    FATHERMANAGESCOPEDROP       = (By.ID, "editfatherId")
    MANAGESCOPEDROP             = (By.ID, "editscopeId")
    FATHERMANAGESCOPE           = ".//*[@id='editfatherId']/option[%d]"
    MANAGESCOPE                 = ".// *[ @ id = 'editscopeId']/option[%d]"
