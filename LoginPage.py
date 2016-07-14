# -*- coding: UTF-8 -*-


"""
Author       :  刘建民
Create Date  :  2016/7/1
Edit Date    :  2016/7/14
"""


from selenium.common.exceptions import NoSuchElementException
from attribute import *  # @UnusedWildImport
from BasePage import BasePage
import logging


class LoginPageAction(BasePage):
    """
    封装登入以及登出步骤的页面对象
    """

    def type_username(self, usr):
        try:
            self.find_element(*username_input).clear()
            self.find_element(*username_input).send_keys(usr)
        except NoSuchElementException:
            logging.info("1")
        except Exception as e:
            raise e

    def type_password(self, pwd):
        try:
            self.find_element(*password_input).clear()
            self.find_element(*password_input).send_keys(pwd)
        except NoSuchElementException:
            pass
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
            self.wait_element_load_end(login_button)
            self.find_element(*login_button).click()
        except NoSuchElementException:
            pass
        except Exception as e:
            raise e

    def click_logout_button(self):
        try:
            self.wait_element_load_end(logout_button)
            ele_id = self.find_element(*logout_button)
            ele_id.click()
        except NoSuchElementException:
            pass
        except Exception as e:
            raise e
