import unittest,time,requests,random,json,pymysql,HTMLTestReportCN
#禁用https请求警告
#from requests.packages.urllib3.exceptions import InsecureRequestWarning
#requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
from second_test_log.logmethod import *
from second_test_method.base_method import *
from second_test_method.excel_method import *

#获取访问令牌
class  Token(unittest.TestCase):
    @classmethod          # 声明为类方法（必须）
    def setUpClass(cls):  # 类方法，注意后面是cls，整个类只执行一次
        cls.logger=logger(os.path.basename(__file__))
        cls.logger.debug('_______start_______')

    @classmethod
    def tearDownClass(cls):
        cls.logger.debug('_______stop______')

    #正常获取未过期token   -   is_refresh字段是0
    def test01(self):
        msg_=frequentlyMethod.duQu_Excel(self,'v2','令牌',1,8 )
        response=requestMethod().Get_register('v2','令牌',1,4,3,2)
        print("响应时间->：%s" % response.elapsed.total_seconds())
        print("字符串方式的响应体->：%s"%response.text)

        self.logger.debug(response.text)
        self.logger.debug(response.url)
        self.assertEqual(msg_,response.json()['return_code'],msg='断言失败显示错误')

    # 正常获取未过期token   -   缺少is_refresh字段
    def test02(self):
        msg_=frequentlyMethod.duQu_Excel(self,'v2','令牌',2,8 )
        response=requestMethod().Get_register('v2','令牌',2,4,3,2)
        self.logger.debug(response.text)
        self.logger.debug(response.url)
        self.assertEqual(msg_,response.json()['return_code'])

    # 正常获取未过期token   -   is_refresh字段是0
    def test03(self):
        msg_=frequentlyMethod.duQu_Excel(self,'v2','令牌',3,8 )
        response=requestMethod().Get_register('v2','令牌',3,4,3,2)
        self.logger.debug(response.text)
        self.logger.debug(response.url)
        self.assertEqual(msg_,response.json()['return_code'])

    # 正常获取未过期token   -   is_refresh字段是null
    def test04(self):
        msg_=frequentlyMethod.duQu_Excel(self,'v2','令牌',4,8 )
        response=requestMethod().Get_register('v2','令牌',4,4,3,2)
        self.logger.debug(response.text)
        self.logger.debug(response.url)
        self.assertEqual(msg_,response.json()['return_code'])

    # 不输入app_id
    def test05(self):
        msg_=frequentlyMethod.duQu_Excel(self,'v2','令牌',5,8 )
        response=requestMethod().Get_register('v2','令牌',5,4,3,2)
        self.logger.debug(response.text)
        self.logger.debug(response.url)
        self.assertEqual(msg_,response.json()['return_msg'])

    # 不输入时间戳time_stamp
    def test06(self):
        msg_=frequentlyMethod.duQu_Excel(self,'v2','令牌',6,8 )
        response=requestMethod().Get_register('v2','令牌',6,4,3,2)
        self.logger.debug(response.text)
        self.logger.debug(response.url)
        self.assertEqual(msg_,response.json()['return_msg'])

    #不输入签名sign
    def test07(self):
        msg_ = frequentlyMethod.duQu_Excel(self, 'v2', '令牌', 7, 8)
        response = requestMethod().Get_register('v2', '令牌', 7, 4, 3, 2)
        self.logger.debug(response.text)
        self.logger.debug(response.url)
        self.assertEqual(msg_, response.json()['return_msg'])

        # 不输入签名类型sign_type
    def test08(self):
        msg_ = frequentlyMethod.duQu_Excel(self, 'v2', '令牌', 8, 8)
        response = requestMethod().Get_register('v2', '令牌', 8, 4, 3, 2)
        self.logger.debug(response.text)
        self.logger.debug(response.url)
        self.assertEqual(msg_, response.json()['return_msg'])

    #输入错误的app_id
    def test09(self):
        msg_=frequentlyMethod.duQu_Excel(self,'v2','令牌',9,8 )
        response=requestMethod().Get_register('v2','令牌',9,4,3,2)
        self.logger.debug(response.text)
        self.logger.debug(response.url)
        self.assertEqual(msg_,response.json()['return_msg'])

        # 输入签名错误
    def test10(self):
        msg_ = frequentlyMethod.duQu_Excel(self, 'v2', '令牌', 10, 8)
        response = requestMethod().Get_register('v2', '令牌', 10, 4, 3, 2)
        self.logger.debug(response.text)
        self.logger.debug(response.url)
        self.assertEqual(msg_, response.json()['return_code'])

        # 输入的app_id不存在
    def test11(self):
        msg_ = frequentlyMethod.duQu_Excel(self, 'v2', '令牌', 11, 8)
        response = requestMethod().Get_register('v2', '令牌', 11, 4, 3, 2)
        self.logger.debug(response.text)
        self.logger.debug(response.url)
        self.assertEqual(msg_, response.json()['return_msg'])

