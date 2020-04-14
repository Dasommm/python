#-*- coding:utf-8 -*-

#pip install pymongo

from pymongo import MongoClient

client = MongoClient('127.0.0.1', 27017)
db = client['score']
#db = client .score 형태로 가져올 수도 있다.
score = db['score']
#db = client.score

result = score.find()
for res in result:
    print(res)