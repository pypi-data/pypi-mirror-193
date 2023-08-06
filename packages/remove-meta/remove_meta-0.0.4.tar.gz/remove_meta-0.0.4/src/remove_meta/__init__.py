import glob
import os
import time
import win32com.client as win32


def remove_meta():
    excel = win32.gencache.EnsureDispatch("Excel.Application")
    excel.Visible = False
    excel.DisplayAlerts = False
    
    filetypes = ["**/*.xls", "**/*.xlsx", "**/*.xlsm"]

    for filetype in filetypes:
        for file in glob.iglob(filetype, recursive=True):
            absolute_path = os.path.abspath(file)
            print("Working with file:", absolute_path)
            try:
                wb = excel.Workbooks.Open(absolute_path)
                time.sleep(1)
            except:
                print("Error occurred when tried to open file:", absolute_path)
                continue
            wb.RemovePersonalInformation = True
            wb.Save()
            wb.Close()

    excel.Quit()
