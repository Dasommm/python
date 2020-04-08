#-*- coding:utf-8 -*-

#def 함수명(파람){} 형식으로 메소드를 선언한다.

def func01():
    pass


def func02():
    print('함수02 입니다.')


def func03():
    return '함수03 입니다.'


def func04():
    return {1:'a',2:200}

if __name__ == '__main__':
    # main : 프로그램의 주 진입점
    print(func02())     #None => 아무것도 없다 
    str01 = func03()
    print(str01)
    print(func04()[1])





