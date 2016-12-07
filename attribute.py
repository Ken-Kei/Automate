# -*- coding: UTF-8 -*-


"""
Author       :  Ken-Kei
Create Date  :  2016/07/01
"""


import configparser
import time
import os
import xlrd
from xlutils3.copy import copy


# ====================================================================
config = configparser.ConfigParser()
config.read("config.ini", encoding='UTF-8')
# ====================================================================


# ====================================================================
"""指定驱动文件位置"""

chrome_driver_path = os.path.join("./Driver/chromedriver.exe")
ie_driver_path = os.path.join("./Driver/IEDriverServer.exe")
# ====================================================================


# ====================================================================
"""Config.ini属性配置"""

# [url_info]
browser = config.get("url_info", "browser")  # 选择浏览器
main_url = config.get("url_info", "main_url")  # 主页url
waiting_time = config.getint("url_info", "waiting_time")  # 页面等待时间
operation_system = config.get("url_info", "operation_system")  # 测试使用的操作系统

# [account_info]
account_row = config.getint("account_info", "account_row")  # 读取到excel表的账号行数
username = config.get("account_info", "username")  # 后台使用的账号
password = config.get("account_info", "password")  # 后台使用的密码
wrong_username = config.get("account_info", "wrong_username")  # 错误的用户名
wrong_password = config.get("account_info", "wrong_password")  # 错误的密码

# [test_result]
data_source = config.get("test_result", "data_source")  # 测试数据数据源
need_screenshot = config.get("test_result", "need_screenshot")  # 是否需要截图

# [email_info]
smtp_server = config.get("email_info", "smtp_server")  # smtp服务器地址
smtp_server_port = config.get("email_info", "smtp_server_port")  # smtp服务器地址端口号
from_email_address = config.get("email_info", "from_email_address")  # 发件人账号
from_email_address_pwd = config.get("email_info", "from_email_address_pwd")  # 发件人密码
to_mail_address = config.get("email_info", "to_email_address").split(',')  # 收件人地址
cc_mail_address = config.get("email_info", "cc_email_address").split(',')  # 抄送人地址

# [cron_job_time_setting]
time_set = config.get("cron_job_time_setting", "time_set")  # 定时任务触发的时间

# [operation_data_setting]
card_center_url = config.get("operation_data_setting", "card_center_url")  # 卡券中心的url
card_name = config.get("operation_data_setting", "card_name")  # 卡券名称
rebate_data = config.get("operation_data_setting", "rebate_data")  # 折扣率
goods_summary = config.get("operation_data_setting", "goods_summary")  # 商品简介
inventory_data = config.get("operation_data_setting", "inventory_data")  # 优惠券库存
big_image_name = config.get("operation_data_setting", "big_image_name")  # 卡券封面大图
small_image_name = config.get("operation_data_setting", "small_image_name")  # 卡券封面小图
picture_classify_name = config.get("operation_data_setting", "pickit_classify_name")  # 套图分类名称
pickit_manage_url = config.get("operation_data_setting", "pickit_manage_url")  # 套图管理的url
pickit_url = config.get("operation_data_setting", "pickit_url")  # 新建套图的url
picture_name = config.get("operation_data_setting", "pickit_name")  # 套图的名称
pickit_description = config.get("operation_data_setting", "pickit_description")  # 套图介绍
pickit1 = config.get("operation_data_setting", "pickit1")  # 上传的第一张套图的名称
micro_help_url = config.get("operation_data_setting", "micro_help_url")  # 微助力的url
activity_name = config.get("operation_data_setting", "activity_name")  # 微助力活动名称
share_title = config.get("operation_data_setting", "share_title")  # 微助力分享标题
share_description = config.get("operation_data_setting", "share_description")  # 微助力分享描述
event_description = config.get("operation_data_setting", "event_description")  # 微助力活动详情
friend_collect_number = config.getint("operation_data_setting", "friend_collect_number")  # 好友集满数量
unit = config.get("operation_data_setting", "unit")  # 单位
friend_valid_chance = config.getint("operation_data_setting", "friend_valid_chance")  # 好友有效助力概率
number_config = config.getint("operation_data_setting", "number_config")  # 数量设置
prize_number = config.getint("operation_data_setting", "prize_number")  # 奖品数量
qrcode_url = config.get("operation_data_setting", "qrcode_url")  # 二维码名称
qrcode_type = config.getint("operation_data_setting", "qrcode_type")  # 渠道二维码的类型设置
qrcode_temp_name = config.get("operation_data_setting", "qrcode_temp_name")  # 临时二维码名称
qrcode_forever_name = config.get("operation_data_setting", "qrcode_forever_name")  # 永久二维码名称
store_name = config.get("store_data_setting", "store_name")  # 门店名称
store_type = config.get("store_data_setting", "store_type")  # 门店类型
store_status = config.get("store_data_setting", "store_status")  # 门店状态
store_phone = config.get("store_data_setting", "store_phone")  # 门店电话
store_contact = config.get("store_data_setting", "store_contact")  # 联系人
father_manage_scope = config.get("store_data_setting", "father_manage_scope")  # 父级经营范围
manage_scope = config.get("store_data_setting", "manage_scope")  # 子级经营范围
# ====================================================================


