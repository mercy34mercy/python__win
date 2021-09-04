import time                            # スリープを使うために必要
import requests
from bs4 import BeautifulSoup
import random
import re

def image(data):
    Res = requests.get("https://www.google.com/search?hl=jp&q=" + data + "&btnG=Google+Search&tbs=0&safe=off&tbm=isch")
    Html = Res.text
    Soup = BeautifulSoup(Html,'lxml')

    #kanrens = Soup.find_all('span')
    # kanrens = Soup.find_all()
    # kanren = Soup.find_all("span","hIOe2")
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

    ad = Soup.select(".PKhmud")
    print(ad)
    print(Html)


            

 




a = image('美女')






