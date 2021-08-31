import time                            # スリープを使うために必要
import requests
from bs4 import BeautifulSoup
import random

def image(data):
    Res = requests.get("https://www.google.com/search?hl=jp&q=" + data + "&btnG=Google+Search&tbs=0&safe=off&tbm=isch")
    Html = Res.text
    Soup = BeautifulSoup(Html,'lxml')
    links = Soup.find_all("img")
    link = random.choice(links).get("src")

    return link

i = 0

for i in range(10): 
    a = image('river')
    print(a)
    i = i + 1


