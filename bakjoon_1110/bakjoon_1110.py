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
