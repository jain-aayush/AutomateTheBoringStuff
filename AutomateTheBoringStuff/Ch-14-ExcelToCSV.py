"""
Using the openpyxl module, write a program that reads all the Excel files in the current working directory
and outputs them as CSV files.
A single Excel file might contain multiple sheets; you’ll have to create one CSV file per sheet. 
The filenames of the CSV files should be <excel filename>_<sheet title>.csv, 
where <excel filename> is the filename of the Excel file without the file extension 
(for example, 'spam_data', not 'spam_data.xlsx') and 
<sheet title> is the string from the Worksheet object’s title variable.
"""

import os, openpyxl, csv

print("Converting...")

for file in os.listdir('.'):
    if(file.endswith('.xlsx')):
        wb = openpyxl.load_workbook(file)                                   #opening excel workbooks
        for sheets in wb.sheetnames:                                        #iterating every sheet in the workbook
            sheet = wb[sheets]
            sheetContent = []                                               #list storing all content of a sheet
            for row in range(1,sheet.max_row + 1):
                rowContent = []                                             #list storing all contents of a row
                for col in range(1,sheet.max_column + 1):
                    cellContent = sheet.cell(row=row, column=col).value
                    rowContent.append(cellContent)
                sheetContent.append(rowContent)
            excelFilename = file.replace('.xlsx', '_')
            csvFilename = excelFilename + sheets + ".csv"                   #csv file name creation
            with open(csvFilename, 'w') as csvFileObj:
                csvWriter = csv.writer(csvFileObj)
                for row in sheetContent:                                    #writing each row
                    csvWriter.writerow(row)

print("Done!")
