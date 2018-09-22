"""
Write a program that takes an email address and string of text on the command
line and then, using Selenium, logs into your email account and sends an email
of the string to the provided address. (You might want to set up a separate email
account for this program.)
"""

import sys
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

user_email = input("Enter your Email Address")
user_pass = input("Enter your Password")
if(len(sys.argv) >= 3):                                                 #checking for command-line arguments
    receiver_email = sys.argv[1]
    message = sys.argv[2:]
    message = ' '.join(message)                                         #converting the message into a space-seperated string
else:
    receiver_email = input("Enter the Email Address of the Receiver")   #promting input when no arguments are passed
    message = input("What message do you want to send?")

driver = webdriver.Chrome()
driver.get("http://mail.google.com")

driver.implicitly_wait(20)                                              #waiting for page to load

email_field = driver.find_element_by_id("identifierId")
email_field.send_keys(user_email)

next_field = driver.find_element_by_id("identifierNext")
next_field.click()

password_field=driver.find_element_by_name("password")
password_field.send_keys(user_pass)
driver.implicitly_wait(10)

pass_next = driver.find_element_by_id("passwordNext")
pass_next.click()

composeMail_Elem = driver.find_element_by_link_text("Compose Mail")
composeMail_Elem.click()

to_Elem = driver.find_element_by_id("to")
to_Elem.send_keys(receiver_email)

body_Elem = driver.find_element_by_name("body")
body_Elem.send_keys(message)
driver.implicitly_wait(20)

send_Elem = driver.find_element_by_name("nvp_bu_send")
send_Elem.click()