# ====================================================================
"""初始化读excel操作"""

data_source_path = os.path.join("./DataSource/" + data_source)
data = xlrd.open_workbook(data_source_path)
table = data.sheet_by_name('account')
copy_data = copy(data)
copy_sheet = copy_data.get_sheet(0)
# ====================================================================


# ====================================================================
"""log文件和截图文件路径变量"""

launch_log_path = os.path.join("./Log/Log_" + time.strftime("%Y%m%d"))
launch_screenshot_path = os.path.join("./Log/Screenshot_" + time.strftime("%Y%m%d") + "/" + time.strftime("%H%M%S"))
launch_result_path = os.path.join("./Result/Result_" + time.strftime("%Y%m%d"))
big_image_name = os.path.join("./Image/" + big_image_name)
small_image_name = os.path.join("./Image/" + small_image_name)
# ====================================================================


# ====================================================================
"""截图文件名"""

# 登入登出截图
login_failed_screenshot = '登录失败'
login_succeed_screenshot = '登录成功'
logout_succeed_screenshot = '登出成功'
logout_failed_screenshot = '登出失败'

# 创建套图分类
create_pc_succeed_screenshot = '创建套图分类成功'
create_pc_failed_screenshot = '创建套图分类失败'

# 创建套图
create_pk_succeed_screenshot = '创建套图成功'
create_pk_failed_screenshot = '创建套图失败'

# 创建卡券
create_card_succeed_screenshot = '创建卡券成功'
create_card_failed_screenshot = '创建卡券失败'
card_name_exist_screenshot = '创建卡券失败-卡券名称重复'

# 创建微助力活动
create_mh_succeed_screenshot = '创建微助力成功'
create_mh_failed_screenshot = '创建微助力失败'

# 创建渠道二维码
create_code_succeed_screenshot = '创建渠道二维码成功'
create_code_failed_screenshot = '创建渠道二维码失败'
# ====================================================================


# 图库上传的元素位置
# .//*[@id='upImgs']/div/div/div[4]/div/div[2]/div/div[1]/div


# ====================================================================
"""用例名"""

test_LoginSucceed = '登入以及登出O2O平台成功'
test_LoginFailedWithWrongUser = '错误的用户名登录'
test_LoginFailedWithWrongPwd = '错误的密码登录'
test_CreatePictureClassify = '创建套图分类'
test_CreatePictureKit = '创建套图'
test_CreateCard = '创建卡券'
test_CreateMicroHelp = '创建微助力活动'
test_CreateQRCode = '创建渠道二维码'
# ====================================================================


# ====================================================================
"""log信息"""

loging_in = "正在使用此用户登录: %s"
# ====================================================================


# ====================================================================
"""指定邮件标题、正文及其它信息"""

# 邮件标题
subject = '自动化用例执行结果'

# 邮件正文
main_body = """
自动化测试用例已经执行完成，以下为测试报告概况，用例的详细执行状况请查看附件。

==============================================


这是自动发送的邮件，请勿答复。



以上
测试组
"""
# ====================================================================


# ====================================================================
"""JS语句"""

# 上传图片的元素id为fileImage
file_image_block = """document.getElementById('fileImage').style.display='block'; """
file_image_none = """document.getElementById('fileImage').style.display='none'; """
remove_sd_read_only = """document.getElementById('js-startDate').readOnly=false; """
remove_ed_read_only = """document.getElementById('js-endDate').readOnly=false; """
# ====================================================================
