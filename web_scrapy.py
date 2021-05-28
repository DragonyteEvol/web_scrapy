from bs4 import BeautifulSoup
import requests
url=input("url:")
r=requests.get(url)
soup = BeautifulSoup(r.content,"lxml")
tags= soup("a")
for tag in tags:
    print(tag.get('href'))