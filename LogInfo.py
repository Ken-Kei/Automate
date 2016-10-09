# -*- coding: UTF-8 -*-


"""
Author       :  Ken-Kei
Create Date  :  2016/08/24
"""


class PublicLogInfo:

    """
    Name         :  公共日志 - 打印信息
    Author       :  Ken-Kei
    Create Date  :  2016/08/24
    """

    UPLOADINGBIGPIC                 = '正在上传大图：%s'
    UPLOADPICFIN                    = '上传图片完毕'
    UPLOADINGSMALLPIC               = '正在上传封面小图：%s'
    UPLOADSMALLPICFIN               = '上传封面小图完毕'
    UPLOADNOTFOUND                  = '找不到上传图片的按钮位置'
    ALERTNOTFOUND                   = '找不到alert窗口'
    SAVEBUTTONNOTFOUND              = '找不到保存按钮'
    CONFIRMNOTFOUND                 = '找不到确定按钮'
    DROPDOWNLISTNOTFOUND            = '找不到下拉框'


class MHLogInfo:

    """
    Name         :  运营 - 微助力 - 打印信息
    Author       :  Ken-Kei
    Create Date  :  2016/08/24
    """

    TYPENAME                        = '输入活动名称：%s'
    NAMEFIELDNOTFOUND               = '找不到活动名称输入框位置'
    STARTDATENOTFOUND               = '找不到微助力活动开始时间输入框位置'
    ENDDATENOTFOUND                 = '找不到微助力活动结束时间输入框位置'
    UPLOADINGBGPIC                  = '正在上传微助力背景图：%s'
    UPLOADBGPICFIN                  = '上传背景图完毕'
    TYPESHARETITLE                  = '输入分享标题：%s'
    SHARETITLENOTFOUND              = '找不到分享标题输入框位置'
    TYPESHAREDESC                   = '输入分享描述：%s'
    SHAREDESCNOTFOUND               = '找不到分享描述输入框位置'
    EVENTDESC                       = '找不到活动详情的元素位置'
    FRIENDCOLLECTNUM                = '输入好友集满数量：%s'
    FCNOTFOUND                      = '找不到好友集满数量输入框位置'
    TYPEUNIT                        = '输入好友集满数量的单位：%s'
    UNITNOTFOUND                    = '找不到单位输入框位置'
    TYPEVALIDCHANCE                 = '输入好友有效助力概率：%s'
    VCNOTFOUND                      = '找不到好友有效助力概率输入框位置'
    TYPENUMCONFIG                   = '输入数量设置：%s'
    NCNOTFOUND                      = '找不到数量设置输入框位置'
    ADDPRIZE                        = '正在添加奖品'
    APNOTFOUND                      = '找不到添加奖品按钮位置'
    PRIZENOTFOUND                   = '找不到奖品'
    TYPEEVENTDESC                   = '输入活动详情：%s'
    TYPESTARTTIME                   = '输入微助力活动开始时间：%s'
    TYPEENDTIME                     = '输入微助力活动结束时间：%s'
    SELECTPRIZE                     = '选择了奖品：%s'
    TYPEPRIZENUMBER                 = '输入奖品数量：%s'
    MHCREATESUCCEED                 = '微助力活动创建成功，用例通过'
    MHCREATEFAILED                  = '没有找到微助力活动，用例执行失败'


class CCLogInfo:

    """
    Name         :  运营 - 卡券中心 - 打印信息
    Author       :  Ken-Kei
    Create Date  :  2016/09/08
    """

    OPERTABNOTFOUND                 = '没找到运营模块的标签元素'
    TYPECARDNAME                    = '输入卡券名称：%s'
    CARDNAMENOTFOUND                = '没找到卡券名称的元素位置'
    TYPECARDREBATE                  = '输入折扣率：%s'
    CARDREBATENOTFOUND              = '没找到卡券折扣率的元素位置'
    CHOOSEIMMEDIATE                 = '选择卡券有效期类型为：领取后生效'
    CCVNOTFOUND                     = '没找到选择卡券有效期类型的单选框'
    CARDNAMEEXIST                   = '卡券名称已存在，请使用一个新的卡券名称'
    SUITENOTFOUND                   = '没找到上传适用商品的按钮'
    UPLOADINGSUITEPIC               = '正在上传适用商品图：%s'
    UPLOADSUITEPICFIN               = '上传适用商品图完毕'
    TYPEGOODSUMMARY                 = '输入商品简介：%s'
    GSNOTFOUND                      = '没找到商品简介的元素位置'
    TYPECARDINVENT                  = '输入卡券库存：%s'
    CARDINVENTNOTFOUND              = '没找到优惠券库存的元素位置'
    CARDCREATESUCCEED               = '卡券创建成功,用例执行通过'
    CARDCREATEFAILED                = '没有找到卡券，用例执行失败'


