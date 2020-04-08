#-*- coding:utf-8 -*-

def ant(i):
    pass


if __name__ == '__main__':
    n = int(input('ant stage : '))
    val = ant(1)
    
    print('1')
    for i in range(1,n):
        val = ant(val)
        print(val)




















