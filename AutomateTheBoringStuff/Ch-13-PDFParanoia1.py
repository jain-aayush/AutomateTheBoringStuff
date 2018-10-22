"""
Using the os.walk() function from Chapter 9, write a script that will go through every
PDF in a folder (and its subfolders) and encrypt the PDFs using a password provided on
the command line. Save each encrypted PDF with an _encrypted.pdf suffix added to the
original filename. Before deleting the original file, have the program attempt to read
and decrypt the file to ensure that it was encrypted correctly. 
"""

import os, PyPDF2,sys
if(len(sys.argv) == 2):
    password = sys.argv[1]
else:
    print("Usage: python <filename>.py <password>")

filelocation = input("Enter the location where you want to encrypt PDF files\n")

print("Encrypting....")

for folderName, subfolders, filenames in os.walk(filelocation):
    for filename in filenames:
        if(filename.endswith('.pdf')):
            with open(os.path.join(folderName,filename), 'rb') as pdfFile:
                pdfReader = PyPDF2.PdfFileReader(pdfFile)
                pdfWriter = PyPDF2.PdfFileWriter()
                for pageNum in range(pdfReader.numPages):
                    pdfWriter.addPage(pdfReader.getPage(pageNum))
                pdfWriter.encrypt(password)
                newFilename = filename.replace('.pdf','_encrypted.pdf')
                with open(newFilename, 'wb') as resultPdf:
                    pdfWriter.write(resultPdf)
            with open(newFilename, 'rb') as pdfFile:
                pdfReader = PyPDF2.PdfFileReader(pdfFile)
                if(not pdfReader.isEncrypted):
                    print(newFilename + " was not encrypted successfully")
                else:
                    os.remove(os.path.join(folderName,filename))

print("Done!")