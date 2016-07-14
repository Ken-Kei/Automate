# -*- coding: UTF-8 -*-


"""
Author       :  刘建民
Create Date  :  2016/7/1
Edit Date    :  2016/7/8
"""


import configparser
import time
import os
import xlrd
from xlutils3.copy import copy
from selenium.webdriver.common.by import By


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
waiting_time = config.getint("url_info", "waiting_time")  # 页面轮询等待时间
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
rebate_data = config.get("operation_data_setting", "rebate_data")  # 折扣率
inventory_data = config.get("operation_data_setting", "inventory_data")  # 优惠券库存
card_center_url = config.get("operation_data_setting", "card_center_url")  # 卡券中心的url
big_pic_name = config.get("operation_data_setting", "big_pic_name")  # 卡券封面大图
small_pic_name = config.get("operation_data_setting", "small_pic_name")  # 卡券封面小图
card_name = config.get("operation_data_setting", "card_name")  # 卡券名称

pickit_classify_name = config.get("operation_data_setting", "pickit_classify_name")  # 套图分类名称
pickit_manage_url = config.get("operation_data_setting", "pickit_manage_url")  # 套图管理的url
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
"""元素定位"""

# 登入登出元素定位
username_input = (By.CSS_SELECTOR, "#username")
password_input = (By.CSS_SELECTOR, "#password")
login_button = (By.CSS_SELECTOR, ".loginBtn")
user_account = (By.CSS_SELECTOR, "#spnUid")
logout_button = (By.CSS_SELECTOR, ".quit-nav>li>a")


# 运营模块--卡券中心元素定位
operation_tab_ele = (By.CSS_SELECTOR, "#current3")
card_center_ele = (By.XPATH, ".//*[@id='sidebar']/ul/li[5]/a/span[2]")
big_pic_ele = (By.ID, "ccPicBigImg")
small_pic_ele = (By.CSS_SELECTOR, "#ccPicSmallImg")
card_name_ele = (By.CSS_SELECTOR, "#coupon_name")
card_rebate_ele = (By.CSS_SELECTOR, "#ccRebateId")
card_validity_ele = (By.XPATH, ".//*[@id='ccSetForm']/div/div[8]/div/div[1]/label/input")
card_inventory_ele = (By.CSS_SELECTOR, "#ccInventory")
card_save_ele = (By.CSS_SELECTOR, ".btn-default.large-btn")
# 上传图片的元素位置
upload_button_ele = (By.CSS_SELECTOR, ".file-btn")
display_upload_button_ele = (By.ID, "fileImage")
# 上传图片的确认按钮
confirm_ele = (By.ID, "ccPicBigImgDia_btn1")
# 创建成功后的卡券定位
new_create_card_ele = (By.XPATH, ".//*[@id='setting']/table/tbody/tr[1]/td[1]")


# 运营模块--套图管理元素定位
create_pickit_classify_ele = (By.XPATH, ".//*[@id='content_body']/tbody/tr/td[1]/button")
classify_name_ele = (By.ID, "pmName")
color_type_ele = (By.XPATH, ".//*[@id='color_type']/li[1]")
classify_save_ele = (By.ID, "button")
new_create_pickit_classify_ele = (By.XPATH, ".//*[@class='cm_type active']/dl/dd[1]")
# ====================================================================


# ====================================================================
"""log信息"""

login_succeed = "登录成功"
login_failed = "找不到登录后的关键字，登录失败"
loging_in = "正在使用此用户登录: %s"
create_card_succeed = "卡券创建成功,用例执行通过"
create_card_failed = "没有找到卡券，卡券创建失败"
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
