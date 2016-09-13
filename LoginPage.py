# -*- coding: UTF-8 -*-


"""
Author       :  刘建民
Create Date  :  2016/07/01
"""


from selenium.common.exceptions import NoSuchElementException
from LoginLocators import *
from BasePage import BasePage
import logging
from LogInfo import *


class LoginPageAction(BasePage):

    """
    Name        :  登入登出
    Author      :  刘建民
    Create Date :  2016/08/23
    """

    def type_username(self, usr):
        try:
            self.type(LoginPageLocators.USERNAME, usr)
        except NoSuchElementException:
            logging.error(LoginLogInfo.ACCOUNTNOTFOUND)
        except Exception as e:
            raise e

    def type_password(self, pwd):
        try:
            self.type(LoginPageLocators.PASSWORD, pwd)
        except NoSuchElementException:
            logging.error(LoginLogInfo.PASSNOTFOUND)
        except Exception as e:
            raise e

    # 封装了输入url,输入用户名，输入密码并且点击登录按钮的登入操作
    def login(self, url, usr, pwd):
        self.type_url(url)
        self.type_username(usr)
        self.type_password(pwd)
        self.click_login_button()

    def logout(self):
        self.click_logout_button()

    def click_login_button(self):
        try:
            self.click(LoginPageLocators.LOGINBUTTON)
        except NoSuchElementException:
            logging.error(LoginLogInfo.LOGINBUTTONNOTFOUND)
        except Exception as e:
            raise e

    def click_logout_button(self):
        try:
            self.click(LoginPageLocators.LOGOUTBUTTON)
        except NoSuchElementException:
            logging.error(LoginLogInfo.LOGOUTNOTFOUND)
        except Exception as e:
            raise e
