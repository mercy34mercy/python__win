from bs4 import BeautifulSoup
import requests
import json
import re

url = "https://www.instagram.com/c0c0tana/"

def get_json_data(url):

  res = requests.get(url)
  html = BeautifulSoup(res.content, 'html.parser')

  pattern = re.compile('window._sharedData = ({.*?});')
  script = html.find("script", text=pattern)
  data = pattern.search(script.text).group(1)
  json_user_data = json.loads(data)

  return(json_user_data)

json_data = get_json_data(url)

ig_user = json_data['entry_data']['ProfilePage'][0]['graphql']['user']
ig_user_username = ig_user['username']
ig_user_fullname = ig_user['full_name']
ig_user_followers = ig_user['edge_followed_by']['count']
ig_user_following = ig_user['edge_follow']['count']
ig_user_biography = ig_user['biography']

print('ユーザー名: '+ig_user_username)
print('フルネーム: '+ig_user_fullname)
print('フォロアー数: '+str(ig_user_followers))
print('フォロー数: '+str(ig_user_following))
print('紹介文: '+ig_user_biography)