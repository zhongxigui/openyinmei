import xlrd,pymysql,requests
from second_test_log.logmethod import *
import redis,random

class frequentlyMethod():
    def __init__(self):
        self.logger = logging.getLogger()

        '''excelb表格读取'''
    def duQu_Excel(self,ExcelName,Sheet,a,b):
        PathCode=os.path.dirname(os.path.dirname(__file__))+'/second_excel_case/'+ExcelName+'.xlsx'
        excel_Name = xlrd.open_workbook(PathCode)
        # 打开excel文件格式为xlsx有的是xls
        table = excel_Name.sheet_by_name(Sheet)
        cell_a1 = table.cell(a,b).value  # a代表行——从零开始   b代表列 从零开始
        return cell_a1


    @staticmethod
    def readToken():
        with open(paths['上一级']+'/second_test_method/token.txt','r')  as f:
            token=f.readlines()
        return token





