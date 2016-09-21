# -*- coding: UTF-8 -*-

"""
Author       :  Ken-Kei
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
    Author      :  Ken-Kei
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
            logging.info(CCLogInfo.TYPECARDNAME % card_name)
            self.type(CCPageLocators.CARDNAME, card_name)
            self.driver.switch_to_active_element().send_keys(Keys.TAB)
            time.sleep(1)
            if self.find_element(CCPageLocators.TITLEFAULTTIP).text == '卡券名称已存在!':
                logging.error(CCLogInfo.CARDNAMEEXIST)
                self.create_screen_shot(card_name_exist_screenshot, tc_name=test_CreateCard)
                raise ValueError(CCLogInfo.CARDNAMEEXIST)
        except NoSuchElementException:
            logging.error(CCLogInfo.CARDNAMENOTFOUND)
        except Exception as e:
            raise e

    # 卡券中心 - 输入折扣券的折扣率
    def type_card_rebate(self):
        try:
            logging.info(CCLogInfo.TYPECARDREBATE % rebate_data)
            self.type(CCPageLocators.CARDREBATE, rebate_data)
        except NoSuchElementException:
            logging.error(CCLogInfo.CARDREBATENOTFOUND)
        except Exception as e:
            raise e

    # 卡券中心 - 选择折扣券有效期为领取后生效
    def select_validity_to_immediately(self):
        try:
            logging.info(CCLogInfo.CHOOSEIMMEDIATE)
            self.click(CCPageLocators.CARDVALIDITY)
        except NoSuchElementException:
            logging.error(CCLogInfo.CCVNOTFOUND)
        except Exception as e:
            raise e

    # 卡券中心 - 点击适用商品上传图片按钮
    def click_suite_goods_button(self):
        try:
            self.click(CCPageLocators.SUITEGOODSUPLOADBUTTON)
        except NoSuchElementException:
            logging.error(CCLogInfo.SUITENOTFOUND)
        except Exception as e:
            raise e

    # 卡券中心 - 上传适用商品图片
    def upload_suite_goods_pic(self):
        logging.info(CCLogInfo.UPLOADINGSUITEPIC % big_image_name)
        self.click_suite_goods_button()
        self.upload_image(CCPageLocators.FILEIMAGE,
                          CCPageLocators.FILEIMAGELOCATE, big_image_name)
        self.click_confirm_button(CCPageLocators.SUITEGOODSUPLOADCONFIRM)
        logging.info(CCLogInfo.UPLOADSUITEPICFIN)

    # 卡券中心 - 输入商品简介
    def type_goods_summary(self):
        try:
            logging.info(CCLogInfo.TYPEGOODSUMMARY % inventory_data)
            self.type(CCPageLocators.GOODSSUMMARY, goods_summary)
        except NoSuchElementException:
            logging.error(CCLogInfo.GSNOTFOUND)
        except Exception as e:
            raise e

    # 卡券中心 - 输入优惠券的库存
    def type_card_inventory(self):
        try:
            logging.info(CCLogInfo.TYPECARDINVENT % inventory_data)
            self.type(CCPageLocators.CARDINVENTORY, inventory_data)
        except NoSuchElementException:
            logging.error(CCLogInfo.CARDINVENTNOTFOUND)
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
        self.click_save_button(CCPageLocators.SAVE)
        self.handle_alert()


class PictureManageAction(BasePage):
    """
    Name        :  运营 -> 套图管理
    Author      :  Ken-Kei
    Create Date :  2016/08/23
    """

    # 套图管理 - 新建套图分类 - 点击套图管理的新建分类按钮
    def click_create_picture_classify_button(self):
        try:
            self.click(PMPageLocators.CREATEPICTURECLASSIFY)
        except NoSuchElementException:
            logging.error(PMLogInfo.PCBUTTONNOTFOUND)
        except Exception as e:
            raise e

    # 套图管理 - 新建套图分类 - 输入套图的分类名称
    def type_classify_name(self):
        try:
            logging.info(PMLogInfo.TYPECLASSNAME % picture_classify_name)
            self.type(PMPageLocators.CLASSIFYNAME, picture_classify_name)
        except NoSuchElementException:
            logging.error(PMLogInfo.CLASSNAMEFIELDNOTFOUND)
        except Exception as e:
            raise e

    # 套图管理 - 新建套图分类 - 选择套图分类的颜色标识
    def select_classify_color_type(self):
        try:
            logging.info(PMLogInfo.COLORFIELD)
            self.click(PMPageLocators.COLORTYPE)
        except NoSuchElementException:
            logging.error(PMLogInfo.COLORFIELDNOTFOUND)
        except Exception as e:
            raise e

    # 套图管理 - 新建套图分类 - 创建套图分类
    def create_pickit_classify(self):
        self.click_create_picture_classify_button()
        self.type_classify_name()
        self.upload_big_pic(PMPageLocators.BIGPIC, PMPageLocators.FILEIMAGE,
                            PMPageLocators.FILEIMAGELOCATE, PMPageLocators.CONFIRM)
        self.upload_small_pic(PMPageLocators.SMALLPIC, PMPageLocators.FILEIMAGE,
                              PMPageLocators.FILEIMAGELOCATE, PMPageLocators.CONFIRM)
        self.select_classify_color_type()
        self.click_save_button(PMPageLocators.SAVEPICTURECLASSIFY)
        self.handle_alert()

    # 套图管理 - 新建套图 - 输入套图的名称
    def type_pickit_name(self):
        try:
            logging.info(PMLogInfo.TYPEPICNAME % picture_name)
            self.type(PMPageLocators.PICTURETITLE, picture_name)
        except NoSuchElementException:
            logging.error(PMLogInfo.PICNAMEFIELDNOTFOUND)
        except Exception as e:
            raise e

    # 套图管理 - 新建套图 - 选择套图的所属分类
    def select_picture_classify(self):
        try:
            # 点击所属分类的下拉框
            self.click(PMPageLocators.PICTUREBELONGDROP)
            logging.info(PMLogInfo.SELECTCLASSBELONG % self.find_element(PMPageLocators.PICTUREBELONG).text)
            self.click(PMPageLocators.PICTUREBELONG)
        except NoSuchElementException:
            logging.error(PMLogInfo.CBDROPDOWNNOTFOUND)
        except Exception as e:
            raise e

    # 套图管理 - 新建套图 - 输入套图介绍
    def type_pickit_description(self):
        try:
            logging.info(PMLogInfo.TYPEPICDESC % pickit_description)
            self.type(PMPageLocators.PICTUREDESCRIPTION, pickit_description)
        except NoSuchElementException:
            logging.error(PMLogInfo.PICDESCFIELDNOTFOUND)
        except Exception as e:
            raise e

    # 套图管理 - 新建套图 - 上传套图
    def upload_pickit_pic(self):
        # 点击上传套图的按钮
        self.click_upload_button(PMPageLocators.ADDPITCURE)
        logging.info(PMLogInfo.UPLOADFIRSTPIC % pickit1)
        self.upload_image(PMPageLocators.UPLOADPICTURE,
                          PMPageLocators.UPLOADPICTURELOACTE, big_image_name)
        self.click_save_button(PMPageLocators.PICTURECONFIRM)
        logging.info(PMLogInfo.PICUPLOADFIN)

    # 套图管理 - 新建套图 - 创建套图
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
        self.handle_alert()


class MicroHelpPageAction(BasePage):
    """
    Name        :  运营 -> 微助力
    Author      :  Ken-Kei
    Create Date :  2016/08/23
    """

    # 微助力 - 输入微助力活动名称
    def type_activity_name(self):
        try:
            logging.info(MHLogInfo.TYPENAME % activity_name)
            self.type(MHPageLocators.EVENTNAME, activity_name)
        except NoSuchElementException:
            logging.error(MHLogInfo.NAMEFIELDNOTFOUND)
        except Exception as e:
            raise e

    # 微助力 - 输入微助力活动开始时间
    def type_mh_start_time(self):
        date = time.strftime("%Y-%m-%d %H:%M:%S")
        try:
            logging.info(MHLogInfo.TYPESTARTTIME % date)
            self.driver.execute_script(remove_sd_read_only)
            self.type(MHPageLocators.TYPESTARTDATE, date)
        except NoSuchElementException:
            logging.error(MHLogInfo.STARTDATENOTFOUND)
        except Exception as e:
            raise e

    # 微助力 - 输入微助力活动结束时间
    def type_mh_end_time(self):
        now_time = datetime.datetime.now()
        # 设定活动的结束时间为开始时间的3天后
        fur_time = now_time + datetime.timedelta(days=3)
        date = fur_time.strftime("%Y-%m-%d %H:%M:%S")
        try:
            logging.info(MHLogInfo.TYPEENDTIME % date)
            self.driver.execute_script(remove_ed_read_only)
            self.type(MHPageLocators.TYPEENDDATE, date)
        except NoSuchElementException:
            logging.error(MHLogInfo.ENDDATENOTFOUND)
        except Exception as e:
            raise e

    # 微助力 - 上传微助力背景图
    def upload_mh_background_pic(self):
        logging.info(MHLogInfo.UPLOADINGBGPIC % big_image_name)
        self.click_upload_button(MHPageLocators.BACKGROUNDBUTTON)
        self.upload_image(MHPageLocators.DOC, MHPageLocators.DOCLOCATE, big_image_name)
        self.click_confirm_button(MHPageLocators.BACKGROUNDCONFIRM)
        logging.info(MHLogInfo.UPLOADBGPICFIN)

    # 微助力 - 输入微助力分享标题
    def type_share_title(self):
        try:
            logging.info(MHLogInfo.TYPESHARETITLE % share_title)
            self.type(MHPageLocators.SHARETITLE, share_title)
        except NoSuchElementException:
            logging.error(MHLogInfo.SHARETITLENOTFOUND)
        except Exception as e:
            raise e

    # 微助力 - 输入分享描述
    def type_share_description(self):
        try:
            logging.info(MHLogInfo.TYPESHAREDESC % share_description)
            self.type(MHPageLocators.SHAREDESCRIPTION, share_description)
        except NoSuchElementException:
            logging.error(MHLogInfo.SHAREDESCNOTFOUND)
        except Exception as e:
            raise e

    # 微助力 - 输入活动详情
    def type_event_description(self):
        try:
            logging.info(MHLogInfo.TYPEEVENTDESC % event_description)
            self.type_in_iframe(MHPageLocators.IFRAME, MHPageLocators.EVENTMAINBODY, event_description)
        except NoSuchElementException:
            logging.error(MHLogInfo.EVENTDESC)
        except Exception as e:
            raise e

    # 微助力 - 输入好友集满数量
    def type_friend_collect_number(self):
        try:
            logging.info(MHLogInfo.FRIENDCOLLECTNUM % friend_collect_number)
            self.type(MHPageLocators.FRIENDCOLLECTNUM, friend_collect_number)
        except NoSuchElementException:
            logging.error(MHLogInfo.FCNOTFOUND)
        except Exception as e:
            raise e

    # 微助力 - 输入好友集满数量的单位
    def type_friend_collect_unit(self):
        try:
            logging.info(MHLogInfo.TYPEUNIT % unit)
            self.type(MHPageLocators.UNIT, unit)
        except NoSuchElementException:
            logging.error(MHLogInfo.UNITNOTFOUND)
        except Exception as e:
            raise e

    # 微助力 - 输入好友有效助力概率
    def type_friend_valid_chance(self):
        try:
            logging.info(MHLogInfo.TYPEVALIDCHANCE % friend_valid_chance)
            self.type(MHPageLocators.VALIDCHANCE, friend_valid_chance)
        except NoSuchElementException:
            logging.error(MHLogInfo.VCNOTFOUND)
        except Exception as e:
            raise e

    # 微助力 - 输入数量设置
    def type_number_config(self):
        try:
            logging.info(MHLogInfo.TYPENUMCONFIG % number_config)
            self.type(MHPageLocators.NUMBERCONFIG, number_config)
        except NoSuchElementException:
            logging.error(MHLogInfo.NCNOTFOUND)
        except Exception as e:
            raise e

    # 微助力 - 点击添加奖品
    def click_add_prize(self):
        try:
            logging.info(MHLogInfo.ADDPRIZE)
            self.click(MHPageLocators.ADDPRIZEBUTTON)
        except NoSuchElementException:
            logging.error(MHLogInfo.APNOTFOUND)
        except Exception as e:
            raise e

    # 微助力 - 选择奖品
    def select_prize(self):
        self.click_add_prize()
        # 选择奖品类型为折扣券
        self.click(MHPageLocators.PRIZENAME)
        # 在下拉框的前十个option里面挑选奖品
        option_num = 11
        try:
            for i in range(1, option_num):
                select = (By.XPATH, MHPageLocators.SELECT % i)
                self.click(select)
                # 如果挑选的奖品库存大于0，才会选择
                if int(self.find_element(MHPageLocators.PRIZENUMBER).get_attribute("value")) > 0:
                    logging.info(MHLogInfo.SELECTPRIZE % self.find_element(select).text)
                    self.type(MHPageLocators.PRIZENUMBER, prize_number)
                    logging.info(MHLogInfo.TYPEPRIZENUMBER % prize_number)
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
        self.handle_alert()


class ChannalQRCodePageAction(BasePage):
    """
    Name        :  运营 -> 渠道二维码
    Author      :  Ken-Kei
    Create Date :  2016/09/20
    """

    # 渠道二维码 - 点击新建二维码按钮
    def click_create_code_button(self):
        try:
            logging.info(CQLogInfo.CREATINGQRCODE)
            self.click(CQPageLocators.CREATEQRCODE)
        except NoSuchElementException:
            logging.error(CQLogInfo.CREATEBUTTONNOTFOUND)
        except Exception as e:
            raise e

    # 渠道二维码 - 点击二维码的类型的下拉框
    def click_code_type_drop(self):
        try:
            logging.info(CQLogInfo.SELECTINGCODETYPE)
            self.click(CQPageLocators.QRCODEDROP)
        except NoSuchElementException:
            logging.error(CQLogInfo.CODEDROPNOTFOUND)
        except Exception as e:
            raise e

    # 渠道二维码 - 选择二维码的类型
    def select_code_type(self, code_type=None):
        self.click_code_type_drop()
        try:
            # 渠道二维码的类型，1为临时二维码，2为永久二维码
            if code_type == 1:
                logging.info(CQLogInfo.SELECTCODETYPE % self.find_element(CQPageLocators.QRCODETYPETEMP).text)
                self.click(CQPageLocators.QRCODETYPETEMP)
            elif code_type == 2:
                logging.info(CQLogInfo.SELECTCODETYPE % self.find_element(CQPageLocators.QRCODETYPEFOREVER).text)
                self.click(CQPageLocators.QRCODETYPEFOREVER)
            else:
                logging.error(CQLogInfo.QRCODETYPENOTLEGAL)
                raise ValueError(CQLogInfo.QRCODETYPENOTLEGAL)
        except NoSuchElementException:
            logging.error(CQLogInfo.TEMPCODENOTFOUND)
        except Exception as e:
            raise e

    # 渠道二维码 - 输入二维码的名称
    def type_code_name(self, code_type=None):
        try:
            if code_type == 1:
                logging.info(CQLogInfo.TYPEQRCODENAME % qrcode_temp_name)
                self.type(CQPageLocators.QRCODENAME, qrcode_temp_name)
            if code_type == 2:
                logging.info(CQLogInfo.TYPEQRCODENAME % qrcode_forever_name)
                self.type(CQPageLocators.QRCODENAME, qrcode_forever_name)
        except NoSuchElementException:
            logging.error(CQLogInfo.QRCODENAMENOTFOUND)
        except Exception as e:
            raise e

    # 点击渠道二维码列表
    def click_qrcode_list(self):
        try:
            time.sleep(1)
            self.click(CQPageLocators.QRCODELIST)
        except NoSuchElementException:
            logging.error(CQLogInfo.QRCODELISTNOTFOUND)
        except Exception as e:
            raise e

    def create_qrcode(self):
        # 如果二维码类型为3，即创建两种类型的二维码
        if qrcode_type == 3:
            for i in range(1, qrcode_type):
                self.click_create_code_button()
                self.select_code_type(code_type=i)
                self.type_code_name(code_type=i)
                self.click_save_button(CQPageLocators.QRCODESAVE)
                time.sleep(2)
        else:
            self.click_create_code_button()
            self.select_code_type(code_type=qrcode_type)
            self.type_code_name(code_type=qrcode_type)
            self.click_save_button(CQPageLocators.QRCODESAVE)
