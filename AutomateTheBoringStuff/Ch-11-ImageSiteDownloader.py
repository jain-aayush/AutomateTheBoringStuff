"""Write a program that goes to a photo-sharing site like Flickr or Imgur, searches for a 
category of photos, and then downloads all the resulting images. You could 
write a program that works with any photo site that has a search feature."""

import requests, os, bs4

base_url = "https://imgur.com/search?q="                                            #base url for downloading files from imgur

search = input("What do you want to search?\n")                                     #asking user what to search
os.makedirs("imgur", exist_ok = True)

res = requests.get(base_url+search)
res.raise_for_status()

soup = bs4.BeautifulSoup(res.text,"lxml")

imagelist = soup.find_all("img")                                                   #list of all the img tags
for image in imagelist:
    image_url ="http:" + image['src']                                              #getting image source
    res = requests.get(image_url)
    res.raise_for_status()
    imageFile = open(os.path.join('imgur',os.path.basename(image_url)), 'wb')
    for chunk in res.iter_content(10000):                                          #saving the image
        imageFile.write(chunk)
    imageFile.close()