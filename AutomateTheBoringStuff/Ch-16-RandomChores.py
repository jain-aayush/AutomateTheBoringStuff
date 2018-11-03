"""
Write a program that takes a list of people’s email addresses and 
a list of chores that need to be done and randomly assigns chores to people.
Email each person their assigned chores. 
If you’re feeling ambitious, keep a record of each person’s previously assigned chores so that you 
can make sure the program avoids assigning anyone the same chore they did last time. 
For another possible feature, schedule the program to run once a week automatically.
"""

import smtplib, random

emails = [x for x in input("Enter the emails - ").split()]                      #taking inputs in one line
chores = [x for x in input("Enter the chores - ").split()]

if(len(emails) > len(chores)):
    print("There are more people than the chores available")
    print("Remove %d emails" %(len(emails) - len(chores)))
    exit()

prev_assigned = {}                          

choice = input("Do you want to enter the previous tasks of the given emails? ") #storing previous assigned tasks
if(choice.lower() == 'y'):
    for email in emails:
        prev_assigned[email] = input("Enter the task for %s\n" % email)

assigned = {}

for email in emails:
    chore = random.choice(chores)
    if(len(prev_assigned)):
        while(chore == prev_assigned[email]):
            chore = random.choice(chores)
    assigned[email] = chore
    chores.remove(chore)

smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
smtpObj.ehlo()
smtpObj.starttls()

yourEmail = input("Enter your email address\n")
password = input("Enter your password\n")

try:
    smtpObj.login(email, password)
    for email, chore in assigned.items():
        message = "Subject: Chores\nHello,\nYou have been assigned to complete %s chore" % chore
        smtpObj.sendmail(yourEmail, email, message)

except smtplib.SMTPAuthenticationError:
    print("Incorrect Email-Password Pair")