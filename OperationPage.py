# -*- coding: UTF-8 -*-

"""
Author       :  刘建民
Create Date  :  2016/7/1
"""


from selenium.common.exceptions import NoSuchElementException
from attribute import *  # @UnusedWildImport
from BasePage import BasePage
import logging
import datetime
import time


class PublicMethod(BasePage):
    """
    Name        :  公用方法
    Author      :  刘建民
    Create Date :  2016/08/23
    """

    # 点击上传大图按钮
    def click_big_pic(self, ele):
        try:
            self.wait_element_load_end(ele)
            self.find_element(ele).click()
        except NoSuchElementException:
            logging.error("没找到上传大图的按钮")
        except Exception as e:
            raise e

    # 点击上传小图按钮
    def click_small_pic(self, ele):
        try:
            self.wait_element_load_end(ele)
            self.find_element(ele).click()
        except NoSuchElementException:
            logging.error("没找到上传小图的按钮")
        except Exception as e:
            raise e

    # 上传图片元素为fileImage且存在style = none
    def upload_file_image_pic(self, ele, ele_locate, picture):
        try:
            self.upload_file(ele, ele_locate, picture)
        except NoSuchElementException:
            logging.error("找不到上传图片的元素位置")
        except Exception as e:
            raise e

    # 上传封面大图
    def upload_big_pic(self, button_ele, ele, ele_locate, confrim_ele):
        try:
            self.click_big_pic(button_ele)
            logging.info("正在上传大图：%s" % big_pic_name)
            self.upload_file_image_pic(ele, ele_locate, big_pic_name)
            self.click_confirm_button(confrim_ele)
            logging.info("上传大图完毕")
        except Exception as e:
            raise e

    # 上传封面小图
    def upload_small_pic(self, button_ele, ele, ele_locate, confrim_ele):
        try:
            self.click_small_pic(button_ele)
            logging.info("正在上传小图：%s" % small_pic_name)
            self.upload_file_image_pic(ele, ele_locate, small_pic_name)
            self.click_confirm_button(confrim_ele)
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

    # 点击保存按钮
    def click_save_button(self, ele):
        try:
            self.wait_element_load_end(ele)
            self.find_element(ele).click()
        except Exception as e:
            raise e


