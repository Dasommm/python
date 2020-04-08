#산술 연산

a = 21
b =2
print(a+b)
print(a-b)
print(a*b)
print(a**b)
# a의 b제곱
print(a/b)
print(a//b)
#몫 (Floor division)
print(a%b)
#나머지

#비교연산
a,b = 5,3
print(a == b)
print(a != b)
print(a > b)
print(a <= b)
print("========")
print(a is b)
print(a is not b)
print("========")
print(True or False)
print(False and True)
print(not False)
print("========")

#범위 연산
#[start : end] => start ~ end-1
#[start : end : step] => start, start+step, ..., end-1
list01 = list(range(100))   #0~99까지 
print(list01)
print(list01[2])
print(list01[12:49])    #12~48까지
print(list01[12:49:3])  #3씩 증가하면서 12~48까지

str01 = 'Hello, World!'
print(str01)
print(str01[0:5])
print(str01[7:12])

#reverse
print(str01[-1])
print(str01[:-1])
print(str01[::-1])

#멤버연산
list02 = [0,1,2,3,4]
print(3 in list02)
print(5 not in list02)
print(4 not in list02)







