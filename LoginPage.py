# -*- coding: UTF-8 -*-


"""
Author       :  刘建民
Create Date  :  2016/07/01
"""


from selenium.common.exceptions import NoSuchElementException
from attribute import *  # @UnusedWildImport
from LoginLocators import *
from BasePage import BasePage
import logging


class LoginPageAction(BasePage):
    """
    Name        :  登入登出
    Author      :  刘建民
    Create Date :  2016/08/23
    """

    def type_username(self, usr):
        try:
            self.find_element(LoginPageLocators.USERNAME).clear()
            self.find_element(LoginPageLocators.USERNAME).send_keys(usr)
        except NoSuchElementException:
            logging.info("找不到账号输入框")
        except Exception as e:
            raise e

    def type_password(self, pwd):
        try:
            self.find_element(LoginPageLocators.PASSWORD).clear()
            self.find_element(LoginPageLocators.PASSWORD).send_keys(pwd)
        except NoSuchElementException:
            logging.info("找不到密码输入框")
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
        time.sleep(5)

    def click_login_button(self):
        try:
            self.wait_element_load_end(LoginPageLocators.LOGINBUTTON)
            self.find_element(LoginPageLocators.LOGINBUTTON).click()
        except NoSuchElementException:
            pass
        except Exception as e:
            raise e

    def click_logout_button(self):
        try:
            self.wait_element_load_end(LoginPageLocators.LOGOUTBUTTON)
            ele_id = self.find_element(LoginPageLocators.LOGOUTBUTTON)
            ele_id.click()
        except NoSuchElementException:
            pass
        except Exception as e:
            raise e