class LoginLogInfo:

    """
    Name         :  登入登出 - 打印信息
    Author       :  Ken-Kei
    Create Date  :  2016/09/13
    """

    ACCOUNTNOTFOUND                 = '找不到账号输入框'
    PASSNOTFOUND                    = '找不到密码输入框'
    LOGINBUTTONNOTFOUND             = '找不到登录按钮'
    LOGOUTNOTFOUND                  = '找不到登出按钮'
    LOGINFAILED                     = '找不到登录后的关键字，登录失败'
    WRONGUSERLOGINFAILED            = '找不到登录后的关键字，用错误的用户名登录失败，用例执行通过'
    LOGINSUCCEED                    = "登录成功"
    WRONGUSERLOGINSUCCEED           = "用错误的用户名登录成功，用例执行失败"
    WRONGPWDLOGINFAILED             = '找不到登录后的关键字，用错误的密码登录失败，用例执行通过'
    WRONGPWDLOGINSUCCEED            = "用错误的密码登录成功，用例执行失败"


class PMLogInfo:

    """
    Name         :  运营 - 套图管理 - 打印信息
    Author       :  Ken-Kei
    Create Date  :  2016/09/13
    """

    PCBUTTONNOTFOUND                = '找不到新建分类按钮'
    TYPECLASSNAME                   = '输入套图分类名称：%s'
    CLASSNAMEFIELDNOTFOUND          = '找不到套图分类名称输入框，输入失败'
    COLORFIELD                      = '选择分类的颜色标识：绿色'
    COLORFIELDNOTFOUND              = '找不到套图分类颜色标识'
    TYPEPICNAME                     = '输入套图的名称：%s'
    PICNAMEFIELDNOTFOUND            = '找不到套图名称输入框位置'
    SELECTCLASSBELONG               = '选择套图的所属分类：%s'
    CBDROPDOWNNOTFOUND              = '找不到套图分类下拉框下的分类'
    TYPEPICDESC                     = '输入套图介绍：%s'
    PICDESCFIELDNOTFOUND            = '找不到套图介绍输入框位置'
    UPLOADFIRSTPIC                  = '正在上传第一张套图：%s'
    PICUPLOADFIN                    = '上传套图完毕'
    PICCLASSCREATESUCCEED           = '套图分类创建成功，用例通过'
    PICCLASSCREATEFAILED            = '没有找到套图分类，用例执行失败'
    PICCREATESUCCEED                = '套图创建成功，用例通过'
    PICCREATEFAILED                 = '没有找到套图，用例执行失败'


class CQLogInfo:

    """
    Name         :  运营 - 渠道二维码 - 打印信息
    Author       :  Ken-Kei
    Create Date  :  2016/09/20
    """

    CREATINGQRCODE                  = '正在创建二维码'
    CREATEBUTTONNOTFOUND            = '找不到创建二维码的按钮'
    SELECTINGCODETYPE               = '正在选择二维码的类型'
    CODEDROPNOTFOUND                = '找不到下拉框的位置'
    SELECTCODETYPE                  = '选择创建的二维码的类型为：%s'
    TEMPCODENOTFOUND                = '找不到二维码的选项'
    TYPEQRCODENAME                  = '输入二维码的名称：%s'
    QRCODENAMENOTFOUND              = '找不到二维码名字输入框'
    QRCODETYPENOTLEGAL              = '配置的二维码类型不合法，请检查qrcode_type字段'
    QRCODELISTNOTFOUND              = '找不到二维码列表位置'
    CODECREATESUCCEED               = '二维码创建成功，用例执行通过'
    CODECREATEFAILED                = '二维码创建失败，用例执行失败'


class SLLogInfo:

    """
    Name         :  门店 - 门店列表 - 打印信息
    Author       :  Ken-Kei
    Create Date  :  2016/09/21
    """

    CREATEBUTTONNOTFOUND            = '找不到新增按钮'
    TYPESTORENAME                   = '输入门店名称：%s'
    STORETYPEDROPNOTFOUND           = '找不到门店类型的下拉框'
    SELECTSTORETYPE                 = '选择门店类型：%s'
    STORETYPENOTFOUND               = '找不到相应的门店类型：%s'
    WRONGSTORETYPE                  = '配置的门店类型不合法，请检查store_type字段'
    SELECTSTORESTATUS               = '选择门店状态：%s'
    WRONGSTORESTATUS                = '配置的门店状态不合法，请检查store_status字段'
    STORESTATUSNOTFOUND             = '找不到相应的门店状态：%s'
    TYPESTOREPHONE                  = '输入门店电话：%s'
    STORENAMENOTFOUND               = '找不到门店名称输入框'
    STOREPHONENOTFOUND              = '找不到门店电话输入框'
    TYPECONTACT                     = '输入联系人：%s'
    CONTACTNOTFOUND                 = '找不到联系人的输入框'
    SELECTMANAGESCOPE               = '选择经营范围：%s'
    WRONGFATHERMANGESCOPE           = '配置的父级经营范围不合法，请检查father_manage_scope字段'
    MANAGESCOPENOTFOUND             = '找不到相应的经营范围：%s'
    WRONGMANGESCOPE                 = '配置的子级经营范围不合法，请检查manage_scope字段'