class CardCenterPageAction(PublicMethod, BasePage):
    """
    Name        :  运营 -> 卡券中心
    Author      :  刘建民
    Create Date :  2016/08/23
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
            self.wait_element_load_end(card_validity_ele)
            time.sleep(1)
            logging.info("选择卡券有效期类型为：领取后生效")
            self.find_element(card_validity_ele).click()
        except NoSuchElementException:
            pass
        except Exception as e:
            raise e

    # 点击适用商品上传图片按钮
    def click_suite_goods_button(self):
        ele = (By.ID, 'ccProductImageImg')
        try:
            self.wait_element_load_end(ele)
            self.find_element(ele).click()
        except NoSuchElementException:
            logging.error("没找到上传适用商品的按钮")
        except Exception as e:
            raise e

    # 上传适用商品图片
    def upload_suite_goods_pic(self):
        ele = (By.ID, "ccPicBigImgDia_btn1")
        try:
            self.click_suite_goods_button()
            logging.info("正在上传适用商品图：%s" % big_pic_name)
            self.upload_file_image_pic(file_image_ele, file_image_ele_locate, big_pic_name)
            self.click_confirm_button(ele)
            logging.info("上传适用商品图完毕")
        except Exception as e:
            raise e

    # 输入商品简介
    def type_goods_summary(self):
        ele = (By.ID, "ccProductInfo")
        try:
            self.wait_element_load_end(ele)
            logging.info("输入商品简介：%s" % inventory_data)
            self.find_element(ele).send_keys(goods_summary)
        except NoSuchElementException:
            logging.error("没找到商品简介的元素位置")
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

    # 创建折扣券
    def create_rebate_card(self):
        self.upload_big_pic(big_pic_ele, file_image_ele, file_image_ele_locate, confirm_ele)
        self.upload_small_pic(small_pic_ele, file_image_ele, file_image_ele_locate, confirm_ele)
        self.type_card_name()
        self.type_card_rebate()
        self.select_validity_to_immediately()
        self.upload_suite_goods_pic()
        self.type_goods_summary()
        self.type_card_inventory()
        self.click_save_button(card_save_ele)
        time.sleep(1)
        self.driver.switch_to_alert().accept()

    # 验证是否成功创建了卡券
    def is_card_create_succeed(self):
        ele = (By.XPATH, ".//*[@id='setting']/table/tbody/tr[1]/td[1]")
        try:
            self.wait_element_load_end(ele)
            if self.is_element_exist(ele) is False:
                return False
            elif self.find_element(ele).text == card_name:
                return True
            else:
                return False
        except:
            return False


class PictureManage(PublicMethod, BasePage):
    """
    Name        :  运营 -> 套图管理
    Author      :  刘建民
    Create Date :  2016/08/23
    """

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
        self.upload_big_pic(big_pic_ele, file_image_ele, file_image_ele_locate, confirm_ele)
        self.upload_small_pic(small_pic_ele, file_image_ele, file_image_ele_locate, confirm_ele)
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

    # 上传套图
    def upload_pickit_pic(self):
        ele = (By.ID, "fileOneImage")
        ele_locate = "fileOneImage"
        pic_confirm_ele = (By.ID, "dialog_save")
        try:
            self.click_add_pickit_pic()
            logging.info("正在上传第一张套图：%s" % pickit1)
            self.upload_file(ele, ele_locate, big_pic_name)
            self.click_save_button(pic_confirm_ele)
            logging.info("上传套图完毕")
        except Exception as e:
            raise e

    # 创建套图
    def create_pickit(self):
        self.type_pickit_name()
        self.select_pickit_classify()
        self.upload_big_pic(big_pic_ele, file_image_ele, file_image_ele_locate, confirm_ele)
        self.upload_small_pic(small_pic_ele, file_image_ele, file_image_ele_locate, confirm_ele)
        self.type_pickit_description()
        self.upload_pickit_pic()
        self.click_save_button(pickit_save_ele)
        time.sleep(1)
        self.driver.switch_to_alert().accept()

    # 验证是否成功创建了套图
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


class MicroHelp(PublicMethod, BasePage):
    """
    Name        :  运营 -> 微助力
    Author      :  刘建民
    Create Date :  2016/08/23
    """

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
    def click_micro_help_bgpic(self, ele):
        try:
            self.wait_element_load_end(ele)
            self.find_element(ele).click()
        except NoSuchElementException:
            logging.error("找不到上传微助力背景图位置")
        except Exception as e:
            raise e

    # 上传微助力背景图
    def upload_mh_background_pic(self):
        mh_background_confirm_ele = (By.XPATH, ".//*[@id='upImgs']/div/div/div[5]/button[2]")
        try:
            self.click_micro_help_bgpic(mh_background_button_ele)
            logging.info("正在上传微助力背景图：%s" % big_pic_name)
            self.upload_file(doc_ele, doc_ele_locate, big_pic_name)
            self.click_confirm_button(mh_background_confirm_ele)
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

    # 输入活动详情
    def type_event_description(self):
        ele = (By.XPATH, "html/body")
        iframe_ele = "ueditor_0"
        try:
            self.driver.switch_to_frame(iframe_ele)
            self.wait_element_load_end(ele)
            self.find_element(ele).send_keys(event_description)
            self.driver.switch_to_default_content()
        except NoSuchElementException:
            logging.error("找不到活动详情的元素位置")
        except Exception as e:
            raise e

    # 输入好友集满数量
    def type_friend_collect_number(self):
        ele = (By.ID, 'raNum')
        try:
            self.wait_element_load_end(ele)
            logging.info("输入好友集满数量：%s" % friend_collect_number)
            self.find_element(ele).send_keys(friend_collect_number)
        except NoSuchElementException:
            logging.error("找不到好友集满数量输入框位置")
        except Exception as e:
            raise e

    # 输入好友集满数量的单位
    def type_friend_collect_unit(self):
        ele = (By.ID, 'raUnit')
        try:
            self.wait_element_load_end(ele)
            logging.info("输入好友集满数量：%s" % unit)
            self.find_element(ele).send_keys(unit)
        except NoSuchElementException:
            logging.error("找不到单位输入框位置")
        except Exception as e:
            raise e

    # 输入好友有效助力概率
    def type_friend_valid_chance(self):
        ele = (By.ID, 'raPro')
        try:
            self.wait_element_load_end(ele)
            logging.info("输入好友有效助力概率：%s" % friend_valid_chance)
            self.find_element(ele).send_keys(friend_valid_chance)
        except NoSuchElementException:
            logging.error("找不到好友有效助力概率输入框位置")
        except Exception as e:
            raise e

    # 输入数量设置
    def type_number_config(self):
        ele = (By.ID, 'raTotalPeople')
        try:
            self.wait_element_load_end(ele)
            logging.info("输入数量设置：%s" % number_config)
            self.find_element(ele).send_keys(number_config)
        except NoSuchElementException:
            logging.error("找不到数量设置输入框位置")
        except Exception as e:
            raise e

    # 点击添加奖品
    def click_add_prize(self):
        ele = (By.XPATH, ".//*[@id='setForm']/div[4]/div[3]/div[5]/div")
        try:
            self.wait_element_load_end(ele)
            self.find_element(ele).click()
        except NoSuchElementException:
            logging.error("找不到添加奖品按钮位置")
        except Exception as e:
            raise e

    # 选择奖品
    def select_prize(self):
        prize_name_ele = (By.XPATH, ".//*[@id='awardForm']/div/div[2]/table/tbody/tr[2]/td/div/select")
        prize_number_ele = (By.XPATH, ".//*[@id='awardForm']/div/div[2]/table/tbody/tr[3]/td/div/input")
        ele = (By.ID, 'addAward')
        try:
            self.click_add_prize()
            self.wait_element_load_end(prize_name_ele)
            self.find_element(prize_name_ele).click()
            for i in range(1, 11):
                select_ele = (By.XPATH,
                              ".//*[@id='awardForm']/div/div[2]/table/tbody/tr[2]/td/div/select/option[%d]" % i)
                self.find_element(select_ele).click()
                if int(self.find_element(prize_number_ele).get_attribute("value")) > 0:
                    self.find_element(prize_number_ele).clear()
                    self.find_element(prize_number_ele).send_keys(prize_number)
                    self.click_confirm_button(ele)
                    break
        except NoSuchElementException:
            logging.error("找不到添加奖品按钮位置")
        except Exception as e:
            raise e

    # 创建一个微助力活动
    def create_micro_help(self):
        self.type_activity_name()
        self.upload_big_pic(micro_bigpic_ele, doc_ele, doc_ele_locate, micro_confirm_ele)
        self.upload_small_pic(micro_smallpic_ele, doc_ele, doc_ele_locate, micro_confirm_ele)
        self.type_mh_start_time()
        self.type_mh_end_time()
        self.upload_mh_background_pic()
        self.type_share_title()
        self.type_share_description()
        self.type_event_description()
        self.type_friend_collect_number()
        self.type_friend_collect_unit()
        self.type_friend_valid_chance()
        self.type_number_config()
        self.select_prize()
        self.click_save_button(mh_save_ele)
        time.sleep(1)
        self.driver.switch_to_alert().accept()

    # 判断微助力活动是否创建成功
    def is_mh_create_succeed(self):
        ele = (By.XPATH, ".//*[@id='section']/div[1]/table/tbody/tr[1]/td[3]")
        try:
            self.wait_element_load_end(ele)
            if self.is_element_exist(ele) is False:
                return False
            elif self.find_element(ele).text == activity_name:
                return True
            else:
                return False
        except:
            return False
