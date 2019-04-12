import time,random,os,xlrd,smtplib,requests,json,hashlib
from xlutils.copy import copy #复制写入
from email.mime.text import  MIMEText
from email.mime.multipart import MIMEMultipart
from second_test_log.logmethod import *
from second_test_conf.env.config import *
from second_test_method.excel_method import frequentlyMethod
from second_test_method.sqlhelper_method import mysqlHelper


from second_test_conf.env.config import MustCode
from second_test_conf.env.config import *


class smtpMethod(object):
    def __init__(self):
        self.logger = logger(os.path.basename(__file__))
    '''发送邮件方法'''
    @staticmethod
    def smtp_mail(choocemail, sendmail,receivemail):  # choocemail选择163还是qq,sendmail发件人，receivemail收件人

        path=paths['上上一级']+'\openyinmei\second_test_result\\'
        lists = os.listdir(path)
        filepath = path + lists[-1]
        with open(filepath, "rb") as fp:
            mail_body = fp.read()
        if choocemail == '163':  # 选择是163之后，所有的参数都是163的
            smtpserver = "smtp.163.com"  # 163邮箱服务器地址
            port = 0  # 端口号163邮箱为0，腾讯邮箱为 465 或者587
            mailtext = "您好:</br><p>　　　　请下载附件之后，由谷歌打开查看测试报告详情！</p>"  # 邮件内容
            mailCode = MIMEMultipart()
            # 使用MUMEText构造文本邮件字典
            mailCode['from'] = sendmail  # 添加发件人键值对
            mailCode['to'] = receivemail  # 添加收件人键值对
            mailCode['subject'] = '自动化测试报告'  # 添加文本主题键值对

            body = MIMEText(mailtext, "html", "utf-8")
            mailCode.attach(body)
            # 添加附件
            att = MIMEText(mail_body, "base64", "utf-8")
            att["Content-Type"] = "application/octet-stream"
            att["Content-Disposition"] = 'attachment; filename="test_report.html"'
            mailCode.attach(att)

            smtp = smtplib.SMTP()  # 使用该方法发送邮件
            smtp.connect(smtpserver)  # 链接服务器
            smtp.login(sendmail, 'qhjbbfqngrdsbfga')  # 登录
            smtp.sendmail(sendmail, receivemail, mailCode.as_string())  # 发送
            smtp.quit()  # 关闭
        if choocemail == 'qq':
            smtpserver = "smtp.qq.com"  # qq邮箱服务器地址
            port = 465
            mailtext = "您好:</br><p>　　　　请下载附件之后，由谷歌打开查看测试报告详情！</p>"  # 邮件内容
            mailCode = MIMEMultipart()

            mailCode['from'] = sendmail
            mailCode['to'] = receivemail
            mailCode['subject'] = '自动化测试报告'

            text = MIMEText(mailtext, 'html', 'utf-8')  # 构造邮件
            mailCode.attach(text)

            # 添加附件
            att = MIMEText(mail_body, "base64", "utf-8")
            att["Content-Type"] = "application/octet-stream"
            att["Content-Disposition"] = 'attachment; filename="report.html"'
            mailCode.attach(att)

        smtp = smtplib.SMTP_SSL(smtpserver, port)
        smtp.login(sendmail, "qhjbbfqngrdsbfga")  # 登录
        smtp.sendmail(sendmail, receivemail, mailCode.as_string())  # 发送
        smtp.quit()  # 关闭



