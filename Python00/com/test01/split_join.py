#split
str01 = 'Hello, World!\nHello, Python!'
print(str01)

arr01 = str01.split(' ')
print(arr01)

arr02 = str01.split(' ',1)  # 뒤의 숫자는 몇번 자를건지
print(arr02)

import re
arr03 = re.split('[\s]|[,]',str01) # ,이거나 공백을 기준으로 잘린다
print(arr03)

#join
arr04 = ['1','2','3','4']
print(arr04)
print(eval('+'.join(arr04)))


















