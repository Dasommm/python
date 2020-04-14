#-*- coding:utf-8 -*-

from pymongo import MongoClient
import pprint
client = MongoClient('localhost',27017)
db = client.score
score = db.score

#국어점수가 50이 넘는 애들의 합
aggr = score.aggregate([
    {'$match':{'kor':{'$gt':50}}},
    {'$group':{'_id':'kor', 'sum':{'$sum':'$kor'}}}
])

print(aggr)
#cursor와 command_cursor의 다른점 => mongodb.com에서 doc -> pythonEdition에서 찾아보기
pprint.pprint(list(aggr))





















