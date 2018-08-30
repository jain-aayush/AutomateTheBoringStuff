""" 
Write a function that takes a string and does the same thing as the strip()
string method. If no other arguments are passed other than the string to strip,
then whitespace characters will be removed from the beginning and end of the
string. Otherwise, the characters specified in the second argument to the
function will be removed from the string. 
"""
 
import re

def regex_strip(string,strip_string):
    if(strip_string == ''):
        leading_whitespaces = re.compile(r'^\s*')               #regex object for leading whitespaces
        trailing_whitespaces = re.compile(r'\s*$')              #regex object for trailing whitespaces
        new_string = leading_whitespaces.sub('', string)
        new_string = trailing_whitespaces.sub('', new_string)

    #.strip() in python removes any of the characters found in the string we pass.
    #According to the documentation, the chars argument is a set of characters to be removed.

    else:
        new_string = string
        for character in set(strip_string):                         
            charactersToRemove = re.compile(character)              #regex object for each unique character
            new_string = charactersToRemove.sub('',new_string)

    return new_string

#__main__
string = input("Enter string\n")
character = input("Enter character to remove\n")
print("Stripped String :" + regex_strip(string, character))
 