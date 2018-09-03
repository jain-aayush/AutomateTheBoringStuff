"""
Create a Mad Libs program that reads in text files and lets users add their own text anywhere
the contents ADJECTIVE, NOUN, ADVERB, or VERB appears in the text file.
"""

import re

with open('madlibs.txt', 'r') as file1:                     #opens a file named madlibs.txt(create beforehand)
    contents = file1.read()

#creating regex objects for various parts of speech
adjective = re.compile(r'ADJECTIVE')
noun = re.compile(r'NOUN')
adverb = re.compile(r'ADVERB')
verb = re.compile(r'VERB')

while(contents):
    if(adjective.search(contents)):
        substitute = input("Enter an adjective:\n")
        contents = adjective.sub(substitute, contents, 1)
    elif(noun.search(contents)):
        substitute = input("Enter a noun:\n")
        contents = noun.sub(substitute, contents, 1)
    elif(adverb.search(contents)):
        substitute = input("Enter an adverb:\n")
        contents = adverb.sub(substitute, contents, 1)
    elif(verb.search(contents)):
        substitute = input("Enter a verb:\n")
        contents = verb.sub(substitute, contents, 1)
    else:
        break

print("The new file reads as follows")
print(contents)

with open('new_madlibs.txt', 'w') as file2:
    file2.write(contents)
    
    
