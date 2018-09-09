"""
Write a program that walks through a folder tree and searches for files with a
certain file extension. Copy these files from whatever location they are in to a new folder.
"""

import shutil, os

def filesCopy(folderLocation, extension, destination):
    folderLocation = os.path.abspath(folderLocation)
    for folderName, subfolders, filenames in os.walk(folderLocation):           #walking through the folder tree
            for filename in filenames:
                if(filename.endswith(extension)):
                    source = os.path.join(folderName, filename)
                    shutil.copy(source, destination)                            #copying the file

#__main__
folderLocation = input("Enter the location from where you want to copy\n")
extension = input("Enter the extension of the files\n")
destination = input("Enter the place where you want to copy the files\n")

print("The files are copied to a new folder named - "+ "Extension_Copy" )
destination = destination + "/" + "Extension_Copy"                             #naming the destination folder
try:
    os.makedirs(destination)                                                   #making the directory
except FileExistsError:
    print("Folder already Exists")
    
filesCopy(folderLocation, extension,destination)
                    

