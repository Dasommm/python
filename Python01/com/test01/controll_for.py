#-*- coding:utf-8 -*-

subject = ['java','javascript', 'python']
for i in subject:
    print(i)
    
for i in subject:
    print(i, end=' ')
else:
    print('\n재밌다')  #모든 제어문에 else 붙일 수 있다. => 반복문에 else가 붙으면 반복문이 정상 종료 되었을 때, else의 명령을 수행한다. 

for i in range(1,100):
    print(i, end=', ')
else:
    print(100)

print('==========================')
print('<<구구단>>')
for i in range(2,10):
    print(str(i)+'단')
    for j in range(1,10):
        print(i,'*',j,'=',(i*j), sep=' ')
print()

print('==========================')
for i in range(10,0,-1):
    print(i)









