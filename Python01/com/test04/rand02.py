#-*- coding:utf-8 -*-

#로또 만들기
import random

def lotto():
    lotto = set()
    while len(lotto) <= 6:
        ran = random.randint(1,45)
        lotto.add(ran)
    #print(list(lotto))
    lst = sorted(lotto)
    print(lst)

if __name__ == '__main__':
    lotto()    

    















