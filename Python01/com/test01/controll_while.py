#-*- coding:utf-8 -*-

i = 1
while i <= 10:
    print(i)
    i += 1
    #python에는 i++ 없다
    
mysum = 0
mycount = 1
while mycount <= 10:
    mysum += mycount
    mycount += 1
else:
    print('sum', mysum, sep=':')
    print('cnt',mycount, sep=':')