#调用接口方式为POST方式
    def test12(self):
        msg_=frequentlyMethod.duQu_Excel(self,'v2','令牌',12,8 )
        response=requestMethod().Post_register('v2','令牌',12,4,3,2)
        self.logger.debug(response.text)
        self.logger.debug(response.url)
        self.assertEqual(msg_,response.json()['return_code'])

    #前后带有空格
    def test13(self):
        msg_=frequentlyMethod.duQu_Excel(self,'v2','令牌',13,8 )
        response=requestMethod().Get_register('v2','令牌',13,4,3,2)
        self.logger.debug(response.text)
        self.logger.debug(response.url)
        self.assertEqual(msg_,response.json()['return_code'])

    #时间戳超过180s
    def test14(self):
        msg_=frequentlyMethod.duQu_Excel(self,'v2','令牌',14,8 )
        response=requestMethod().Get_register('v2','令牌',14,4,3,2)
        self.logger.debug(response.text)
        self.logger.debug(response.url)
        self.assertEqual(msg_,response.json()['return_code'])

    #is_refresh字段传1，获取一个新的token
    def test15(self):
        msg_=frequentlyMethod.duQu_Excel(self,'v2','令牌',15,8 )
        response=requestMethod().Get_register('v2','令牌',15,4,3,2)
        self.logger.debug(response.text)
        self.logger.debug(response.url)
        self.assertEqual(msg_,response.json()['return_code'])

    #token有效期为一天
    def test16(self):
        msg_=frequentlyMethod.duQu_Excel(self,'v2','令牌',16,8 )
        response=requestMethod().Get_register('v2','令牌',16,4,3,2)
        self.logger.debug(response.text)
        self.logger.debug(response.url)
        self.assertEqual(msg_,response.json()['return_data']['expires_in'])



#添加
def suite():
    #定义一个单元测试容器
    suiteTest = unittest.TestSuite()
    suiteTest.addTest(Token('test01'))
    suiteTest.addTest(Token('test02'))
    suiteTest.addTest(Token('test03'))
    suiteTest.addTest(Token('test04'))
    suiteTest.addTest(Token('test05'))
    suiteTest.addTest(Token('test06'))
    suiteTest.addTest(Token('test07'))
    suiteTest.addTest(Token('test08'))
    suiteTest.addTest(Token('test09'))
    suiteTest.addTest(Token('test10'))
    suiteTest.addTest(Token('test11'))
    suiteTest.addTest(Token('test12'))
    suiteTest.addTest(Token('test13'))
    suiteTest.addTest(Token('test14'))
    suiteTest.addTest(Token('test15'))
    suiteTest.addTest(Token('test16'))
    return suiteTest




if __name__ == '__main__':
    '''我们在如果想要生成测试报告，那么一定要注意右键执行时选择的右键菜单，一定要当做文件执行，不要让编辑器当做用例执行'''
    #确定生成报告的路径
    pathCode = paths['上上一级'] + '\openyinmei\second_test_result\\'
    curtime = time.strftime('%Y%m%d%H%M%S', time.localtime())
    report_path = pathCode + curtime + 'test_case001'+'.html'
    report_set = open(report_path, 'wb')

    #生成报告的Title,描述
    runner = HTMLTestReportCN.HTMLTestRunner(
        stream=report_set,
        title='自动化测试报告',
        description='详细测试用例结果',
        tester='zhong'
        )
    #运行测试用例
    runner.run(suite())
    # 关闭文件，否则会无法生成文件
    report_set.close()
    #smtpMethod.smtp_mail('qq', '578740769@qq.com', '36694640@qq.com')