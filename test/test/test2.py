#-*- coding:utf-8 -*-


n = input('숫자를 입력해주세요 ')   
print(n)
a,b = 0,1
i = 0
while i <int(n):
    print(a)
    a,b = b, a+b
    i += 1
    
    

def fibo1(n):
    a,b = 0,1
    i=0
    while i <int(n):
        print(a)
        a=b
        b=a+b
        i += 1
        


n = input('숫자를 입력해주세요 ')   
print(n)
a,b = 0,1
i = 0
lst = list()
while i <int(n):
    lst.append(a)
    a,b = b, a+b
    i += 1


def fibo2(n):
    a,b = 0,1
    i = 0
    lst = list()
    while i <int(n):
        lst.append(i) = a
        a,b = b, a+b
        i += 1
        
        
        
if __name__ == '__main__':
    n = input('숫자를 입력하세요:')
    fibo1(n)
    fibo2(n)


