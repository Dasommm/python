#-*- coding:utf-8 -*-

#하얀색 배경의 사진
#pip install wordcloud
#error: Microsoft Visual C++ 14.0 is required. Get it with "Microsoft Visual C++ Build Tools": https://visualstudio.microsoft.com/downloads/


#window-> preferences-> python interpreter -> 
#프로젝트 우클릭-> properties -> pyDev-interpreter/Grammar -> interpreter를  새로추가한 path로 바꾸고, grammar는 3.7
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np
import json


with open('webtoons.json', encoding='utf-8') as file:
    webtoon = json.load(file)
    

res = dict()
for tmp in webtoon ['webtoons']:
    res[tmp['title']] = int(float(tmp['star']) * 100)
    # {'유미의 세포들':980}

masking_img = np.array(Image.open('kakao.png'))
cloud = WordCloud(font_path='Goyang.ttf',
                  max_font_size=40,
                  mask=masking_img,
                  background_color='white').fit_words(res)
cloud.to_file('result.png')

plt.imshow(cloud, interpolation='bilinear')
plt.axis('off')
plt.show()













