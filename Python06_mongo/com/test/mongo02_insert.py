#-*- coding:utf-8 -*-

from pymongo import MongoClient

client = MongoClient('localhost',27017)
db = client.score
score = db['score']


res01 = score.insert_many([
    {
    'name' : 'You',
    'midterm':{'kor':100, 'eng':70, 'math':80},
    'final':{'kor':90, 'eng':40, 'math':100}    
    },
    {
    'name' : 'Moon',
    'midterm':{'kor':100, 'eng':70, 'math':80},
    }
])

print(res01.inserted_ids)



res02 = db.score.insert_one(
    {'name':'Sun', 'kor':100, 'eng':100}
)

print(res02.inserted_id)




