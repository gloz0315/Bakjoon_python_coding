N = int(input())
A = list(map(int,input().split()))
Y = M = 0
for i in range(N):
    Y += (i//30 + 1)*10
    M += (i//60 + 1)*15

if Y > M:
    print("M", M)
elif Y == M:
    print("Y","M",Y)
else:
    print("Y",Y)
    
# 틀렸다고 뜨는 코드이다.
# range(N)으로 쓰면 왜 잘못된건지 이해가 안간다.
