# 개념적인 측면을 따져봐야 할 것 같다.
# list형을 int형과 비교 연산을 어떻게 하는지 다시 보자.
N,X = map(int,input().split())
A = list(map(int,input().split()))
for i in range(N):
    if A[i] < X:
        print(A[i],end=" ")
