import time                            # スリープを使うために必要
import requests
from urllib import request
import json
import re
from bs4 import BeautifulSoup
# Webブラウザを自動操作する（python -m pip install selenium)
from selenium import webdriver
import chromedriver_binary


# driver = webdriver.Chrome()            # Chromeを準備
# get_text = driver.get('https://www.instagram.com/explore/tags/%E7%BE%8E%E5%A5%B3/')  # Googleを開く

url = 'https://www.google.com/search?q=%E9%87%8E%E7%90%83&sxsrf=AOaemvKYx2eaAlxFEqVFPKptbH7n9Eg7Qw:1630424889589&source=lnms&tbm=isch&sa=X&ved=2ahUKEwi-pIGDztvyAhVLzmEKHTawCZMQ_AUoAXoECAEQAw&biw=2048&bih=1010'

res = requests.get(url)
html = BeautifulSoup(res)

# script = html.find_all('div', 'v1Nh3')

print(html)

res.close()

# soup = BeautifulSoup(get_text.toString, 'lxml')
# slist = soup.find_all("div", class_="v1Nh3 KIKUG _bz0w")
time.sleep(15)                          # 5秒間待機
# driver.quit()                          # ブラウザを閉じる
