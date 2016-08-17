# -*- coding: UTF-8 -*-

"""
Author       :  刘建民
Create Date  :  2016/7/1
Edit Date    :  2016/7/21
"""


from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from attribute import *  # @UnusedWildImport
from common import CommonUtils
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import logging
from selenium.common.exceptions import NoSuchElementException

com = CommonUtils()


class BasePage(object):
    """
    封装基础的页面操作方法，如获取驱动、查找页面元素，输入url等
    """
    
    def __init__(self, driver):
        self.driver = driver
        self.timeout = 30
        
    def find_element(self, *loc):
        return self.driver.find_element(*loc)

    def type_url(self, url):
        try:
            self.driver.maximize_window()
            self.driver.get(self.merge_launch_url(url))
        except Exception as e:
            raise e

    # to add the "https://" string when the given url doesn't contain it.
    @staticmethod
    def merge_launch_url(hosturl):
        if "http://" not in hosturl:
            hosturl = "http://" + hosturl
        return hosturl
    
    # wait until finish the element loading
    def wait_element_load_end(self, *element):
        wait = WebDriverWait(self.driver, waiting_time)
        try:
            # wait.until(ec.presence_of_element_located(element))
            wait.until(ec.element_to_be_clickable(*element))
            wait.until(ec.presence_of_element_located(*element))
        except:
            time.sleep(1)

    # 判断是否有alert窗口
    def is_alert_exist(self):
        wait = WebDriverWait(self.driver, waiting_time)
        for i in range(0, 3):
            try:
                wait.until(ec.alert_is_present())
                break
            except:
                time.sleep(i * 1)

    def get_driver(self):
        try:
            if browser.lower() == "chrome":
                caps = DesiredCapabilities.CHROME
                caps['trustAllSSLCertificates'] = True
                self.driver = webdriver.Chrome()
                self.driver.set_page_load_timeout(40)
            elif browser.lower() == "firefox":
                self.driver = webdriver.Firefox()
                self.driver.set_page_load_timeout(40)
            elif browser.lower() == "ie":
                caps = DesiredCapabilities.INTERNETEXPLORER
                caps['javascriptEnabled'] = True
                caps['requireWindowFocus'] = True
                caps['acceptSslCerts'] = True
                caps['trustAllSSLCertificates'] = True
                self.driver = webdriver.Ie()
                self.driver.set_page_load_timeout(40)
            else:
                print("It doesn't support other browsers except ie/chrome/firefox")
            time.sleep(3)
            self.driver.delete_all_cookies()
            return self.driver
        except Exception as e:
            raise e

    def is_element_exist(self, *ele):
        try:
            self.find_element(*ele)
        except NoSuchElementException:
            return False
        return True

    def upload_file(self, ue, file_name):
        try:
            file_path = os.path.join(os.path.abspath(file_name))
            if self.is_element_exist(*ue) is True:
                self.driver.execute_script(file_image_block)
                self.find_element(*ue).send_keys(file_path)
                self.driver.execute_script(file_image_none)
            else:
                self.find_element(*ue).send_keys(file_path)
        except Exception as e:
            raise e

    # 截图
    def create_screen_shot(self, screenshot_path):
        try:
            if need_screenshot.lower() == 'n':
                return None
            elif need_screenshot.lower() == 'y':
                screenshot_path = com.create_path(screenshot_path)
                screenshot = os.path.join(screenshot_path, "screenshot_%s.jpg") % time.strftime("%H%M%S")
                time.sleep(2)
                self.driver.save_screenshot(screenshot)
            else:
                logging.error("need_screenshot配置错误，请检查配置文件！")
        except Exception as e:
            raise e
