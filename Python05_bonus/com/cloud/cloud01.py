#-*- coding:utf-8 -*-

#하얀색 배경의 사진
#pip install wordcloud
#error: Microsoft Visual C++ 14.0 is required. Get it with "Microsoft Visual C++ Build Tools": https://visualstudio.microsoft.com/downloads/


#window-> preferences-> python interpreter -> 
#프로젝트 우클릭-> properties -> pyDev-interpreter/Grammar -> interpreter를  새로추가한 path로 바꾸고, grammar는 3.7
from wordcloud import WordCloud
import json

cloud = WordCloud(font_path="Goyang.ttf", backgroud_color ='white', max_words=30, width=400, height=300)


with open('webtoons.json') as file:
    webtoon = json.load(file)
    

res = dict()
for tmp in webtoon ['webtoons']:
    res[tmp['title']] = int(float(tmp['star']) * 100)
    # {'유미의 세포들':980}

visual = cloud.fit_word(res)
visual.to_image()
visual.to_file('cloud.png')














