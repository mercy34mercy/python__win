from sample6 import image
import requests
from bs4 import BeautifulSoup
from requests.api import get
import spacy
import time
import re
import random

url_list = []


def get_key(top_key):
    # 100ランク取得
    load_url = "https://www.google.co.jp/search?hl=ja&source=hp&q=" + \
        top_key+"&ie=utf-8&oe=utf-8&num=101"

    # HTML取得
    html = requests.get(load_url)
    web_data = BeautifulSoup(html.content, "html.parser")
    list = web_data.findAll(True, {'class': 'BNeawe vvjwJb AP7Wnd'})

    for i in range(1):
        # 10ランク取得
        pagenum = 1
        load_url = "https://search.yahoo.co.jp/search?p="+top_key + "&ei=utf-8&b=" + \
                str(pagenum)

        # HTML取得
        html = requests.get(load_url)
        web_data = BeautifulSoup(html.content, "html.parser")
        list = web_data.findAll('a')

        # 獲得したテキストから、indexを作成
        result_title = []
 

        pattern = "(.*)clear.gif(.*)"
        # ランキング表示
        for ls in list:
            if str(ls).find('clear.gif') != -1:
                d = re.search(pattern, str(ls))
                a = d.group(2)
                a = a.replace("<b>", "")
                a = a.replace("</b>", "")
                a = a.replace(""""""">", "")
                a = a.replace("</a", "")

                result_title.append(a.strip('|'))

        

        syorii(result_title[random.randint(0,len(result_title))], top_key)
        time.sleep(1)
                


def syorii(text_data, top_key):
    nlp = spacy.load('ja_ginza_electra')
    doc = nlp(text_data)

    index = 0

    for sent in doc.sents:
        for token in sent:
            if token.pos_ == 'NOUN':
                get_image(top_key + token.orth_)
                break


def get_image(key):
    current_url = "https://www.google.com/search?q=" + key + \
        "&sxsrf=AOaemvI6vp0YKj-fyH9-T3r370jZUHhZgg:1630890428328&source=lnms&tbm=isch&sa=X&ved=2ahUKEwjCjpellOnyAhUGCYgKHUcEA_QQ_AUoAXoECAEQAw"
    html = requests.get(current_url)
    bs = BeautifulSoup(html.text, 'lxml')
    images = bs.find_all('img', limit=10)
    # for image in images:
    #     # print image source
    #     print(image['data-src'])

    for index in random.randint(1,len(images)):

        image = images[index]
        try:
            url = image.get("src")
            print(url)
            break
        except:
            print("EOF")


key_data = "美女"
# get_image(key_data)
get_key(key_data)
