from bs4 import BeautifulSoup
import requests

r=requests.get("https://www.pokemon.com/el/")
soup = BeautifulSoup(r.content,"lxml")
tags= soup("a")
for tag in tags:
    print(tag.get('href'))