# -*- coding: UTF-8 -*-

"""
Author       :  刘建民
Create Date  :  2016/7/1
Edit Date    :  2016/7/8
"""


from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from attribute import *  # @UnusedWildImport
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


class BasePage(object):
    """
    封装基础的方法，如获取驱动、查找页面元素，输入url等
    """
    
    def __init__(self, driver):
        self.driver = driver
        self.timeout = 30
        
    def find_element(self, *loc):
        return self.driver.find_element(*loc)

    def type_url(self, url):
        try:
            # driver.maximize_window()
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
        for i in range(0, 3):
            try:
                wait.until(EC.element_to_be_clickable(*element))
                # wait.until(self.find_element(*element))
                break
            except:
                time.sleep(i * 1)

    # 判断是否有alert窗口
    def is_alert_exist(self):
        wait = WebDriverWait(self.driver, waiting_time)
        for i in range(0, 3):
            try:
                wait.until(EC.alert_is_present())
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
            flag = True
        except:
            flag = False
        return flag

    def upload_file(self, file_name):
        try:
            file_path = os.path.join(os.path.abspath(file_name))
            self.wait_element_load_end(*upload_button_ele)
            self.driver.execute_script("""document.getElementById('fileImage').style.display='block'; """)
            self.find_element(*display_upload_button_ele).send_keys(file_path)
        except Exception as e:
            raise e
