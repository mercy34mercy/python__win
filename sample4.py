from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import chromedriver_binary
import urllib.parse
import re
import json
import time
import pprint


INSTAGRAM_DOMAIN = "https://www.instagram.com/"
MIN_COUNT = 10

KEYWORD = "カメラ"

#tag_info取得.
def get_info_tag(text):
    soup = BeautifulSoup(text,features='lxml')
    tags = []
    try:
        #(xil3iに＃がある)
        elems = soup.find_all(class_ = 'xil3i')
        #print("elems",elems)
        for elem in elems:
            tag = elem.get_text()
            tags.append(tag)
            #print('繰り返しelem:',tag)
        return tags
    except:
        return None


# info取得
def get_info_from_text(text):
    soup = BeautifulSoup(text, features='lxml')
    try:
        info = {}
        id_ = []
        # 投稿（v1Nh3 kIKUG  _bz0w）
        elems = soup.find_all(class_="v1Nh3")
        #print("info_elems:",elems)
        for elem in elems:
            a_elem = elem.find("a")
            href = a_elem["href"]
            url = INSTAGRAM_DOMAIN + href
            post_id = get_search_value("\/p\/(.*)\/", href)

            #辞書からurlを引き出すためのid
            id_.append(post_id)

            # img情報
            img_elem = elem.find("img")
            alt = img_elem["alt"]
            src = img_elem["src"]

            post_dic = {}
            post_dic["url"] = url
            post_dic["alt"] = alt
            post_dic["src"] = src
            info[post_id] = post_dic


        return info,id_

    except:
        return None
 
def get_search_value(ptn, str):
      
    result = re.search(ptn, str)
      
    if result:
        return result.group(1)
    else:
        return None

def do_login(driver):
    # ログインURL
    login_url = 'https://www.instagram.com/' + "accounts/login/"
    driver.get(login_url)

    # 電話、メールまたはユーザー名のinput要素が読み込まれるまで待機（最大10秒）
    elem_id = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.NAME, "username"))
    )

    try:
        # パスワードのinput要素
        elem_password = driver.find_element_by_name("password")

        if elem_id and elem_password:
            # ログインID入力
            LOGIN_ID = 'etukobamasatyan34@gmail.com'

            elem_id.send_keys(LOGIN_ID)

            # パスワード入力
            PASSWORD = 'mashikotyan'
            elem_password.send_keys(PASSWORD)


            # ログインボタンクリック
            elem_btn = WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, '//*[@id="loginForm"]/div/div[3]/button'))
            )

            actions = ActionChains(driver)
            actions.move_to_element(elem_btn)
            actions.click(elem_btn)
            actions.perform()

            # 適当（3秒間待つように対応しています）
            time.sleep(3)

            # 遷移
            # 遷移後のURLでログイン可否をチェック
            perform_url = driver.current_url

            if perform_url.find(login_url) == -1:
                # ログイン成功
                return True
            else:
                # ログイン失敗
                return False

        else:
            return False
    except:
        return False 
     
if __name__ == '__main__':
     
    # url
    url = "https://www.instagram.com/explore/tags/" + urllib.parse.quote(KEYWORD) + "/"
 
    #　ヘッドレスモードでブラウザを起動
    options = Options()
    options.add_argument('--headless')
     
    # ブラウザーを起動
    driver = webdriver.Chrome()
    

    do_login(driver)

    driver.get(url)

    driver.implicitly_wait(10)  # 見つからないときは、10秒まで待つ
     
    html = driver.page_source
     
    json_str = get_search_value("window._sharedData = (.*);<\/script>", html)
     
    dict = json.loads(json_str)
    
    # for mykey in dict.keys():
    #     print(mykey)
    #     print(dict['entry_data']['TagPage'])
    #     print("\n\n")

    # print(dict['entry_data']['TagPage'])

    k = dict['entry_data']['TagPage']

    url = [d.get('data') for d in k]

     
    url2 = [s.get('top') for s in url]
    url3 = [r.get('sections') for r in url2]
    url4 = url3[0]
    url5 = [t.get('layout_content') for t in url4]
    url6 = [q.get('medias') for q in url5]
    url7 = url6[0]
    
    url8 = [i.get('media') for i in url7]
    url9 = [z.getall('image_versions2') for z in url8]
    url10 = [m.get('candidates') for m in url9]
    url11 = url10[0]
    url12 = [x.get('url') for x in url11]

    print(url12)

    # for mykey, myvalue in dict.items():
    #     print("key:" + mykey + ", values:" + myvalue)


    time.sleep(100)

    #pprint.pprint(dict, width=100)

