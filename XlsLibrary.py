import xlrd

class XlsLibrary:

    ROBOT_LIBRARY_SCOPE = 'TEST SUITE'

    def open_workbook(self, path_to_file):
        workbook = xlrd.open_workbook(path_to_file)
        return workbook

    def get_cell_value(self, workbook, sheet_name, row, column):
        workbook = workbook
        worksheet = workbook.sheet_by_name(sheet_name)
        cell_value = worksheet.cell_value(int(row), int(column))
        return cell_value
