#-*- coding:utf-8 -*-



n = input('n 입력 : ')
print(n)

a,b = 0,1
i = 0
while i <int(n):
    print(a, end=' ')
    a,b = b, a+b
    i += 1
print()


















def mysum(x, y):
    return 2 * x + y


print('------------')
lam1 = lambda x,y : 2*x+y
print(lam1)
print(lam1(2,4))
print('--------------')



hap01 = lambda a,b : a + b
print(hap01)
print(hap01(10,20))















def test(x):
    return x + 10
a = test(10)
print(a)

b = lambda x : x + 10
print(b(10))





gob = lambda a,b : a*b
print(gob(10,20))


hop02 = lambda a,b,c: a+b+c
print(hop02(3,4,5))


a =[(1,'one',9),(2,'two',8),(3,'three',7),(4,'four',6)]
a.sort(key=lambda a:a[1])
print(a)

min01 = (lambda x, y : x if x <y else y)(11, 22)
print(min01)


max01 = lambda x, y : x if x>y else y
print(max01(33,44))


b = lambda x: (lambda newx: x + newx)
c = b(100) # lambda newx: 100 + newx
d = c(90)  
print(d)
print(b(100)(90))

# 1~100사이의 숫자 중, 5의 배수만 출력하자
e = lambda x: bool(x % 5)
five = [i for i in range(1, 101) if not e(i)]
print(five)
# if not e(i)  -> i가 5의 배수이면 false반환 if not false -> if true

f = lambda x: x if (x % 5 != 0) else None
res = [i for i in range(1, 101) if not f(i)]
print(res)

result = [i for i in range(1, 101) if not (lambda x: x if (x % 5 != 0) else None)(i)]
print(result) 





