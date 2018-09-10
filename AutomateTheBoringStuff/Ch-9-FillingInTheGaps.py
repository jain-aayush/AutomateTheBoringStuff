"""
Write a program that finds all files with a given prefix, such as spam001.txt, spam002.txt,
and so on, in a single folder and locates any gaps in the numbering (such as if there is a
spam001.txt and spam003.txt but no spam002.txt). Have the program rename all the later files
to close this gap.
"""

import os, re

#regex for matching pattern. 3 groups - filename, sequence and extension
numberSequence = re.compile(r'^(\D*)(\d{1,})(.*)$')

def FindingSequentialFiles(folderLocation):
    regexGroup = []
    files = []
    #walking through the folder
    for folderName, subfolders, filenames in os.walk(folderLocation):
            for filename in filenames:
                match = numberSequence.search(filename)
                if(match):
                    matchedFile = []
                    address = os.path.join(folderName, filename)
                    #creating a list of the 3 groups of the matched regex object
                    regexGroup = [match.group(1),match.group(2),match.group(3)]
                    matchedFile.append(address)
                    matchedFile.append(regexGroup)
                    #files is thus a list of list
                    files.append(matchedFile)
                    

    return files

def FillingGaps(files, folderLocation):
    for i in range(len(files) - 1):
        #if the sequence differ by 1 and also the sequence are for the same file name
        #scam003 will not be renamed if a folder contains file001, and file002
        if(int(files[i][1][1]) - int(files[i+1][1][1]) != -1 and files[i][1][0] == files[i+1][1][0]):
            #creating the new file name
            newFileName = folderLocation + '/' + files[i][1][0]+ str(int(files[i][1][1]) + 1) + files[i][1][2]
            source = files[i+1][0]
            #changing the values in the list
            files[i+1][0] = newFileName
            files[i+1][1][1] = str(int(files[i][1][1]) + 1)
            os.rename(source, newFileName)
            print(source + " has been renamed!")

#__main__
folderLocation = input("Enter the Folder You want to Fill the Gaps in\n")
fileSequence = FindingSequentialFiles(folderLocation)

#sorting the list based on the sequence in their name
fileSequence = sorted(fileSequence, key = lambda x:int(x[1][1]))

FillingGaps(fileSequence, folderLocation)



