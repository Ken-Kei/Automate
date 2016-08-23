# -*- coding: UTF-8 -*-


"""
Author       :  刘建民
Create Date  :  2016/7/1
"""


import configparser
import time
import os
import xlrd
from xlutils3.copy import copy


# ====================================================================
"""初始化配置文件"""

config = configparser.ConfigParser()
config.read("config.ini")
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
big_pic_name = config.get("operation_data_setting", "big_pic_name")  # 卡券封面大图
small_pic_name = config.get("operation_data_setting", "small_pic_name")  # 卡券封面小图


pickit_classify_name = config.get("operation_data_setting", "pickit_classify_name")  # 套图分类名称
pickit_manage_url = config.get("operation_data_setting", "pickit_manage_url")  # 套图管理的url

pickit_url = config.get("operation_data_setting", "pickit_url")  # 新建套图的url
pickit_name = config.get("operation_data_setting", "pickit_name")  # 套图的名称
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
# ====================================================================


# ====================================================================
"""初始化读excel操作"""

data = xlrd.open_workbook(data_source)
table = data.sheet_by_name('account')
copy_data = copy(data)
copy_sheet = copy_data.get_sheet(0)
# ====================================================================


# ====================================================================
"""log文件和截图文件路径变量"""

launch_log_path = os.path.join("./Log/Log_" + time.strftime("%Y%m%d"))
launch_screenshot_path = os.path.join("./Log/Screenshot_" + time.strftime("%Y%m%d"))
launch_result_path = os.path.join("./Result/Result_" + time.strftime("%Y%m%d"))
# ====================================================================


# ====================================================================
"""log信息"""

login_succeed = "登录成功"
login_failed = "找不到登录后的关键字，登录失败"
loging_in = "正在使用此用户登录: %s"
# 输出到控制台信息
finishmsg = '************************ Finish ************************'
# ====================================================================


# ====================================================================
"""指定邮件标题、正文及其它信息"""

# 邮件标题
subject = '自动化用例执行结果'

# 邮件正文
main_body = """
自动化用例已经执行完成，用例的详细执行状况请查看附件。
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
