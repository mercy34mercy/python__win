import time                            # スリープを使うために必要
import requests
from bs4 import BeautifulSoup
import random
import re

def image(data):
    Res = requests.get("https://search.yahoo.co.jp/search?p=%E3%81%82%E3%81%84%E3%81%86%E3%81%88%E3%81%8A&fr=top_ga1_sa&ei=UTF-8&ts=4438&aq=-1&oq=&at=&ai=db0882f1-d8e1-4898-9732-8d47ea5cacf5")
    Html = Res.text
    Soup = BeautifulSoup(Html,'lxml')

    kanren = Soup.find_all('a')
    # kanrens = Soup.find_all()
    #kanren = Soup.select('Unit__listItem')
    #, class_="Unit__listItem"
    # #a = kanrens[2].contents[0]
    # kanren = random.choice(kanrens).get("aria-label")

    # links = Soup.find_all("img")
    # link = random.choice(links).get("src")



    # content = Soup.find_all("div",attrs={"class": "PKhmud"})
    # for ad_list in content:
    #for ad in Soup.select(".PKhmud"):
        # ad_link = ad['href']
        # ad_basics = ad['aria-label']
        #print(ad)

    # ad = Soup.select(".PKhmud")
    print(kanren)
    #print(Html)
    for elem in kanren:
        print(elem)


            

 

#<li class="Unit__listItem">




a = image('美女')






