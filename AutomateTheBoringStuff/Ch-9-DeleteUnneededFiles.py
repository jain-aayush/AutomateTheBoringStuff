"""
Write a program that walks through a folder tree and searches for exceptionally
large files or folders—say, ones that have a file size of more than 100 MB.
Print these files with their absolute path to the screen.
"""


import os

def filesToDelete(folderLocation, minSize):
    folderLocation = os.path.abspath(folderLocation)
    delFiles = {}
    for folderName, subfolders, filenames in os.walk(folderLocation):
            for filename in filenames:
                fileAddress = os.path.join(folderName, filename)
                if(os.path.getsize(fileAddress) > minSize):
                    delFiles[os.path.abspath(fileAddress)] = os.path.getsize(fileAddress)
    return delFiles

#__main__

folderLocation = input("Enter the Path from where you want to Delete Files\n")
minSize = int(input("Enter the accepted size of file in MB\n"))
delFiles = filesToDelete(folderLocation, minSize * 1000000)
for address, size in delFiles.items():
    print("Press 1 if you want to delete " + address + " of size = " + str(size))
    ch = input()
    if(ch == 1):
        os.unlink(address)
        print("File Permanetly Deleted")
