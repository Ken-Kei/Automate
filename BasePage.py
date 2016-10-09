# -*- coding: UTF-8 -*-

"""
Author       :  Ken-Kei
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
    Author       :  Ken-Kei
    Create Date  :  2016/08/24
    """
    
    def __init__(self, driver):
        self.driver = driver
        self.timeout = 40
        
    def find_element(self, loc):
        return self.driver.find_element(*loc)

    def type_url(self, url):
        try:
            self.driver.maximize_window()
            self.driver.get(self.merge_launch_url(url))
        except Exception as e:
            raise e

    def click(self, locator):
        self.wait_element_load_end(locator)
        self.find_element(locator).click()

    def type(self, locator, text):
        self.find_element(locator).clear()
        self.wait_element_load_end(locator)
        self.find_element(locator).send_keys(text)

    def type_in_iframe(self, frame_loc, loc, text):

        """
        :param frame_loc    : The locator of the frame.
        :param loc          : The locator of which element you want to handled.
        :param text         : The text you want to type.
        """

        self.driver.switch_to_frame(frame_loc)
        self.find_element(loc).clear()
        self.wait_element_load_end(loc)
        self.find_element(loc).send_keys(text)
        self.driver.switch_to_default_content()

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

    # 等待alert窗口
    def wait_alert_load_end(self):
        wait = WebDriverWait(self.driver, waiting_time)
        try:
            wait.until(ec.alert_is_present())
        except:
            time.sleep(1)

    # 对alert窗口作处理
    def handle_alert(self):
        try:
            self.wait_alert_load_end()
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

        """
        :param ele      : This is the upload locator which is the real locator to upload image,
                          e.g: (By.ID, "fileImage").
        :param locator  : Locator's attribute, e.g: "fileImage".
        :return         : Due to the different status of the @style(exist or not),
                          return True or False.
        """

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

        """
        :param ue           : This is the upload locator which is the real locator to upload image,
                              e.g: (By.ID, "fileImage").
        :param locator      : Locator's attribute, e.g: "fileImage".
        :param file_name    : The image you want to upload.
        """

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

    # # 创建截图存放目录
    # @staticmethod
    # def create_screenshot_path():
    #     try:
    #         screenshot_path = com.create_path(launch_screenshot_path)
    #         return screenshot_path
    #     except Exception as e:
    #         raise e

    # 截图
    def create_screen_shot(self, screenshot_name, tc_name=None):

        """
        :param screenshot_name  : The name of screen shot.
        :param tc_name          : This is a default parameter, you can assign a value when you want to save
                                  screenshot with a single directory named by the name of the test case,
                                  such as: tc_name=test_LoginSucceed.
        """

        try:
            if need_screenshot.lower() == 'n':
                return None
            elif need_screenshot.lower() == 'y':
                screenshot_path = com.create_path(launch_screenshot_path, tc_name)
                screenshot = os.path.join(screenshot_path, screenshot_name + '_%s.jpg') % time.strftime("%H%M%S")
                self.driver.save_screenshot(screenshot)
                time.sleep(2)
            else:
                logging.error("need_screenshot字段配置错误，请检查配置文件！")
        except Exception as e:
            raise e

    # 点击上传图片按钮
    def click_upload_button(self, ele):
        try:
            self.click(ele)
        except NoSuchElementException:
            logging.error(PublicLogInfo.UPLOADNOTFOUND)
        except Exception as e:
            raise e

    # 上传封面大图
    def upload_pic(self, button_ele, ele, ele_locate, confrim_ele, log_content):

        """
        :param button_ele   : The upload button locator.
        :param ele          : This is the upload locator which is the whole locator to upload image,
                              e.g: (By.ID, "fileImage").
        :param ele_locate   : Locator's attribute, e.g: "fileImage".
        :param confrim_ele  : The confirm button locator.
        :param log_content  : The log content will print when finish uploading image.
        """

        logging.info(PublicLogInfo.UPLOADINGBIGPIC % big_image_name)
        self.click_upload_button(button_ele)
        self.upload_image(ele, ele_locate, big_image_name)
        self.click_confirm_button(confrim_ele)
        logging.info(log_content)

    # 上传封面小图
    def upload_pic(self, button_ele, ele, ele_locate, confrim_ele):
        logging.info(PublicLogInfo.UPLOADINGSMALLPIC % small_image_name)
        self.click_upload_button(button_ele)
        self.upload_image(ele, ele_locate, small_image_name)
        self.click_confirm_button(confrim_ele)
        logging.info(PublicLogInfo.UPLOADSMALLPICFIN)

    # 上传图片后点击确认
    def click_confirm_button(self, ele):
        try:
            self.click(ele)
        except NoSuchElementException:
            logging.error(PublicLogInfo.CONFIRMNOTFOUND)
        except Exception as e:
            raise e

    # 点击保存按钮
    def click_save_button(self, ele):
        try:
            self.click(ele)
        except NoSuchElementException:
            logging.error(PublicLogInfo.SAVEBUTTONNOTFOUND)
        except Exception as e:
            raise e

    # 验证是否成功创建对应内容
    def is_create_succeed(self, ele, event_name, sec_ele=None, sec_event_name=None):

        """
        :param ele              : The locator of the key word which is considered to judge the creation is exist.
        :param event_name       : The name of the creation.
        :param sec_ele          : The second locator of the key word which is considered to judge the creation
                                  is exist, the default value is None.
        :param sec_event_name   : The name of the second creation, the default value is None.
        """
        try:
            self.wait_element_load_end(ele)
            if self.is_element_exist(ele) is False:
                return False
            elif self.find_element(ele).text == event_name:
                # 当第一个创建的内容判断通过后，再判断第二个是否也判断通过
                if sec_ele is not None:
                    if self.is_element_exist(sec_ele) is False:
                        return False
                    # 当第二个内容也判断通过后，才返回True
                    elif self.find_element(sec_ele).text == sec_event_name:
                        return True
                # 如果没有传入第二个元素，则直接返回True
                else:
                    return True
            else:
                return False
        except:
            return False

    # 点击下拉框
    def click_drop_down_list(self, ele):
        try:
            self.click(ele)
        except NoSuchElementException:
            logging.error(PublicLogInfo.DROPDOWNLISTNOTFOUND)
        except Exception as e:
            raise e
