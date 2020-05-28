#-*- coding:utf-8 -*-

# cmd 에 pip install requests

import requests
from bs4 import BeautifulSoup
import json



resp = requests.get('https://comic.naver.com/webtoon/weekdayList.nhn?week=wed')
soup = BeautifulSoup(resp.text, 'html.parser')

#print(soup)

webtoon_list = soup.find('ul',class_='img_list')
#print(webtoon_list)

dl = webtoon_list.select('dl')
print(dl)
lst = list()

for chd in dl:
    title = chd.find('a').text
    star = chd.find('strong').text
    #print(title, star)
    
    tmp = {}
    tmp['title'] = title
    tmp['star'] = star
    lst.append(tmp)
     
res = {}
res['webtoons'] =lst
res_json = json.dumps(res, ensure_ascii=False)    
    
    
print(res_json)
    
with open('webtoons.json', 'w', encoding='utf-8') as file:
    file.write(res_json)
    
    
    
    
    