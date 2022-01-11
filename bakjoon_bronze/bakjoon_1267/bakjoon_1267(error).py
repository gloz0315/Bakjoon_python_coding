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

-----------------------------------------------

# 이유를 찾았다.
# range(N)을 하면 루프를 돌때마다 i 가 0부터 N-1을 도는 것이고
# A로 하면 루프를 돌때마다 i가 A의 인덱스 번호 [0]부터 [N-1]까지, 즉 원소 0부터 N-1 까지 도는 이유로써 이 문제에서 range(N)은 틀린것이다.
