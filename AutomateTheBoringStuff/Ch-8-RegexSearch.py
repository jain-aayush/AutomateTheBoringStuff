"""
Write a program that opens all .txt files in a folder and searches for any line that
matches a user-supplied regular expression. The result should be printed to the screen
"""

import os, re, pprint


search_expression = input("Enter the expression you want to search:\n")
expression = re.compile(search_expression, re.I)

matched_searches = []
for filename in os.listdir(os.getcwd()):
    if(filename.endswith('.txt')):
        with open(filename, 'r') as file:
            lines = file.readlines()
            for line in lines:
                if(expression.search(line)):
                    matched_searches.append(line)

if(len(matched_searches) == 0):
    print("No results found!")

else:
    pprint.pprint(matched_searches)
