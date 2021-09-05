import xlrd
import os

excel_path=os.path.join(os.path.dirname(__file__),'data/test_data.xls')
#print(excel_path)
#excel_path='data/test_data.xlsx'
print(excel_path)
#创建工作簿对象
wb=xlrd.open_workbook( excel_path )
#创建表格对象
sheet=wb.sheet_by_name('Sheet1')
#取单元格内容
cell_value=sheet.cell_value(2,2)
#合并的单元格左上角首个单元格会返回真实值
cell_value=sheet.cell_value(1,0)
print(cell_value)

#xlrd中merged_cells属性
merged=(sheet.merged_cells) #返回表格中所有合并单元格的起始行列坐标
#逻辑： 凡是在merged_cells属性范围内的单元格，它的值都等于左上角首个单元格的值
def get_merged_cell_value(row_index,col_index):
    cell_value=None
    for (rlow,rhigh,clow,chigh) in merged: #python中for循环同时多个变量遍历列表
        if (row_index>=rlow and row_index<rhigh):
            if (col_index>=clow and col_index<chigh):
                cell_value=sheet.cell_value(rlow,clow)
    return cell_value
print(get_merged_cell_value(4,0))