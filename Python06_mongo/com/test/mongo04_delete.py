#-*- coding:utf-8 -*-

from pymongo import MongoClient

client = MongoClient('localhost',27017)
db = client['score']
score = db.score

res01 = score.delete_one({'name':'유재석'})
print(res01.deleted_count)


res02 = score.delete_many(
    {'midtetm.math':{'$gte':60}}
)

print(res02.deleted_count)


#score.delete_many({}) => 도큐먼트 전체 삭제











