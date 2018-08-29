"""
Write a function that uses regular expressions to make sure the password
string it is passed is strong. A strong password is defined as one that
is at least eight characters long, contains both uppercase and lowercase
characters, and has at least one digit. You may need to test the string
against multiple regex patterns to validate its strength.

"""
import re
def passStrength(password):
    passLength = re.compile(r'(\S){8,}')
    upper = re.compile(r'[A-Z]')
    lower = re.compile(r'[a-z]')
    digits = re.compile(r'(\d)')
    if(passLength.search(password) == None):
        print("Password Too Short!")
    elif(upper.search(password) == None):
        print("No Upper Case Characters In The Password!")
    elif(lower.search(password) == None):
        print("No Lower Case Characters In The Password!")
    elif(digits.search(password) == None):
        print("No Digits Used In The Password!")
    else:
        print("Your Password Is Strong")

#__main__
password = input("Enter Your Password to Check its Strength ")
passStrength(password)

