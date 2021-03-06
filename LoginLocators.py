# -*- coding: UTF-8 -*-


"""
Author       :  刘建民
Create Date  :  2016/08/23
"""


from selenium.webdriver.common.by import By


class LoginPageLocators:

    """
    Name         :  登入登出 - 元素定位
    Author       :  Ken-Kei
    Create Date  :  2016/08/23
    """

    USERNAME                    = (By.CSS_SELECTOR, "#username")
    PASSWORD                    = (By.CSS_SELECTOR, "#password")
    LOGINBUTTON                 = (By.CSS_SELECTOR, ".loginBtn")
    USERACCOUNT                 = (By.CSS_SELECTOR, "#spnUid")
    LOGOUTBUTTON                = (By.CSS_SELECTOR, ".quit-nav>li>a")
