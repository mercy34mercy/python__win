import re
import time
import webbrowser as wb
import requests
from bs4 import BeautifulSoup

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

    # ランキング表示
    cnt = 0
    for ls in list:
        a = str(ls).strip('<div class="BNeawe vvjwJb AP7Wnd">')
        result_title = a.strip('</')
        print(str(cnt) + ":" + result_title)
        cnt = cnt + 1

    # Yahooは10件単位でしか取れないので10回まわす
    print("■Yahoo ランキング■")
    cnt = 0
    for i in range(10):
        # 10ランク取得
        pagenum = i * 10 + 1
        load_url = "https://search.yahoo.co.jp/search?p=ジョジョ+スタンド&ei=utf-8&b=" + str(pagenum)

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
                print(str(cnt) + ":" + result_title)
                cnt = cnt + 1

        time.sleep(1)