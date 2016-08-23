# -*- coding: UTF-8 -*-


"""
Author       :  刘建民
Create Date  :  2016/7/1
"""


from selenium.webdriver.common.by import By


class CardCenterPageElements:
    OPERATIONTABELE = (By.CSS_SELECTOR, "#current3")
    card_center_ele = (By.XPATH, ".//*[@id='sidebar']/ul/li[5]/a/span[2]")
    big_pic_ele = (By.ID, "ccPicBigImg")
    small_pic_ele = (By.ID, "ccPicSmallImg")
    card_name_ele = (By.CSS_SELECTOR, "#coupon_name")
    card_rebate_ele = (By.CSS_SELECTOR, "#ccRebateId")
    card_validity_ele = (By.XPATH, ".//*[@id='ccSetForm']/div/div[8]/div/div[1]/label/input")
    card_inventory_ele = (By.CSS_SELECTOR, "#ccInventory")
    card_save_ele = (By.CSS_SELECTOR, ".btn-default.large-btn")
    # 上传图片的元素位置
    upload_button_ele = (By.CSS_SELECTOR, ".file-btn")
    # 上传图片的确认按钮
    confirm_ele = (By.ID, "ccPicBigImgDia_btn1")

    # 运营模块--套图管理元素定位
    create_pickit_classify_ele = (By.XPATH, ".//*[@id='content_body']/tbody/tr/td[1]/button")
    classify_name_ele = (By.ID, "pmName")
    color_type_ele = (By.XPATH, ".//*[@id='color_type']/li[1]")
    classify_save_ele = (By.ID, "button")
    new_create_pickit_classify_ele = (By.XPATH, ".//*[@class='cm_type active']/dl/dd[1]")

    pickit_title_ele = (By.ID, "pmTitle")
    pickit_belong_classify_drop_ele = (By.ID, "pmCgSysuuid")
    pickit_belong_classify_ele = (By.XPATH, ".//*[@id='pmCgSysuuid']/option[2]")
    pickit_description_ele = (By.ID, "pmDesc")
    add_pickit_ele = (By.ID, "img_add_btn")
    new_create_pickit_ele = (By.XPATH, ".//*[@id='tableData']/tbody/tr/td[1]")
    pickit_smallpic_ele = (By.XPATH, ".//*[@id='setting']/form/div[1]/table/tbody/tr[3]/td/div/div[2]/div[1]")
    add_pickit_window_ele = (By.XPATH, ".//*[@id='checkOneImg']/div[2]")
    micro_bigpic_ele = (By.ID, "BgiImgUrl")
    micro_smallpic_ele = (By.ID, "ImgSmallUrl")
    pickit_save_ele = (By.XPATH, ".//*[@id='setting']/form/div[2]/table/tbody/tr[4]/td/div/input")
    micro_confirm_ele = (By.XPATH, ".//*[@id='upImgs']/div/div/div[5]/button[2]")
    mh_background_button_ele = (By.ID, "raBackgroundImgUrl")
    mh_save_ele = (By.ID, "saveRacBtn")
    file_image_ele = (By.ID, "fileImage")
    file_image_ele_locate = "fileImage"
    doc_ele = (By.ID, "doc")
    doc_ele_locate = 'doc'