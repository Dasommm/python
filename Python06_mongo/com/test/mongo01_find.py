#-*- coding:utf-8 -*-

from pymongo import MongoClient
import pprint

client=MongoClient('localhost',27017)
db = client.score
score= db.score

cursor = score.find()
print(cursor)
for doc in cursor:
    pprint.pprint(doc)


print("----------------")

hong = score.find({'name':'홍길동'})
pprint.pprint(hong) #cursor로 값이 뜬다.

for doc in hong:
    print(doc)


cho = score.find_one({'name':'조세호'})
pprint.pprint(cho)


print('-------------')

print('document의 총 갯수 : ', score.count_documents({}))


#국어점수가 70보다 높은 사람만 출력하자
kor70 = score.find({'kor':{'$gt':70}})
print(kor70)
for doc in kor70:
    print(doc)















