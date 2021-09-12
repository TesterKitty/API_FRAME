import os
from common.excel_untils import  ExcelUtils

current_path=os.path.dirname(__file__)
test_data_path=os.path.join(current_path,'..','test_data/test_case.xlsx')

class TestdataUtils():
    def __init__(self,test_data_path=test_data_path):
        self.test_data_path=test_data_path
        self.test_data=ExcelUtils(test_data_path,'Sheet1').get_sheet_data_by_dict() #直接把表格数据拿过来做成属性使用

    #把表格数据转成目标字典格式，用例编号相同的行数据处理为一条字典数据
    def __get_testcase_data_dict(self):
        test_case_dict={}
        for row_data in self.test_data:
            #setdefault:如果字典中包含有给定键，则返回该键对应的值，否则返回为该键设置的值。
            test_case_dict.setdefault(row_data['测试用例编号'],[]).append(row_data)
        return test_case_dict

    #把字典转成目标列表格式
    def def_testcase_list(self):
        testcase_list=[]
        for k, v in self.__get_testcase_data_dict().items():
            one_case_dict = {}
            one_case_dict['case_name'] = k
            one_case_dict['case_info'] = v
            testcase_list.append(one_case_dict)
        return testcase_list

    #__get_testcase_data_dict为私有方法，私有方法不能直接调用，必须构造另一个函数来调用私有方法
    # def test(self):
    #     print(self.__get_testcase_data_dict())

if __name__=='__main__':
    testdataUtils = TestdataUtils()
    #testdataUtils.test()
    print(testdataUtils.def_testcase_list())