class requestMethod(object):
    def __init__(self):
        self.logger = logger(os.path.basename(__file__))

    """get请求"""
    @staticmethod
    def get_v2(url,param,header):
        url = url
        params = param
        headers = header
        if param==None:
            response = requests.get(url, headers=headers,verify=False)
        else:
            response = requests.get(url, params=params, headers=headers, verify=False)
        return  response


    @staticmethod
    #get请求 直接获取Excel表格内容，并完成接口访问，返回接口返回内容
    def Get_register(ExcelName,SheetName,Row,column_url,column_header,column_data):
        url = MustCode['url'] + frequentlyMethod().duQu_Excel(ExcelName, SheetName, Row, column_url)
        header = frequentlyMethod().duQu_Excel(ExcelName, SheetName, Row, column_header)
        param = frequentlyMethod().duQu_Excel(ExcelName,SheetName, Row, column_data)
        str_data = json.loads(param)
        response = requests.get(url, headers=eval(header), params=str_data , verify=False)
        return response

    @staticmethod
    #get请求 获取config变量内容，获取Excel表格内容，并完成接口访问，返回接口返回内容
    def Get_registers(ExcelName,SheetName,Row,column_url,column_header):
        url = MustCode['url'] + frequentlyMethod().duQu_Excel(ExcelName, SheetName, Row, column_url)
        header = frequentlyMethod().duQu_Excel(ExcelName, SheetName, Row, column_header)
        param ={"app_id": MustCode['appid'],
                "access_token": frequentlyMethod().readToken(),
                "device_id":MustCode['device_id']}
        response = requests.get(url, headers=eval(header), params=param , verify=False)
        return response



    """post请求"""
    @staticmethod
    def  post_v2(url,data,header):
        url = url
        headers = header
        data = data
        response=requests.post(url,data=data,headers=header,verify=False)
        return response


    @staticmethod
    # post请求 直接获取Excel表格内容，并完成接口访问，返回接口返回内容
    def Post_register(ExcelName,SheetName,Row,column_url,column_header,column_data):
        url = MustCode['url'] + frequentlyMethod().duQu_Excel(ExcelName, SheetName, Row, column_url )
        header = frequentlyMethod().duQu_Excel(ExcelName, SheetName, Row, column_header)
        data = frequentlyMethod().duQu_Excel(ExcelName,SheetName, Row, column_data)
        str_data=json.loads(data)
        response = requests.post(url, headers=eval(header), data=str_data, verify=False)
        return response

    @staticmethod
    # post请求 获取config变量内容，直接获取Excel表格内容，并完成接口访问，返回接口返回内容
    def Post_registers(ExcelName,SheetName,Row,column_url,column_header):
        url = MustCode['url'] + frequentlyMethod().duQu_Excel(ExcelName, SheetName, Row, column_url )
        header = frequentlyMethod().duQu_Excel(ExcelName, SheetName, Row, column_header)
        param ={"app_id":MustCode['appid'],
                "access_token":frequentlyMethod().readToken(),
                "device_codes":MustCode['device_codes']
                }
        response = requests.post(url, headers=eval(header), data=param, verify=False)
        return response



    @ staticmethod
     # post请求 获取config变量内容，直接获取Excel表格内容，并完成接口访问，返回接口返回内容。调用打印方式接口
    def Post_print(ExcelName,SheetName,Row,column_url,column_header):
        url = MustCode['url'] + frequentlyMethod().duQu_Excel(ExcelName, SheetName, Row, column_url )
        header = frequentlyMethod().duQu_Excel(ExcelName, SheetName, Row, column_header)
        param ={"app_id":MustCode['appid'],
                "access_token":frequentlyMethod().readToken(),
                "device_id":MustCode['device_id'],
                "copies":MustCode['copies'],
                "cus_orderid":MustCode['cus_orderid'] ,
                "bill_content":MustCode['bill_content'] ,
                "paper_width": MustCode['paper_width'],
                "paper_height":MustCode['paper_height'] ,
                "paper_type":MustCode['paper_type'] ,
                "time_out": MustCode['time_out'],
                "sign":MustCode['sign'] ,
                "sign_type":MustCode['sign_type']
                }
        response = requests.post(url, headers=eval(header), data=param, verify=False)
        return response



    @staticmethod
    # 直接获取Excel表格内容，并返回一个字典
    def  Excel_Dict(ExcelName,SheetName,Row,column_url,column_header,column_data):
        url = MustCode['url'] + frequentlyMethod().duQu_Excel(ExcelName,SheetName,Row,column_url)
        headers = frequentlyMethod().duQu_Excel(ExcelName,SheetName,Row,column_header)
        data = frequentlyMethod().duQu_Excel(ExcelName,SheetName,Row,column_data)
        Excel_Dict_Code={'url':url,'headers':eval(headers),'data':eval(data)}
        return Excel_Dict_Code


    """获取token"""
    @staticmethod
    def token(app_id,app_key):
        time_stamp=MustCode['time_stamp']
        md5parameter = 'app_id=' + app_id + '&sign_type=MD5&time_stamp=' + time_stamp + '&key=' + app_key
        md5 = hashlib.md5(md5parameter.encode(encoding='UTF-8')).hexdigest()
        sign = md5.upper()

        url =MustCode['url']+'mcp/v2/sys/GetAccessToken'
        headers =MustCode['headers']
        data  ={
    "app_id": app_id,
    "time_stamp": time_stamp,
    "sign":sign,
    "sign_type": "MD5",
    "is_refresh": ""
}
        response=requests.get(url,headers=headers,data=data,verify=False)
        token=response.json()['return_data']['access_token']
        with open(os.path.dirname(os.path.dirname(__file__))+'/second_test_method/token.txt','w')  as  f:
            f.write(token)
        return token


class sqlMethod(object):
    def __init__(self):
        self.__helper=mysqlHelper()

    '''根据appid取token'''
    def token(self,appid):
        sql='select * from mcp_app_token where app_id=%s'
        params=appid
        return self.__helper.getOne(sql,params)

    '''根据appid,查询cmd命令执行状态'''
    def cmd_status(self,appid):
        sql='select * from mcp_cmd_order_printer where order_id=(select order_id from mcp_cmd_order where app_id=%s limit 1)'
        params = appid
        return self.__helper.getOne(sql, params)

    '''根据appid和打印机,查询cmd命令执行状态'''
    def cmd_status(self,printercode,appid):
        sql='select * from mcp_cmd_order_printer where printer_code=%s AND order_id=(select order_id from mcp_cmd_order where app_id=%s limit 1)'
        params = (printercode,appid)
        return self.__helper.getOne(sql, params)

    '''根据打印机,查询订单执行状态'''
    def order_status(self,printercode):
        sql='SELECT * FROM mcp_order_printer WHERE printer_code=%s'
        params = printercode
        return self.__helper.getOne(sql, params)

    '''查看打印机状态'''
    def printer_status(self,printercode):
        sql='SELECT * FROM mcp_printer_status WHERE printer_code=%s '
        params = printercode
        return self.__helper.getOne(sql, params)
