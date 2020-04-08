#-*- coding:utf-8 -*-

def ant(i):
    for a in inp:
        if a == target:
            cnt += 1
        else:
            res += target + str(cnt)
            


if __name__ == '__main__':
    print('1')
    n = int(input('ant stage :'))
    val = ant(1)
    print('1')
    print(val)
    for i in range(1,n):
        val = ant(val)
        print(val)




















