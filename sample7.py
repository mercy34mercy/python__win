import time                            # スリープを使うために必要
import requests
from bs4 import BeautifulSoup
import random
import re

import spacy

def syorii(data):
    nlp = spacy.load('ja_ginza_electra')
    doc = nlp(data)

    for sent in doc.sents:
        for token in sent:
            if token.pos_ == 'PROPN':
                print(token.orth_)
        


#-------------------------------------------------
## main ###
#-------------------------------------------------
if __name__=='__main__':

    # 100ランク取得
    load_url = "https://www.google.co.jp/search?hl=ja&source=hp&q=ジョジョ+スタンド&ie=utf-8&oe=utf-8&num=101"

    # HTML取得
    html = requests.get(load_url)
    web_data = BeautifulSoup(html.content, "html.parser")
    list = web_data.findAll(True, {'class': 'BNeawe vvjwJb AP7Wnd'})


    # Yahooは10件単位でしか取れないので10回まわす

    cnt = 1
    for i in range(3):
        # 10ランク取得
        pagenum = i * 10 + 1
        load_url = "https://search.yahoo.co.jp/search?p=美女&ei=utf-8&b=" + str(pagenum)

        # HTML取得
        html = requests.get(load_url)
        web_data = BeautifulSoup(html.content, "html.parser")
        list = web_data.findAll('a')

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

                result_title = a.strip('|')
                syorii(result_title)
                # print(str(cnt) + ":" + result_title)
                cnt = cnt + 1

        time.sleep(1)