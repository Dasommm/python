#-*- coding:utf-8 -*-

'''
*
**
***
****
*****
'''
for i in range(1,6):
    print('*'*i)

print('----------------')

print('\n'.join([''.join(['*' for i in range(i+1)])for i in range(5)]))

print('----------------')

'''
*****
****
***
**
*
'''
for i in range(5,0,-1):
    print('*'*i)

print('----------------')
'''
    *
   **
  ***
 ****
*****
'''
for i in range(1,6):
    print('o'*(5-i),'*'*i,sep='')
    
print('----------------')
'''
*****
 ****
  ***
   **
    *
'''
for i in range(5,0,-1):
    print('o'*(5-i),'*'*i,sep='')

print('----------------')
'''
    *
   ***
  *****
 *******
*********
'''
for i in range(1,6):
    print('o'*(5-i),'*'*i,sep='')



