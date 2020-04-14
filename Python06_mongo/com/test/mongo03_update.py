#-*- coding:utf-8 -*-

from pymongo import MongoClient

client = MongoClient('localhost',27017)
db = client.score
score = db.score
#유재석을 찾아서 국어를 100점으로 바꾸자

res01 = score.update_one(
    {'name': '유재석'},
    {
        '$set':{'kor':100}
    }
)

print(res01.matched_count)
print(res01.modified_count)



res02=score.update_many(
    {'eng':{'$lt':80}},
    {'$set':{'eng':0}}
)

print(res02.matched_count)
print(res02.modified_count)





