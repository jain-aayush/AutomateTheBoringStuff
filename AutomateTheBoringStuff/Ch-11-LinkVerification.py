"""
Write a program that, given the URL of a web page, will attempt to download
every linked page on the page. The program should flag any pages that have
a 404 “Not Found” status code and print them out as broken links.
"""

import requests, bs4
url = input("Enter the URL\n")

res = requests.get(url)
res.raise_for_status()

soup = bs4.BeautifulSoup(res.text, "lxml")

a_tags = soup.select('a')                           #finding all <a> tags
false_links = []
for links in a_tags:
    href = links.get('href')                        #getting the href attribute from the tags
    page_url = "http:" + href
    try:
        res = requests.get(page_url)
        if(res.status_code == 404):                 #check for 404 error
            false_links.append(href)
    except:
        continue

if(false_links == []):
    print("All Links Are Verified")
else:
    print("The Following Links Don't Open")
    for links in false_links:
        print(links)