import os ,time,hashlib

#路径
global paths
paths={}
paths['当前']=os.getcwd()
paths['上一级']=os.path.abspath(os.path.dirname(os.getcwd()) + os.path.sep + ".")
paths['上上一级']=os.path.abspath(os.path.dirname(os.getcwd()) + os.path.sep + "..")

#数据库环境
global DataBase
DataBase={}
DataBase['host']='47.106.85.252'
DataBase['port']=3306
DataBase['user']='root'
DataBase['passwd']='123456'
DataBase['db']='mcp_test'
#DataBase['charse']='utf8'


#请求、打印机基本信息
global MustCode
MustCode={}
MustCode['url']='http://mcp.yinmei.me:8081/'
#MustCode['url']=''#域发布
#NustCode['url']=''正式
MustCode['appid']='3a97adc2b23a4890b32ffd59a461872d'
MustCode['appkey']='deydrrxkdh2lrxmr'
MustCode['device_id']='17260165VL'
MustCode['device_codes']='17260165VL#5C3F'
MustCode['time_stamp']=str(int(time.time()))
MustCode['headers']={
    "Connection": "keep-alive",
    "Host": "mcp.yinmei.me:8081",
    "User-Agent": "Apache-HttpClient/4.5.5 (Java/1.8.0_121)"}
MustCode['copies']='1'
MustCode['cus_orderid']=str(int(time.time()))
MustCode['bill_content']='http://dev-open.yinmei.me/Content/htmltest/8.html'
MustCode['paper_width']=''
MustCode['paper_height']=''
MustCode['paper_type']='1'
MustCode['time_out']='180'
MustCode['sign']=''
MustCode['sign_type']='1'









global Email
Email = {}
Email['mailhost']=''
Email['user']=''
Email['pass']=''
Email['port']=''
Email['sender']=''
Email['receiver']=''
Email['subject']=''
Email['content']=''
Email['testuser']=''
Email['on_off']=''


#公用headers部分
global Headers_Dict
Headers_Dict={}
Headers_Dict['Host']=''
Headers_Dict['User-Agent']=''
Headers_Dict['Content-Type']='application/json'
Headers_Dict['Origin']=''
Headers_Dict['req-source']='MWEB'



