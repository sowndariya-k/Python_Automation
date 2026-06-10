import openpyxl

def get_row_count(file, sheet):
    workbook = openpyxl.load_workbook(file)
    return workbook[sheet].max_row