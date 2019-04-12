import unittest,time,requests,random,json,pymysql,HTMLTestReportCN
from second_test_log.logmethod import *
from second_test_method.base_method import *
from second_test_method.excel_method import *


#打印机管理
class Manage(unittest.TestCase):
    @classmethod          # 声明为类方法（必须）
    def setUpClass(cls):  # 类方法，注意后面是cls，整个类只执行一次
        cls.logger=logger(os.path.basename(__file__))
        cls.logger.debug('_______start_______')
        requestMethod().token(MustCode['appid'],MustCode['appkey'])

    @classmethod
    def tearDownClass(cls):
        cls.logger.debug('_______stop______')

    def test01(self):
        msg_ = frequentlyMethod.duQu_Excel(self, 'v2', '打印机管理', 1, 8)
        response=requestMethod().Post_registers('v2','打印机管理',1,4,3)
        self.logger.debug(response.text)
        self.logger.debug(response.url)
        self.assertEqual(msg_,response.json()['return_msg'])

    def test02(self):
        msg_=frequentlyMethod.duQu_Excel(self,'v2','打印机管理',2,8)
        response=requestMethod().Post_register('v2','打印机管理',2,4,3,2)
        self.logger.debug(response.text)
        self.logger.debug(response.url)
        self.assertEqual(msg_, response.json()['return_msg'])

    def test03(self):
        msg_=frequentlyMethod.duQu_Excel(self,'v2','打印机管理',3,8)
        response=requestMethod().Post_register('v2','打印机管理',3,4,3,2)
        self.logger.debug(response.text)
        self.logger.debug(response.url)
        self.assertEqual(msg_, response.json()['return_msg'])

    def test04(self):
        msg_=frequentlyMethod.duQu_Excel(self,'v2','打印机管理',4,8)
        response=requestMethod().Post_register('v2','打印机管理',4,4,3,2)
        self.logger.debug(response.text)
        self.logger.debug(response.url)
        self.assertEqual(msg_, response.json()['return_msg'])

    def test05(self):
        msg_=frequentlyMethod.duQu_Excel(self,'v2','打印机管理',5,8)
        response=requestMethod().Post_register('v2','打印机管理',5,4,3,2)
        self.logger.debug(response.text)
        self.logger.debug(response.url)
        self.assertEqual(msg_, response.json()['return_msg'])

    def test06(self):
        msg_=frequentlyMethod.duQu_Excel(self,'v2','打印机管理',6,8)
        response=requestMethod().Post_register('v2','打印机管理',6,4,3,2)
        self.logger.debug(response.text)
        self.logger.debug(response.url)
        self.assertEqual(msg_, response.json()['return_msg'])

    def test07(self):
        msg_=frequentlyMethod.duQu_Excel(self,'v2','打印机管理',7,8)
        response=requestMethod().Post_register('v2','打印机管理',7,4,3,2)
        self.logger.debug(response.text)
        self.logger.debug(response.url)
        self.assertEqual(msg_, response.json()['return_msg'])

    def test08(self):
        msg_=frequentlyMethod.duQu_Excel(self,'v2','打印机管理',8,8)
        response=requestMethod().Post_register('v2','打印机管理',8,4,3,2)
        self.logger.debug(response.text)
        self.logger.debug(response.url)
        self.assertEqual(msg_, response.json()['return_msg'])

    def test09(self):
        msg_=frequentlyMethod.duQu_Excel(self,'v2','打印机管理',9,8)
        response=requestMethod().Get_register('v2','打印机管理',9,4,3,2)
        self.logger.debug(response.text)
        self.logger.debug(response.url)
        self.assertEqual(msg_, response.json()['return_msg'])









#添加Suite
def suite():
     #定义一个单元测试容器
    suiteTest = unittest.TestSuite()
    suiteTest.addTest(Manage('test01'))
    suiteTest.addTest(Manage('test02'))
    return suiteTest

if __name__ == '__main__':
    '''我们在如果想要生成测试报告，那么一定要注意右键执行时选择的右键菜单，一定要当做文件执行，不要让编辑器当做用例执行'''
    #确定生成报告的路径
    pathCode = paths['上上一级'] + '\openyinmei\second_test_result\\'
    curtime = time.strftime('%Y%m%d%H%M%S', time.localtime())
    report_path = pathCode + curtime + 'test_case002'+'.html'
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
