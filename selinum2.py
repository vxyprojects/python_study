# excel example

# import win32com.client
#
# excel = win32com.client.Dispatch("Excel.Application")
# excel.Visible = True
# wb = excel.Workbooks.Add()
# ws = wb.Worksheets("Sheet1")
# ws.Cells(1, 1).Value = "hello world"
# wb.SaveAs('c:\\Users\\Jason\\Desktop\\test.xlsx')
# excel.Quit()




from openpyxl import Workbook
import time

book = Workbook()
sheet = book.active

sheet['A1'] = 56
sheet['A2'] = 43

now = time.strftime("%x")
sheet['A3'] = now

book.save("sample.xlsx")