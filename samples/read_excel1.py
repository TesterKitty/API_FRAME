import os
import xlrd
from common.excel_untils import ExcelUtils #导入类

excel_path=os.path.join(os.path.dirname(__file__),'data/test_data.xls')
excelUtils=ExcelUtils(excel_path,"Sheet1") #类实例化
#print(excelUtils.get_merged_cell_value(4,0))

#把表格内容转成字典（key、velue）塞到一个列表中
sheet_list=[] #列表
for row in range(1,excelUtils.get_row_count()):
    row_dict={} #字典，字典是Python中唯一内建的映射类型
    row_dict['事件'] = excelUtils.get_cell_value(row,0)
    row_dict['步骤序号'] = excelUtils.get_cell_value(row, 1)
    row_dict['步骤操作'] = excelUtils.get_cell_value(row, 2)
    row_dict['完成情况'] = excelUtils.get_cell_value(row, 3)
    sheet_list.append(row_dict)
#测试
#for row in sheet_list:
#    print(row)

#改进前一个方法
all_data_list=[]
first_row=excelUtils.sheet.row(0) #取出第一行的数据
print(first_row)
for row in range(1,excelUtils.get_row_count()):
    row_dict = {}
    for col in range(0,excelUtils.get_col_count()):
        row_dict[first_row[col].value]=excelUtils.get_cell_value(row,col)
        all_data_list.append(row_dict)
#测试
for row in all_data_list:
    print(row)