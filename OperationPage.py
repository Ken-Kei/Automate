# -*- coding: UTF-8 -*-

"""
Author       :  刘建民
Create Date  :  2016/7/1
"""

from selenium.common.exceptions import NoSuchElementException
from attribute import *  # @UnusedWildImport
from OperationLocators import *
from LogInfo import *
from BasePage import BasePage
import logging
import datetime
import time
from selenium.webdriver.common.keys import Keys


class CardCenterPageAction(BasePage):
    """
    Name        :  运营 -> 卡券中心
    Author      :  刘建民
    Create Date :  2016/08/23
    """

    # 点击运营模块标签
    def click_operation_tab(self):
        try:
            self.wait_element_load_end(CCPageLocators.OPERATIONTAB)
            self.find_element(CCPageLocators.OPERATIONTAB).click()
        except NoSuchElementException:
            logging.error(CCLogInfo.OPERTABNOTFOUND)
        except Exception as e:
            raise e

    # 点击运营模块下的“卡券中心”标签
    def click_card_center_tab(self):
        try:
            self.wait_element_load_end(CCPageLocators.CARDCENTER)
            self.find_element(CCPageLocators.CARDCENTER).click()
        except NoSuchElementException:
            pass
        except Exception as e:
            raise e

    # 卡券中心 - 输入卡券名称
    def type_card_name(self):
        try:
            self.wait_element_load_end(CCPageLocators.CARDNAME)
            logging.info(CCLogInfo.TYPECARDNAME % card_name)
            self.find_element(CCPageLocators.CARDNAME).send_keys(card_name)
            self.driver.switch_to_active_element().send_keys(Keys.TAB)
            if self.find_element(CCPageLocators.TITLEFAULTTIP).text == '卡券名称已存在!':
                raise logging.error(CCLogInfo.CARDNAMEEXIST)
        except NoSuchElementException:
            logging.error(CCLogInfo.CARDNAMENOTFOUND)
        except Exception as e:
            raise e

    # 卡券中心 - 输入折扣券的折扣率
    def type_card_rebate(self):
        try:
            self.wait_element_load_end(CCPageLocators.CARDREBATE)
            logging.info(CCLogInfo.TYPECARDREBATE % rebate_data)
            self.find_element(CCPageLocators.CARDREBATE).send_keys(rebate_data)
        except NoSuchElementException:
            logging.error(CCLogInfo.CARDREBATENOTFOUND)
        except Exception as e:
            raise e

    # 卡券中心 - 选择折扣券有效期为领取后生效
    def select_validity_to_immediately(self):
        try:
            self.wait_element_load_end(CCPageLocators.CARDVALIDITY)
            time.sleep(1)
            logging.info(CCLogInfo.CHOOSEIMMEDIATE)
            self.find_element(CCPageLocators.CARDVALIDITY).click()
        except NoSuchElementException:
            logging.error(CCLogInfo.CCVNOTFOUND)
        except Exception as e:
            raise e

    # 卡券中心 - 点击适用商品上传图片按钮
    def click_suite_goods_button(self):
        try:
            self.wait_element_load_end(CCPageLocators.SUITEGOODSUPLOADBUTTON)
            self.find_element(CCPageLocators.SUITEGOODSUPLOADBUTTON).click()
        except NoSuchElementException:
            logging.error("没找到上传适用商品的按钮")
        except Exception as e:
            raise e

    # 卡券中心 - 上传适用商品图片
    def upload_suite_goods_pic(self):
        try:
            self.click_suite_goods_button()
            logging.info("正在上传适用商品图：%s" % big_image_name)
            self.upload_image(CCPageLocators.FILEIMAGE,
                              CCPageLocators.FILEIMAGELOCATE, big_image_name)
            self.click_confirm_button(CCPageLocators.SUITEGOODSUPLOADCONFIRM)
            logging.info("上传适用商品图完毕")
        except Exception as e:
            raise e

    # 卡券中心 - 输入商品简介
    def type_goods_summary(self):

        try:
            self.wait_element_load_end(CCPageLocators.GOODSSUMMARY)
            logging.info("输入商品简介：%s" % inventory_data)
            self.find_element(CCPageLocators.GOODSSUMMARY).send_keys(goods_summary)
        except NoSuchElementException:
            logging.error("没找到商品简介的元素位置")
        except Exception as e:
            raise e

    # 卡券中心 - 输入优惠券的库存
    def type_card_inventory(self):
        try:
            self.wait_element_load_end(CCPageLocators.CARDINVENTORY)
            logging.info("输入卡券库存：%s" % inventory_data)
            self.find_element(CCPageLocators.CARDINVENTORY).send_keys(inventory_data)
        except NoSuchElementException:
            logging.error("没找到优惠券库存的元素位置")
        except Exception as e:
            raise e

    def click_create_card_save_button(self, ele):
        try:
            self.wait_element_load_end(ele)
            self.find_element(ele).click()
            if self.find_element(CCPageLocators.TITLEFAULTTIP).text == '卡券名称已存在!':
                logging.error('卡券名称已存在，请使用一个新的卡券名称')
        except Exception as e:
            raise e

    # 卡券中心 - 创建折扣券
    def create_rebate_card(self):
        self.upload_big_pic(CCPageLocators.BIGPIC, CCPageLocators.FILEIMAGE,
                            CCPageLocators.FILEIMAGELOCATE, CCPageLocators.CONFIRM)
        self.upload_small_pic(CCPageLocators.SMALLPIC, CCPageLocators.FILEIMAGE,
                              CCPageLocators.FILEIMAGELOCATE, CCPageLocators.CONFIRM)
        self.type_card_name()
        self.type_card_rebate()
        self.select_validity_to_immediately()
        self.upload_suite_goods_pic()
        self.type_goods_summary()
        self.type_card_inventory()
        self.click_create_card_save_button(CCPageLocators.SAVE)
        time.sleep(1)
        self.handle_alert()


