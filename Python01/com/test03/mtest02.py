#-*- coding:utf-8 -*-

def func01(x, y):
    return x + y


def func02(x,y):
    return x+ y, x-y


def func03(x,y):
    print('파라미터로 %d, %d 두개의 숫자가 입력되었습니다.' % (x,y))
    print('{} 와 {}'.format(x, y))

if __name__ == "__main__":
    print(func01(1, 3))
    a, b = func02(4, 7)     #unpacking
    print(a,b)
    func03(6, 10)















