import pymysql
from second_test_conf.env.config import *
from second_test_method.sqlhelper_method import mysqlHelper
from second_test_method.base_method import sqlMethod
import unittest,time,requests,random,json,pymysql,HTMLTestReportCN
#禁用https请求警告
#from requests.packages.urllib3.exceptions import InsecureRequestWarning
#requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
from second_test_log.logmethod import *
from second_test_method.base_method import *
from second_test_method.excel_method import *

# 1. 建立连接,磐石&&微云打测试
# conn = pymysql.connect(host='47.106.85.252',
#                     port=3306,
#                     user='root',
#                     passwd='123456',   # password也可以
#                     db='mcp_test',
#                     charset='utf8')   # 如果查询有中文需要指定数据库编码
#1. 建立连接,磐石&&微云打测试
# conn = pymysql.connect(**DataBase)
# # 2. 从连接建立游标（有了游标才能操作数据库）
# cur = conn.cursor()
# # 3. 查询数据库（读）
# cur.execute("SELECT * FROM mcp_order_printer WHERE printer_code = '18250267YT'")
# # 4. 获取查询结果
# result = cur.fetchone()
# print(result)
# 5. 关闭游标及连接
# cur.close()
# conn.close()


# token=sqlMethod().token('055d92d0b07c4de0954b0b93538d33b6')
# print(token)
# print(type(token))
# a=token['access_token']
# print(a)

# cmd=sqlMethod().cmd_status('2a6f1f4660c04fab8f8bac0dfa88a3a9')
# print(cmd)

# cmd=sqlMethod().cmd_status('18100001SQ','e8b7e6fc8ed349b1b78b137f491bfe1d')
# print(cmd)

# ordeer=sqlMethod().order_status('18250267YT')
# print(ordeer)

# printerstatus=sqlMethod().printer_status('18250267YT')
# print(printerstatus)

def test01(self):
    msg_ = frequentlyMethod.duQu_Excel(self, 'v2', '令牌', 1, 8)
    return msg_

a=test01(1)
print(a)
print(type(a))