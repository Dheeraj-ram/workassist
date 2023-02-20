from xlwt import Workbook
import csv

import xlsxwriter
from tkinter.filedialog import asksaveasfile
  
f=asksaveasfile(initialfile='errors.xls',filetypes=[("All Files","*.*")])
workbook = Workbook(f) 
sheet1=workbook.add_sheet('Sheet 1')

 
# Use the worksheet object to write
# data via the write() method.
sheet1.write(0,0, 'Hello..')
sheet1.write(1,0, 'Geeks')

 


