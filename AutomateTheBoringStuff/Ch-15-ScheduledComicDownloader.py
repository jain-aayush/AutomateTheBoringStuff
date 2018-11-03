"""
Write a program that checks the websites of several web comics and automatically downloads the images 
if the comic was updated since the program’s last visit.
"""

import time, requests, bs4, os

os.makedirs("Comics", exist_ok = True)

baseURL = "http://buttersafe.com/"

print("Checking %s..." %baseURL)
res = requests.get(baseURL)
res.raise_for_status()
    
soup = bs4.BeautifulSoup(res.text, "lxml")
image_url = soup.find("div" , {"id" : "comic"}).img['src']

if(image_url.startswith("http:/") == False):
    image_url = "http:/" + image_url

res = requests.get(image_url)
res.raise_for_status()
filePath = os.path.join("Comics", os.path.basename(image_url))

if(os.path.isfile(filePath)):                                                     #if the file is already downloaded, no new comics have come
    print("No new Comics")
    exit()

with open(filePath, 'wb') as imageFile:
    print("Saving Comic..")
    for chunk in res.iter_content(10000):                                          #saving the image
        imageFile.write(chunk)
