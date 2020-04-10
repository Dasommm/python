#-*- coding:utf-8 -*-

from flask import Flask, render_template
from bs4 import BeautifulSoup
import requests
import json
#pip install flask_cors   => Cross Origin 정책
import flask_cors 
app = Flask(__name__)
flask_cors.CORS(app)

@app.route('/')
def root():
    return render_template('index.html')


@app.route('/crawling')
def crawling():
    #naver movie list를 crawling 해오자
    resp = requests.get('https://movie.naver.com/movie/running/current.nhn?order=reserve')
    soup = BeautifulSoup(resp.text, 'html.parser')
    
    movies = soup.find_all('dl', class_='lst_dsc')
    
    result = list()
    for movie in movies:
        title = movie.find('a').text
        star = movie.find('span',class_='num').text
        # movie.select('.num')[0].text
        #crawling 된 데이터를 dictionary[{movies:{title:제목, star: 별점},...}]로 저장하자
        tmp = dict()
        tmp['title'] = title
        tmp['star'] = star
        result.append(tmp)
    
    #json으로 변환하여 리턴하자
    res_dict ={'movies':result}
    api = json.dumps(res_dict, ensure_ascii=False)
    print(api)
    return api

if __name__ =='__main__':
    app.run('localhost',port='8585')