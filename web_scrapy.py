from bs4 import BeautifulSoup
import requests
url=input("url:")
tag=input("tag:")
value=input("value:")
r=requests.get(url)
soup = BeautifulSoup(r.content,"lxml")
tags= soup(tag)
for tagg in tags:
    print(tagg.get(value))