class PictureManageAction(BasePage):
    """
    Name        :  运营 -> 套图管理
    Author      :  刘建民
    Create Date :  2016/08/23
    """

    # 套图管理 - 点击套图管理的新建分类按钮
    def click_create_picture_classify_button(self):
        try:
            self.wait_element_load_end(PMPageLocators.CREATEPICTURECLASSIFY)
            self.find_element(PMPageLocators.CREATEPICTURECLASSIFY).click()
        except NoSuchElementException:
            logging.error("找不到新建分类按钮")
        except Exception as e:
            raise e

    # 套图管理 - 输入套图的分类名称
    def type_classify_name(self):
        try:
            self.wait_element_load_end(PMPageLocators.CLASSIFYNAME)
            logging.info("输入套图分类名称：%s" % picture_classify_name)
            self.find_element(PMPageLocators.CLASSIFYNAME).send_keys(picture_classify_name)
        except NoSuchElementException:
            logging.error("找不到套图分类名称输入框，输入失败")
        except Exception as e:
            raise e

    # 套图管理 - 选择套图分类的颜色标识
    def select_classify_color_type(self):
        try:
            self.wait_element_load_end(PMPageLocators.COLORTYPE)
            logging.info("选择分类的颜色标识：绿色")
            self.find_element(PMPageLocators.COLORTYPE).click()
        except NoSuchElementException:
            logging.error("找不到套图分类颜色标识")
        except Exception as e:
            raise e

    # 套图管理 - 创建套图分类完毕后点击保存
    def click_pickit_classify_save_button(self):
        try:
            self.wait_element_load_end(PMPageLocators.SAVEPICTURECLASSIFY)
            self.find_element(PMPageLocators.SAVEPICTURECLASSIFY).click()
        except NoSuchElementException:
            logging.error("找不到保存按钮")
        except Exception as e:
            raise e

    # 套图管理 - 创建套图分类
    def create_pickit_classify(self):
        self.click_create_picture_classify_button()
        self.type_classify_name()
        self.upload_big_pic(PMPageLocators.BIGPIC, PMPageLocators.FILEIMAGE,
                            PMPageLocators.FILEIMAGELOCATE, PMPageLocators.CONFIRM)
        self.upload_small_pic(PMPageLocators.SMALLPIC, PMPageLocators.FILEIMAGE,
                              PMPageLocators.FILEIMAGELOCATE, PMPageLocators.CONFIRM)
        self.select_classify_color_type()
        self.click_pickit_classify_save_button()
        time.sleep(2)
        self.handle_alert()

    # 套图管理 - 输入套图的名称
    def type_pickit_name(self):
        try:
            self.wait_element_load_end(PMPageLocators.PICTURETITLE)
            logging.info("输入套图的名称：%s" % picture_name)
            self.find_element(PMPageLocators.PICTURETITLE).send_keys(picture_name)
        except NoSuchElementException:
            logging.error("找不到套图名称输入框位置")
        except Exception as e:
            raise e

    # 套图管理 - 选择套图的所属分类
    def select_picture_classify(self):
        try:
            self.wait_element_load_end(PMPageLocators.PICTUREBELONGDROP)
            self.find_element(PMPageLocators.PICTUREBELONGDROP).click()
            logging.info("选择套图的所属分类：%s" % self.find_element(PMPageLocators.PICTUREBELONG).text)
            self.find_element(PMPageLocators.PICTUREBELONG).click()
        except NoSuchElementException:
            logging.error("找不到套图分类下拉框位置")
        except Exception as e:
            raise e

    # 套图管理 - 输入套图介绍
    def type_pickit_description(self):
        try:
            self.wait_element_load_end(PMPageLocators.PICTUREDESCRIPTION)
            logging.info("输入套图介绍：%s" % pickit_description)
            self.find_element(PMPageLocators.PICTUREDESCRIPTION).send_keys(pickit_description)
        except NoSuchElementException:
            logging.error("找不到套图介绍输入框位置")
        except Exception as e:
            raise e

    # 套图管理 - 点击上传套图按钮
    def click_add_pickit_pic(self):
        try:
            self.wait_element_load_end(PMPageLocators.ADDPITCURE)
            self.find_element(PMPageLocators.ADDPITCURE).click()
        except NoSuchElementException:
            logging.error("找不到上传套图按钮位置")
        except Exception as e:
            raise e

    # 套图管理 - 上传套图
    def upload_pickit_pic(self):
        try:
            self.click_add_pickit_pic()
            logging.info("正在上传第一张套图：%s" % pickit1)
            self.upload_image(PMPageLocators.UPLOADPICTURE,
                              PMPageLocators.UPLOADPICTURELOACTE, big_image_name)
            self.click_save_button(PMPageLocators.PICTURECONFIRM)
            logging.info("上传套图完毕")
        except Exception as e:
            raise e

    # 套图管理 - 创建套图
    def create_pickit(self):
        self.type_pickit_name()
        self.select_picture_classify()
        self.upload_big_pic(PMPageLocators.BIGPIC, PMPageLocators.FILEIMAGE,
                            PMPageLocators.FILEIMAGELOCATE, PMPageLocators.CONFIRM)
        self.upload_small_pic(PMPageLocators.SMALLPIC, PMPageLocators.FILEIMAGE,
                              PMPageLocators.FILEIMAGELOCATE, PMPageLocators.CONFIRM)
        self.type_pickit_description()
        self.upload_pickit_pic()
        self.click_save_button(PMPageLocators.PICTURESAVE)
        time.sleep(1)
        self.handle_alert()


