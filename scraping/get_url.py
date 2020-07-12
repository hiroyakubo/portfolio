"""
google検索で上位3サイトのurlを取得するスクリプト。
"""

import requests
from bs4 import BeautifulSoup

# 検索項目をlist_keywdに入力し、検索を実施.
list_keywd = ["python, download"]
result_num = 3
resp = requests.get('https://www.google.co.jp/search?num={}&q='.format(result_num) + '　'.join(list_keywd))

# 取得したHTMLをパースする.
soup = BeautifulSoup(resp.text, "lxml")

# 検索結果のサイトURLを取得
link_elem01 = soup.select('.kCrYT > a')
for l in link_elem01:
    print(l.get("href").replace("/url?q=", ""))