# -*- coding: UTF-8 -*-

"""
Author       :  刘建民
Create Date  :  2016/7/1
Edit Date    :  2016/7/21
"""


from selenium.common.exceptions import NoSuchElementException
from attribute import *  # @UnusedWildImport
from BasePage import BasePage
import logging
import datetime
import time


class OperationPageAction(BasePage):
    """
    封装运营模块的页面对象
    """

    # 点击运营模块标签
    def click_operation_tab(self):
        try:
            self.wait_element_load_end(operation_tab_ele)
            self.find_element(operation_tab_ele).click()
        except NoSuchElementException:
            logging.error("没找到运营模块的标签元素")
        except Exception as e:
            raise e

    # 点击运营模块下的“卡券中心”标签
    def click_card_center_tab(self):
        try:
            self.wait_element_load_end(card_center_ele)
            self.find_element(card_center_ele).click()
        except NoSuchElementException:
            pass
        except Exception as e:
            raise e

    # 点击上传大图按钮
    def click_big_pic(self):
        try:
            self.wait_element_load_end(big_pic_ele)
            self.find_element(big_pic_ele).click()
        except NoSuchElementException:
            pass
        except Exception as e:
            raise e

    # 点击上传小图按钮
    def click_small_pic(self):
        try:
            self.wait_element_load_end(small_pic_ele)
            self.find_element(small_pic_ele).click()
        except NoSuchElementException:
            pass
        except Exception as e:
            raise e

    # 元素为fileImage时上传图片
    def upload_pic(self, picture):
        ele = (By.ID, "fileImage")
        ele_locate = "fileImage"
        try:
            self.upload_file(ele, ele_locate, picture)
        except NoSuchElementException:
            pass
        except Exception as e:
            raise e

    # 上传封面大图
    def upload_big_pic(self):
        try:
            ele = (By.ID, "ccPicBigImgDia_btn1")
            self.click_big_pic()
            logging.info("正在上传大图：%s" % big_pic_name)
            self.upload_pic(big_pic_name)
            self.click_confirm_button(ele)
            logging.info("上传大图完毕")
        except Exception as e:
            raise e

    # 上传封面小图
    def upload_small_pic(self):
        try:
            ele = (By.ID, "ccPicBigImgDia_btn1")
            self.click_small_pic()
            logging.info("正在上传小图：%s" % small_pic_name)
            self.upload_pic(small_pic_name)
            self.click_confirm_button(ele)
            logging.info("上传小图完毕")
        except Exception as e:
            raise e

    # 上传图片后点击确认
    def click_confirm_button(self, ele):
        try:
            self.wait_element_load_end(ele)
            self.find_element(ele).click()
        except Exception as e:
            raise e

    # 输入卡券名称
    def type_card_name(self):
        try:
            self.wait_element_load_end(card_name_ele)
            logging.info("输入卡券名称：%s" % card_name)
            self.find_element(card_name_ele).send_keys(card_name)
        except NoSuchElementException:
            pass
        except Exception as e:
            raise e

    # 输入折扣券的折扣率
    def type_card_rebate(self):
        try:
            self.wait_element_load_end(card_rebate_ele)
            logging.info("输入折扣率：%s" % rebate_data)
            self.find_element(card_rebate_ele).send_keys(rebate_data)
        except NoSuchElementException as e:
            raise e
        except Exception as e:
            raise e

    # 选择折扣券有效期为领取后生效
    def select_validity_to_immediately(self):
        try:
            # self.wait_element_load_end(card_validity_ele)
            time.sleep(1)
            logging.info("选择卡券有效期类型为：领取后生效")
            self.find_element(card_validity_ele).click()
        except NoSuchElementException:
            pass
        except Exception as e:
            raise e

    # 输入优惠券的库存
    def type_card_inventory(self):
        try:
            self.wait_element_load_end(card_inventory_ele)
            logging.info("输入卡券库存：%s" % inventory_data)
            self.find_element(card_inventory_ele).send_keys(inventory_data)
        except NoSuchElementException:
            pass
        except Exception as e:
            raise e

    # 点击保存
    def click_card_save_button(self):
        try:
            self.wait_element_load_end(card_save_ele)
            self.find_element(card_save_ele).click()
        except NoSuchElementException:
            pass
        except Exception as e:
            raise e

    # 创建折扣券
    def create_rebate_card(self):
        self.upload_big_pic()
        self.upload_small_pic()
        self.type_card_name()
        self.type_card_rebate()
        self.select_validity_to_immediately()
        self.type_card_inventory()
        self.click_card_save_button()
        time.sleep(1)
        self.driver.switch_to_alert().accept()

    # 验证是否成功创建了卡券
    @property
    def is_card_create_succeed(self):
        try:
            self.wait_element_load_end(new_create_card_ele)
            if self.is_element_exist(new_create_card_ele) is False:
                return False
            elif self.find_element(new_create_card_ele).text == card_name:
                return True
            else:
                return False
        except:
            return False

    # 点击套图管理的新建分类按钮
    def click_create_pickit_classify_button(self):
        try:
            self.wait_element_load_end(create_pickit_classify_ele)
            self.find_element(create_pickit_classify_ele).click()
        except NoSuchElementException:
            logging.error("找不到新建分类按钮")
        except Exception as e:
            raise e

    # 输入套图的分类名称
    def type_classify_name(self):
        try:
            self.wait_element_load_end(classify_name_ele)
            logging.info("输入套图分类名称：%s" % pickit_classify_name)
            self.find_element(classify_name_ele).send_keys(pickit_classify_name)
        except NoSuchElementException:
            logging.error("找不到套图分类名称输入框，输入失败")
        except Exception as e:
            raise e

    # 选择套图分类的颜色标识
    def select_classify_color_type(self):
        try:
            self.wait_element_load_end(color_type_ele)
            logging.info("选择分类的颜色标识：绿色")
            self.find_element(color_type_ele).click()
        except NoSuchElementException:
            logging.error("找不到套图分类颜色标识")
        except Exception as e:
            raise e

    # 创建套图分类完毕后点击保存
    def click_pickit_classify_save_button(self):
        try:
            self.wait_element_load_end(classify_save_ele)
            self.find_element(classify_save_ele).click()
        except NoSuchElementException:
            logging.error("找不到保存按钮")
        except Exception as e:
            raise e

    # 创建套图分类
    def create_pickit_classify(self):
        self.click_create_pickit_classify_button()
        self.type_classify_name()
        self.upload_big_pic()
        self.upload_small_pic()
        self.select_classify_color_type()
        self.click_pickit_classify_save_button()
        time.sleep(2)
        self.driver.switch_to_alert().accept()

    # 验证是否成功创建了套图分类
    def is_pickit_classify_create_succeed(self):
        try:
            self.wait_element_load_end(new_create_pickit_classify_ele)
            if self.is_element_exist(new_create_pickit_classify_ele) is False:
                return False
            elif self.find_element(new_create_pickit_classify_ele).text == pickit_classify_name:
                return True
            else:
                return False
        except Exception:
            raise False

    # 输入套图的名称
    def type_pickit_name(self):
        try:
            # self.wait_element_load_end(*pickit_title_ele)
            logging.info("输入套图的名称：%s" % pickit_name)
            self.find_element(pickit_title_ele).send_keys(pickit_name)
        except NoSuchElementException:
            logging.error("找不到套图名称输入框位置")
        except Exception as e:
            raise e

    # 选择套图的所属分类
    def select_pickit_classify(self):
        try:
            self.wait_element_load_end(pickit_belong_classify_drop_ele)
            self.find_element(pickit_belong_classify_drop_ele).click()
            logging.info("选择套图的所属分类：%s" % self.find_element(pickit_belong_classify_ele).text)
            self.find_element(pickit_belong_classify_ele).click()
        except NoSuchElementException:
            logging.error("找不到套图分类下拉框位置")
        except Exception as e:
            raise e

    # 输入套图介绍
    def type_pickit_description(self):
        try:
            # self.wait_element_load_end(*pickit_description_ele)
            logging.info("输入套图介绍：%s" % pickit_description)
            self.find_element(pickit_description_ele).send_keys(pickit_description)
        except NoSuchElementException:
            logging.error("找不到套图介绍输入框位置")
        except Exception as e:
            raise e

    # 点击上传套图按钮
    def click_add_pickit_pic(self):
        try:
            self.wait_element_load_end(add_pickit_ele)
            self.find_element(add_pickit_ele).click()
        except NoSuchElementException:
            logging.error("找不到上传套图按钮位置")
        except Exception as e:
            raise e

    # 上传套图完毕后点击保存
    def click_save_pickit_button(self):
        try:
            self.wait_element_load_end(pic_confirm_ele)
            self.find_element(pic_confirm_ele).click()
            time.sleep(1)
        except NoSuchElementException:
            logging.error("找不到保存按钮位置")
        except Exception as e:
            raise e

    # 上传套图
    def upload_pickit_pic(self):
        ele = (By.ID, "fileOneImage")
        ele_locate = "fileOneImage"
        try:
            self.click_add_pickit_pic()
            logging.info("正在上传第一张套图：%s" % pickit1)
            self.upload_file(ele, ele_locate, big_pic_name)
            self.click_save_pickit_button()
            logging.info("上传套图完毕")
        except Exception as e:
            raise e

    # 创建套图完毕之后点击保存按钮
    def click_save_button(self):
        try:
            self.wait_element_load_end(pic_save_ele)
            self.find_element(pic_save_ele).click()
        except NoSuchElementException:
            logging.error("找不到保存按钮位置")
        except Exception as e:
            raise e

    # 点击套图的上传小图按钮
    def click_picsmall_pic(self):
        try:
            self.wait_element_load_end(pickit_smallpic_ele)
            self.find_element(pickit_smallpic_ele).click()
        except NoSuchElementException:
            pass
        except Exception as e:
            raise e

    # 上传套图的封面小图
    def upload_picsmall_pic(self):
        try:
            ele = (By.ID, "ccPicBigImgDia_btn1")
            self.click_picsmall_pic()
            logging.info("正在上传小图：%s" % small_pic_name)
            self.upload_pic(small_pic_name)
            self.click_confirm_button(ele)
            logging.info("上传小图完毕")
        except Exception as e:
            raise e

    # 创建套图
    def create_pickit(self):
        self.type_pickit_name()
        self.select_pickit_classify()
        self.upload_big_pic()
        self.upload_small_pic()
        self.type_pickit_description()
        self.upload_pickit_pic()
        self.click_save_button()
        time.sleep(1)
        self.driver.switch_to_alert().accept()

    # 验证是否成功创建了卡券
    def is_pickit_create_succeed(self):
        try:
            self.wait_element_load_end(new_create_pickit_ele)
            if self.is_element_exist(new_create_pickit_ele) is False:
                return False
            elif self.find_element(new_create_pickit_ele).text == pickit_name:
                return True
            else:
                return False
        except:
            return False

    # 输入微助力活动名称
    def type_activity_name(self):
        ele = (By.ID, "raName")
        try:
            self.wait_element_load_end(ele)
            logging.info("输入活动名称：%s" % activity_name)
            self.find_element(ele).send_keys(activity_name)
        except NoSuchElementException:
            logging.error("找不到套图介绍输入框位置")
        except Exception as e:
            raise e

    # 点击微助力的上传大图按钮
    def click_micro_help_bigpic(self):
        ele = (By.ID, "BgiImgUrl")
        try:
            self.wait_element_load_end(ele)
            self.find_element(ele).click()
        except NoSuchElementException:
            logging.error("找不到上传微助力大图位置")
        except Exception as e:
            raise e

    # 点击微助力的上传小图按钮
    def click_micro_help_smallpic(self):
        ele = (By.ID, "ImgSmallUrl")
        try:
            self.wait_element_load_end(ele)
            self.find_element(ele).click()
        except NoSuchElementException:
            logging.error("找不到上传微助力小图位置")
        except Exception as e:
            raise e

    # 上传微助力图片方法
    def upload_file_mh(self, picture):
        ele = (By.ID, "doc")
        ele_locate = 'doc'
        try:
            self.upload_file(ele, ele_locate, picture)
        except NoSuchElementException:
            logging.error("找不到上传位置")
        except Exception as e:
            raise e

    # 上传微助力封面大图
    def upload_mh_big_pic(self):
        ele = (By.XPATH, ".//*[@id='upImgs']/div/div/div[5]/button[2]")
        try:
            self.click_micro_help_bigpic()
            logging.info("正在上传微助力封面大图：%s" % big_pic_name)
            self.upload_file_mh(big_pic_name)
            self.click_confirm_button(ele)
            logging.info("上传大图完毕")
        except Exception as e:
            raise e

    # 上传微助力封面小图
    def upload_mh_small_pic(self):
        ele = (By.XPATH, ".//*[@id='upImgs']/div/div/div[5]/button[2]")
        try:
            time.sleep(1)
            self.click_micro_help_smallpic()
            logging.info("正在上传微助力封面小图：%s" % big_pic_name)
            self.upload_file_mh(small_pic_name)
            self.click_confirm_button(ele)
            logging.info("上传小图完毕")
        except Exception as e:
            raise e

    # 输入微助力活动开始时间
    def type_mh_start_time(self):
        ele = (By.ID, "js-startDate")
        date = time.strftime("%Y-%m-%d %H:%M:%S")
        try:
            self.wait_element_load_end(ele)
            self.driver.execute_script(remove_sd_read_only)
            self.find_element(ele).send_keys(date)
        except NoSuchElementException:
            logging.error("找不到微助力活动开始时间位置")
        except Exception as e:
            raise e

    # 输入微助力活动结束时间
    def type_mh_end_time(self):
        ele = (By.ID, "js-endDate")
        now_time = datetime.datetime.now()
        fur_time = now_time + datetime.timedelta(days=3)
        date = fur_time.strftime("%Y-%m-%d %H:%M:%S")
        try:
            self.wait_element_load_end(ele)
            self.driver.execute_script(remove_ed_read_only)
            self.find_element(ele).send_keys(date)
        except NoSuchElementException:
            logging.error("找不到微助力活动结束时间位置")
        except Exception as e:
            raise e

    # 点击微助力的上传背景图按钮
    def click_micro_help_bgpic(self):
        ele = (By.ID, "raBackgroundImgUrl")
        try:
            self.wait_element_load_end(ele)
            self.find_element(ele).click()
        except NoSuchElementException:
            logging.error("找不到上传微助力背景图位置")
        except Exception as e:
            raise e

    # 上传微助力背景图
    def upload_mh_background_pic(self):
        ele = (By.XPATH, ".//*[@id='upImgs']/div/div/div[5]/button[2]")
        try:
            self.click_micro_help_bgpic()
            logging.info("正在上传微助力背景图：%s" % big_pic_name)
            self.upload_file_mh(big_pic_name)
            self.click_confirm_button(ele)
            logging.info("上传背景图完毕")
        except Exception as e:
            raise e

    # 输入微助力分享标题
    def type_share_title(self):
        ele = (By.ID, 'raShareTitle')
        try:
            self.wait_element_load_end(ele)
            logging.info("输入分享标题：%s" % share_title)
            self.find_element(ele).send_keys(share_title)
        except NoSuchElementException:
            logging.error("找不到分享标题输入框位置")
        except Exception as e:
            raise e

    # 输入分享描述
    def type_share_description(self):
        ele = (By.ID, 'raShareDesc')
        try:
            self.wait_element_load_end(ele)
            logging.info("输入分享描述：%s" % share_description)
            self.find_element(ele).send_keys(share_description)
        except NoSuchElementException:
            logging.error("找不到分享描述输入框位置")
        except Exception as e:
            raise e

    # 创建一个微助力活动
    def create_micro_help(self):
        self.type_activity_name()
        self.upload_mh_big_pic()
        self.upload_mh_small_pic()
        self.type_mh_start_time()
        self.type_mh_end_time()
        self.upload_mh_background_pic()
        self.type_share_title()
        self.type_share_description()