class MicroHelpPageAction(BasePage):
    """
    Name        :  运营 -> 微助力
    Author      :  刘建民
    Create Date :  2016/08/23
    """

    # 微助力 - 输入微助力活动名称
    def type_activity_name(self):
        try:
            self.wait_element_load_end(MHPageLocators.EVENTNAME)
            logging.info(MHLogInfo.TYPENAME % activity_name)
            self.find_element(MHPageLocators.EVENTNAME).send_keys(activity_name)
        except NoSuchElementException:
            logging.error(MHLogInfo.NAMEFIELDNOTFOUND)
        except Exception as e:
            raise e

    # 微助力 - 输入微助力活动开始时间
    def type_mh_start_time(self):
        date = time.strftime("%Y-%m-%d %H:%M:%S")
        try:
            self.wait_element_load_end(MHPageLocators.TYPESTARTDATE)
            self.driver.execute_script(remove_sd_read_only)
            self.find_element(MHPageLocators.TYPESTARTDATE).send_keys(date)
        except NoSuchElementException:
            logging.error(MHLogInfo.STARTDATENOTFOUND)
        except Exception as e:
            raise e

    # 微助力 - 输入微助力活动结束时间
    def type_mh_end_time(self):
        now_time = datetime.datetime.now()
        fur_time = now_time + datetime.timedelta(days=3)
        date = fur_time.strftime("%Y-%m-%d %H:%M:%S")
        try:
            self.wait_element_load_end(MHPageLocators.TYPEENDDATE)
            self.driver.execute_script(remove_ed_read_only)
            self.find_element(MHPageLocators.TYPEENDDATE).send_keys(date)
        except NoSuchElementException:
            logging.error(MHLogInfo.ENDDATENOTFOUND)
        except Exception as e:
            raise e

    # 微助力 - 上传微助力背景图
    def upload_mh_background_pic(self):
        try:
            self.click_upload_button(MHPageLocators.BACKGROUNDBUTTON, MHLogInfo.MHBACKGROUNDERROR)
            logging.info(MHLogInfo.UPLOADINGBGPIC % big_image_name)
            self.upload_image(MHPageLocators.DOC, MHPageLocators.DOCLOCATE, big_image_name)
            self.click_confirm_button(MHPageLocators.BACKGROUNDCONFIRM)
            logging.info(MHLogInfo.UPLOADBGPICFIN)
        except Exception as e:
            raise e

    # 微助力 - 输入微助力分享标题
    def type_share_title(self):
        try:
            self.wait_element_load_end(MHPageLocators.SHARETITLE)
            logging.info(MHLogInfo.TYPESHARETITLE % share_title)
            self.find_element(MHPageLocators.SHARETITLE).send_keys(share_title)
        except NoSuchElementException:
            logging.error(MHLogInfo.SHARETITLENOTFOUND)
        except Exception as e:
            raise e

    # 微助力 - 输入分享描述
    def type_share_description(self):
        try:
            self.wait_element_load_end(MHPageLocators.SHAREDESCRIPTION)
            logging.info(MHLogInfo.TYPESHAREDESC % share_description)
            self.find_element(MHPageLocators.SHAREDESCRIPTION).send_keys(share_description)
        except NoSuchElementException:
            logging.error(MHLogInfo.SHAREDESCNOTFOUND)
        except Exception as e:
            raise e

    # 微助力 - 输入活动详情
    def type_event_description(self):
        try:
            self.driver.switch_to_frame(MHPageLocators.IFRAME)
            self.wait_element_load_end(MHPageLocators.EVENTMAINBODY)
            self.find_element(MHPageLocators.EVENTMAINBODY).send_keys(event_description)
            self.driver.switch_to_default_content()
        except NoSuchElementException:
            logging.error(MHLogInfo.EVENTDESC)
        except Exception as e:
            raise e

    # 微助力 - 输入好友集满数量
    def type_friend_collect_number(self):
        try:
            self.wait_element_load_end(MHPageLocators.FRIENDCOLLECTNUM)
            logging.info(MHLogInfo.FRIENDCOLLECTNUM % friend_collect_number)
            self.find_element(MHPageLocators.FRIENDCOLLECTNUM).send_keys(friend_collect_number)
        except NoSuchElementException:
            logging.error(MHLogInfo.FCNOTFOUND)
        except Exception as e:
            raise e

    # 微助力 - 输入好友集满数量的单位
    def type_friend_collect_unit(self):
        try:
            self.wait_element_load_end(MHPageLocators.UNIT)
            logging.info(MHLogInfo.TYPEUNIT % unit)
            self.find_element(MHPageLocators.UNIT).send_keys(unit)
        except NoSuchElementException:
            logging.error(MHLogInfo.UNITNOTFOUND)
        except Exception as e:
            raise e

    # 微助力 - 输入好友有效助力概率
    def type_friend_valid_chance(self):
        try:
            self.wait_element_load_end(MHPageLocators.VALIDCHANCE)
            logging.info(MHLogInfo.TYPEVALIDCHANCE % friend_valid_chance)
            self.find_element(MHPageLocators.VALIDCHANCE).send_keys(friend_valid_chance)
        except NoSuchElementException:
            logging.error(MHLogInfo.VCNOTFOUND)
        except Exception as e:
            raise e

    # 微助力 - 输入数量设置
    def type_number_config(self):
        try:
            self.wait_element_load_end(MHPageLocators.NUMBERCONFIG)
            logging.info(MHLogInfo.TYPENUMCONFIG % number_config)
            self.find_element(MHPageLocators.NUMBERCONFIG).send_keys(number_config)
        except NoSuchElementException:
            logging.error(MHLogInfo.NCNOTFOUND)
        except Exception as e:
            raise e

    # 微助力 - 点击添加奖品
    def click_add_prize(self):
        try:
            self.wait_element_load_end(MHPageLocators.ADDPRIZEBUTTON)
            logging.info(MHLogInfo.ADDPRIZE)
            self.find_element(MHPageLocators.ADDPRIZEBUTTON).click()
        except NoSuchElementException:
            logging.error(MHLogInfo.APNOTFOUND)
        except Exception as e:
            raise e

    # 微助力 - 选择奖品
    def select_prize(self):
        self.click_add_prize()
        self.wait_element_load_end(MHPageLocators.PRIZENAME)
        self.find_element(MHPageLocators.PRIZENAME).click()
        # 在下拉框的前十个option里面挑选奖品
        option_num = 10
        try:
            for i in range(option_num):
                select = (By.XPATH, MHPageLocators.SELECT % i)
                self.find_element(select).click()
                # 如果挑选的奖品库存大于0，才会选择
                if int(self.find_element(MHPageLocators.PRIZENUMBER).get_attribute("value")) > 0:
                    self.find_element(MHPageLocators.PRIZENUMBER).clear()
                    self.find_element(MHPageLocators.PRIZENUMBER).send_keys(prize_number)
                    self.click_confirm_button(MHPageLocators.PRIZECONFIRM)
                    break
        except NoSuchElementException:
            logging.error(MHLogInfo.PRIZENOTFOUND)
        except Exception as e:
            raise e

    # 微助力 - 创建一个微助力活动 - 模板一
    def create_micro_help(self):
        self.type_activity_name()
        self.upload_big_pic(MHPageLocators.BIGPIC, MHPageLocators.DOC,
                            MHPageLocators.DOCLOCATE, MHPageLocators.CONFIRM)
        time.sleep(1)
        self.upload_small_pic(MHPageLocators.SMALLPIC, MHPageLocators.DOC,
                              MHPageLocators.DOCLOCATE, MHPageLocators.CONFIRM)
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
        self.click_save_button(MHPageLocators.SAVE)
        time.sleep(1)
        self.handle_alert()
