"""
Create a program blankRowInserter.py that takes two integers and a filename string as command 
line arguments. Let’s call the first integer N and the second integer M. 
Starting at row N, the program should insert M blank rows into the spreadsheet.
"""

import sys, openpyxl
                                                                    #storing values
n = int(sys.argv[1])
m = int(sys.argv[2])
spreadsheet = sys.argv[3]
                                                                    #opening workbooks
wb = openpyxl.load_workbook(filename = spreadsheet)                 
sheet = wb.active
new_wb = openpyxl.Workbook()
new_sheet = new_wb.active

max_row = sheet.max_row
max_col = sheet.max_column
                                                                    #copying contents till the nth row
for col in range(1,max_col+1):
    for row in range(1,n+1):
        new_sheet.cell(row = row, column= col).value = sheet.cell(row = row, column= col).value
                                                                    #adding a blank row = moving contents from
                                                                    #that row to (n+m)th row 
for col in range(1, max_col+1):
    for row in range(max_row, n, -1):
        new_sheet.cell(row = row+m, column = col).value = sheet.cell(row = row, column= col).value
                                                                    #saving in the same spreadsheet 
new_wb.save(spreadsheet)
