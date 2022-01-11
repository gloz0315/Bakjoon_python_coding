N = int(input())
num = N
cnt = 0
while True:
    a = num // 10
    b = num % 10
    c = (a+b) % 10
    num = (b*10) + c

    cnt += 1
    if (num == N):
        break
print(cnt)

# 단순하게 생각하자.
# while문을 통해서 각각의 값을 str로 생각하지말고 int형으로 생각해서 나머지 값과 몫 값을 따로 분리하면 된다.

다시 한번 푼 코드

N = int(input())
cnt = 0
num = N
while True:
    A = num//10
    B = num%10
    C = A+B
    num = B*10 + (C%10)
    cnt += 1
    if (num == N):
        break
print(cnt)

#num = N으로 num 값에 N을 대입해주며 while문 안에 N값을 집어넣는 것이 아닌 num값을 집어넣어야 돌아간다.
# ( 이건 좀 더 생각해보기로.. )
