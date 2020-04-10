#-*- coding:utf-8 -*-


def factorial():
    res = 1
    for i in range(1, n+1):
        res *= i
    return res


def factorialRecursion(n):
    # 재귀함수
    if n == 1:
        return 1
    return n * factorialRecursion(n-1)


if __name__ == '__main__':
    n = int(input('n : '))
    res = factorialRecursion(n)
    print('{} factorial = {}'.format(n,res))
    print('{} factorial = {}'.format(n,factorial(n)))








