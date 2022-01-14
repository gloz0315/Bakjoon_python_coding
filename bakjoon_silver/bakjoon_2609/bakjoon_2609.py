# 최대 공약수, 그리고 최소 공배수를 구하는 코드
# 정말 근본적인 코드이며 아주 간단하게 표현

import sys
A,B = map(int,sys.stdin.readline().split())
a,b = A,B

def gcd(num1,num2):
    while num2 != 0:
        num1,num2 = num2, num1%num2
    return num1

def lcm(num1,num2):
    return num1*num2 // gcd(num1,num2)

print(gcd(a,b))
print(lcm(a,b))


#혼자서 다른 코드를 for문을 통해 써봤는데..

num1, num2 = map(int,input().split())

lst = []
new_lst = []
for i in range(1,num1+1):
    if num1%i==0:
        lst.append(i)
for j in range(1,num2+1):
    if num2%j==0:
        if j in lst:
           new_lst.append(j)
num3 = num1/new_lst[-1]
num4 = num2/new_lst[-1]
print(new_lst[-1])
print(int(new_lst[-1]*num3*num4))

# 위의 근본적인 코드가 더 빠르며 길이도 더 짧다.
