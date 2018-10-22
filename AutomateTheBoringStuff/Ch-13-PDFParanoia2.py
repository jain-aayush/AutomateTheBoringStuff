"""
Write a program that finds all encrypted PDFs in a folder (and its subfolders)
and creates a decrypted copy of the PDF using a provided password. If the password
is incorrect, the program should print a message to the user and continue to the next
PDF.
"""
import os, PyPDF2

filelocation = input("Enter the location where you want to decrypt pdf files\n")

for folderName, subfolders, filenames in os.walk(filelocation):
    for filename in filenames:
        if(filename.endswith('.pdf')):
            pdfFilename = os.path.join(folderName,filename)
            with open(pdfFilename, 'rb') as pdfFile:
                pdfReader = PyPDF2.PdfFileReader(pdfFile)
                if(pdfReader.isEncrypted):
                    print("Enter password for the file: %s" %pdfFilename)
                    password = input()
                    if(pdfReader.decrypt(password)):
                        pdfWriter = PyPDF2.PdfFileWriter()
                        for pageNum in range(pdfReader.numPages):
                            pdfWriter.addPage(pdfReader.getPage(pageNum))
                        newFilename = filename.replace('.pdf','_decrypted.pdf')
                        with open(newFilename, 'wb') as resultPdf:
                            pdfWriter.write(resultPdf)
                    else:
                        print("Wrong Password!")