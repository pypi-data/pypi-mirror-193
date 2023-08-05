import os
import glob
import win32com.client as win32


def remove_meta():
    excel = win32.gencache.EnsureDispatch("Excel.Application")
    excel.Visible = False
    excel.DisplayAlerts = False

    for file in glob.iglob("**/*.xls?", recursive=True):
        absolute_path = os.path.abspath(file)
        print("Working with file:", absolute_path)
        try:
            wb = excel.Workbooks.Open(absolute_path)
        except:
            print("Error occurred when tried to open file:", absolute_path)
            continue
        wb.RemovePersonalInformation = True
        wb.Save()
        wb.Close()

    excel.Quit()
