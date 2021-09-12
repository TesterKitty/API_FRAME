import os
import xlrd
class ExcelUtils():
    def __init__(self,file_path,sheet_name):
        self.file_path=file_path
        self.sheet_name=sheet_name
        self.sheet=self.get_sheet()  #把整个表格对象做成属性，后面使用方便

    def get_sheet(self):
        wb=xlrd.open_workbook(self.file_path)
        sheet=wb.sheet_by_name(self.sheet_name)
        return sheet

    def get_row_count(self):
        row_count=self.sheet.nrows
        return row_count

    def get_col_count(self):
        col_count=self.sheet.ncols
        return col_count

    def get_cell_value(self,row_index,col_index):  #不常用的方法可以加双下划线私有化命名
        cell_value=self.sheet.cell_value(row_index,col_index)
        return cell_value

    def get_merged_info(self):
        merged = self.sheet.merged_cells
        return merged

    def get_merged_cell_value(self,row_index, col_index):
        cell_value = None
        for (rlow, rhigh, clow, chigh) in self.get_merged_info():
            if (row_index >= rlow and row_index < rhigh):
                if (col_index >= clow and col_index < chigh):
                    cell_value = self.get_cell_value(rlow, clow)
                    break;
                else:
                    cell_value = self.get_cell_value(row_index, col_index)
            else:
                cell_value = self.get_cell_value(row_index, col_index)
        return cell_value
    #将表格数据转成字典，塞到一个list中
    def get_sheet_data_by_dict(self):
        all_data_list = []
        first_row = self.sheet.row(0)  # 取出第一行的数据
        for row in range(1, self.get_row_count()):
            row_dict = {}
            for col in range(0, self.get_col_count()):
                row_dict[first_row[col].value] = self.get_merged_cell_value(row, col)
            all_data_list.append(row_dict)
        return all_data_list

#测试代码
if __name__=='__main__':
    current_path=os.path.dirname(__file__)
    excel_path=os.path.join(current_path,'..','samples/data/test_case.xlsx')
    excelUtils=ExcelUtils(excel_path,"Sheet1") #类实例化
    #print(excelUtils.get_merged_cell_value(4,0))
    print(excelUtils.get_merged_cell_value(4,0))
    for i in excelUtils.get_sheet_data_by_dict():
        print(i)
