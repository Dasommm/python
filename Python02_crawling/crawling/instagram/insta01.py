#-*- coding:utf-8 -*-

from bs4 import BeautifulSoup
import requests

tag = input('search tag:')
url= 'https://www.instagram.com/explore/tags/'+tag

resp = requests.get(url)
soup = BeautifulSoup(resp.text, 'html.parser')

#print(soup)

results = soup.find('div', class_='KL4Bh')
print(results)

