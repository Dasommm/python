#-*- coding:utf-8 -*-
import requests
from bs4 import BeautifulSoup
import json

url = 'https://www.iei.or.kr'
resp = requests.get("https://iei.or.kr/intro/teacher.kh")
soup = BeautifulSoup(resp.text, 'html.parser')

#print(soup)

kh_list = soup.find('div',class_='intro_list')
#print(kh_list)

intro_list = kh_list.select('li');
#print(intro_list)

lst = list()

for chd in intro_list:
    kh_name = chd.find('p').text
    kh_image = chd.find('img').get('src')
    #print(kh_name, kh_image)
    
    tmp = {}
    tmp['name'] = kh_name
    tmp['image'] = url+kh_image
    lst.append(tmp)
    #print(lst)

res = {}
res['kh'] = lst
res_json = json.dumps(res, ensure_ascii=False)

print(res_json)

with open('khTeacher.json','w', encoding='utf-8') as file:
    file.write(res_json)


