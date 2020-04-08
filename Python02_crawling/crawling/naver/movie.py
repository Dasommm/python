#-*- coding:utf-8 -*-
from bs4 import BeautifulSoup

#cmd에서 pip install beautifulsoup4

import urllib.request

resp = urllib.request.urlopen('https://movie.naver.com/movie/running/current.nhn')
soup = BeautifulSoup(resp, 'html.parser')

#print(soup)
movies = soup.find_all('dl',class_='lst_dsc')
#print(movies)

for movie in movies:
    title = movie.find('a').text
    review = movie.find('span',class_='num').text
    print("{} [{}]".format(title, review))
