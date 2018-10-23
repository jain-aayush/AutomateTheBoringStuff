"""
Say you have an encrypted PDF that you have forgotten the password to, 
but you remember it was a single English word. 
Trying to guess your forgotten password is quite a boring task. 
Instead you can write a program that will decrypt the PDF by trying every possible English word
until it finds one that works. This is called a brute-force password attack. 
Download the text file dictionary.txt from http://nostarch.com/automatestuff/. 
This dictionary file contains over 44,000 English words with one word per line.
You should try both the uppercase and lower-case form of each word. Print the hacked password.
"""

import PyPDF2

pdfFilename = input("Enter the name of the PDF File you want to decrypt:\n")

with open("dictionary.txt", 'r') as file:
    words = file.read().splitlines()                            #reading the lines and removing the trailing '\n'

with open(pdfFilename, 'rb') as pdfFile:
    pdfReader = PyPDF2.PdfFileReader(pdfFile)
    for word in words:
        if(pdfReader.decrypt(word)):
            print("Decrypted!")
            print("Password = %s" %word)
            break
        elif(pdfReader.decrypt(word.lower())):                  #trying lower-case words
            print("Decrypted!")
            print("Password = %s" %word.lower())
            break
    else:                                                       #password was not found
        print("Could Not Decrypt!")
        print("Password is not a dictionary term!")
