# -*- coding: UTF-8 -*-

"""
Author       :  刘建民
Create Date  :  2016/07/01
"""


from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from attribute import *  # @UnusedWildImport
from common import CommonUtils
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import logging
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from LogInfo import *
from selenium.webdriver.support import expected_conditions as ec

com = CommonUtils()


class BasePage(object):

    """
    Name         :  公共方法 - 基础页面对象操作
    Author       :  刘建民
    Create Date  :  2016/08/24
    """
    
    def __init__(self, driver):
        self.driver = driver
        self.timeout = 30
        
    def find_element(self, loc):
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
    def wait_element_load_end(self, element):
        wait = WebDriverWait(self.driver, waiting_time)
        try:
            wait.until(ec.presence_of_element_located(*element))
            wait.until(ec.element_to_be_clickable(*element))
        except:
            time.sleep(1)

    # 对alert窗口作处理
    def handle_alert(self):
        try:
            self.driver.switch_to_alert().accept()
        except NoAlertPresentException:
            logging.error(PublicLogInfo.ALERTNOTFOUND)

    def get_driver(self):
        try:
            if browser.lower() == "chrome":
                caps = DesiredCapabilities.CHROME
                caps['trustAllSSLCertificates'] = True
                os.environ['webdriver.chrome.driver'] = chrome_driver_path
                self.driver = webdriver.Chrome(chrome_driver_path)
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
                os.environ['webdriver.ie.driver'] = ie_driver_path
                self.driver = webdriver.Ie(ie_driver_path)
                self.driver.set_page_load_timeout(40)
            else:
                print("It doesn't support other browsers except ie/chrome/firefox")
            time.sleep(3)
            self.driver.delete_all_cookies()
            return self.driver
        except Exception as e:
            raise e

    def is_element_exist(self, ele):
        try:
            self.find_element(ele)
        except NoSuchElementException:
            return False
        return True

    # 判断元素是否存在style属性
    def is_attribute_style_exist(self, ele, locator):
        try:
            ga = self.find_element(ele).get_attribute(locator + "@style")
            if ga is False:
                return False
            elif ga is None:
                return False
            else:
                return True
        except:
            return False

    # 上传图片
    def upload_image(self, ue, locator, file_name):
        try:
            file_path = os.path.join(os.path.abspath(file_name))
            if self.is_attribute_style_exist(ue, locator) is True:
                if self.is_element_exist(ue) is True:
                    self.driver.execute_script(file_image_block)
                    self.find_element(ue).send_keys(file_path)
                    self.driver.execute_script(file_image_none)
            else:
                self.find_element(ue).send_keys(file_path)
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

    # 点击上传图片按钮
    def click_upload_button(self, ele, log):
        try:
            self.wait_element_load_end(ele)
            self.find_element(ele).click()
        except NoSuchElementException:
            logging.error(log)
        except Exception as e:
            raise e

    # 上传封面大图
    def upload_big_pic(self, button_ele, ele, ele_locate, confrim_ele):
        try:
            self.click_upload_button(button_ele, PublicLogInfo.BIGPICERROR)
            logging.info(PublicLogInfo.UPLOADINGBIGPIC % big_image_name)
            self.upload_image(ele, ele_locate, big_image_name)
            self.click_confirm_button(confrim_ele)
            logging.info(PublicLogInfo.UPLOADBIGPICFIN)
        except Exception as e:
            raise e

    # 上传封面小图
    def upload_small_pic(self, button_ele, ele, ele_locate, confrim_ele):
        try:
            self.click_upload_button(button_ele, PublicLogInfo.SMALLPICERROR)
            logging.info(PublicLogInfo.UPLOADINGSMALLPIC % small_image_name)
            self.upload_image(ele, ele_locate, small_image_name)
            self.click_confirm_button(confrim_ele)
            logging.info(PublicLogInfo.UPLOADSMALLPICFIN)
        except Exception as e:
            raise e

    # 上传图片后点击确认
    def click_confirm_button(self, ele):
        try:
            self.wait_element_load_end(ele)
            self.find_element(ele).click()
        except Exception as e:
            raise e

    # 点击保存按钮
    def click_save_button(self, ele):
        try:
            self.wait_element_load_end(ele)
            self.find_element(ele).click()
        except Exception as e:
            raise e

    # 验证是否成功创建对应内容
    def is_create_succeed(self, ele, event_name):
        try:
            self.wait_element_load_end(ele)
            if self.is_element_exist(ele) is False:
                return False
            elif self.find_element(ele).text == event_name:
                return True
            else:
                return False
        except:
            return False
