import requests
from bs4 import BeautifulSoup
from requests.api import get
import random
import re
import spacy

top_key = '美女'

def get_image(key):
    current_url = "https://www.google.com/search?q=" + key + \
        "&sxsrf=AOaemvI6vp0YKj-fyH9-T3r370jZUHhZgg:1630890428328&source=lnms&tbm=isch&sa=X&ved=2ahUKEwjCjpellOnyAhUGCYgKHUcEA_QQ_AUoAXoECAEQAw"
    html = requests.get(current_url)
    bs = BeautifulSoup(html.text, 'lxml')
    images = bs.find_all('img', limit=10)
    # for image in images:
    #     # print image source
    #     print(image['data-src'])

    url_list = []
    for index in range(len(images)-1):
        
        image = images[index+1]
        try:
            url = image.get("src")
            url_list.append(url)
        except:
            print("EOF")
    
    return url_list[random.randint(0,len(url_list)-1)]

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

    
    return result_title[random.randint(0,len(result_title)-1)]


def ginza(text_data):
    nlp = spacy.load('ja_ginza_electra')
    doc = nlp(text_data)

    for sent in doc.sents:
        for token in sent:
            if token.pos_ == 'NOUN':
                #url = get_image(top_key + token.orth_)
                return token.orth_
            #ここ直す

a = get_key(top_key)
b = ginza(a)
c = get_image(b)

print(c)
