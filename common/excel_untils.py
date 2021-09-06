import xlrd
class ExcelUtils():
    def __init__(self,file_path,sheet_name):
        self.file_path=file_path
        self.sheet_name=sheet_name

    def get_sheet(self):
        wb=xlrd.open_workbook(self.file_path)