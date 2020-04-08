#-*- coding:utf-8 -*-

import pickle

score = {'name':'kh', 'kor':100, 'eng':40, 'math':60}
#객체를 파일에 저장

with open('test02.txt', 'wb') as file:
    pickle.dump(score, file)    # binary타입으로 저장

'''
pickling : 객체 -> 파일
unpickling : 파일 -> 객체
'''










