# -*- coding: UTF-8 -*-


"""
Author       :  刘建民
Create Date  :  2016/08/23
"""


from selenium.webdriver.common.by import By


class CCPageLocators:
    """
    Name         :  运营 - 卡券中心 - 元素定位
    Author       :  刘建民
    Create Date  :  2016/08/23
    """

    OPERATIONTAB                = (By.CSS_SELECTOR, "#current3")
    CARDCENTER                  = (By.XPATH, ".//*[@id='sidebar']/ul/li[5]/a/span[2]")
    BIGPIC                      = (By.ID, "ccPicBigImg")
    SMALLPIC                    = (By.ID, "ccPicSmallImg")
    CARDNAME                    = (By.CSS_SELECTOR, "#coupon_name")
    CARDREBATE                  = (By.CSS_SELECTOR, "#ccRebateId")
    CARDVALIDITY                = (By.XPATH, ".//*[@id='ccSetForm']/div/div[8]/div/div[1]/label/input")
    CARDINVENTORY               = (By.CSS_SELECTOR, "#ccInventory")
    SAVE                        = (By.CSS_SELECTOR, ".btn-default.large-btn")
    CARDUPLOADBUTTON            = (By.CSS_SELECTOR, ".file-btn")
    CONFIRM                     = (By.ID, "ccPicBigImgDia_btn1")
    SUITEGOODSUPLOADBUTTON      = (By.ID, 'ccProductImageImg')
    SUITEGOODSUPLOADCONFIRM     = (By.ID, "ccPicBigImgDia_btn1")
    FILEIMAGE                   = (By.ID, "fileImage")
    FILEIMAGELOCATE             = "fileImage"
    GOODSSUMMARY                = (By.ID, "ccProductInfo")
    NEWCARD                     = (By.XPATH, ".//*[@id='setting']/table/tbody/tr[1]/td[1]")


class PMPageLocators:
    """
    Name         :  运营 - 套图管理 - 元素定位
    Author       :  刘建民
    Create Date  :  2016/08/23
    """

    CREATEPICTURECLASSIFY       = (By.XPATH, ".//*[@id='content_body']/tbody/tr/td[1]/button")
    CLASSIFYNAME                = (By.ID, "pmName")
    COLORTYPE                   = (By.XPATH, ".//*[@id='color_type']/li[1]")
    SAVEPICTURECLASSIFY         = (By.ID, "button")
    NEWPICTURECLASSIFY          = (By.XPATH, ".//*[@class='cm_type active']/dl/dd[1]")
    PICTURETITLE                = (By.ID, "pmTitle")
    PICTUREBELONGDROP           = (By.ID, "pmCgSysuuid")
    PICTUREBELONG               = (By.XPATH, ".//*[@id='pmCgSysuuid']/option[2]")
    PICTUREDESCRIPTION          = (By.ID, "pmDesc")
    ADDPITCURE                  = (By.ID, "img_add_btn")
    NEWPICTURE                  = (By.XPATH, ".//*[@id='tableData']/tbody/tr/td[1]")
    PICTURESMALLPIC             = (By.XPATH, ".//*[@id='setting']/form/div[1]/table/tbody/tr[3]/td/div/div[2]/div[1]")
    PICTURESAVE                 = (By.XPATH, ".//*[@id='setting']/form/div[2]/table/tbody/tr[4]/td/div/input")
    BIGPIC                      = (By.ID, "ccPicBigImg")
    SMALLPIC                    = (By.ID, "ccPicSmallImg")
    FILEIMAGE                   = (By.ID, "fileImage")
    FILEIMAGELOCATE             = "fileImage"
    CONFIRM                     = (By.ID, "ccPicBigImgDia_btn1")
    UPLOADPICTURE               = (By.ID, "fileOneImage")
    UPLOADPICTURELOACTE         = "fileOneImage"
    PICTURECONFIRM              = (By.ID, "dialog_save")


class MHPageLocators:
    """
    Name         :  运营 - 微助力 - 元素定位
    Author       :  刘建民
    Create Date  :  2016/08/23
    """

    BIGPIC                      = (By.ID, "BgiImgUrl")
    SMALLPIC                    = (By.ID, "ImgSmallUrl")
    CONFIRM                     = (By.XPATH, ".//*[@id='upImgs']/div/div/div[5]/button[2]")
    BACKGROUNDBUTTON            = (By.ID, "raBackgroundImgUrl")
    SAVE                        = (By.ID, "saveRacBtn")
    FILEIMAGE                   = (By.ID, "fileImage")
    FILEIMAGELOCATE             = "fileImage"
    DOC                         = (By.ID, "doc")
    DOCLOCATE                   = 'doc'
    BACKGROUNDCONFIRM           = (By.XPATH, ".//*[@id='upImgs']/div/div/div[5]/button[2]")
    SHARETITLE                  = (By.ID, 'raShareTitle')
    SHAREDESCRIPTION            = (By.ID, 'raShareDesc')
    EVENTMAINBODY               = (By.XPATH, "html/body")
    IFRAME                      = "ueditor_0"
    FRIENDCOLLECTNUM            = (By.ID, 'raNum')
    UNIT                        = (By.ID, 'raUnit')
    VALIDCHANCE                 = (By.ID, 'raPro')
    NUMBERCONFIG                = (By.ID, 'raTotalPeople')
    ADDPRIZEBUTTON              = (By.XPATH, ".//*[@id='setForm']/div[4]/div[3]/div[5]/div")
    PRIZENAME                   = (By.XPATH, ".//*[@id='awardForm']/div/div[2]/table/tbody/tr[2]/td/div/select")
    PRIZENUMBER                 = (By.XPATH, ".//*[@id='awardForm']/div/div[2]/table/tbody/tr[3]/td/div/input")
    SELECT                      = ".//*[@id='awardForm']/div/div[2]/table/tbody/tr[2]/td/div/select/option[%d]"
    PRIZECONFIRM                = (By.ID, 'addAward')
    NEWMICROHELP                = (By.XPATH, ".//*[@id='section']/div[1]/table/tbody/tr[1]/td[3]")
    EVENTNAME                   = (By.ID, "raName")
    TYPESTARTDATE               = (By.ID, "js-startDate")
    TYPEENDDATE                 = (By.ID, "js-endDate")




