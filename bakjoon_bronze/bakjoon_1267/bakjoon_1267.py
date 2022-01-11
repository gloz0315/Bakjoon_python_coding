N = int(input())
A = list(map(int,input().split()))
Y = M = 0
for i in A:
    Y += (i//30 + 1)*10
    M += (i//60 + 1)*15

if Y > M:
    print("M", M)
elif Y == M:
    print("Y","M",Y)
else:
    print("Y",Y)

# 뭔가 문제를 풀면서 직접 해보면 아무런 이상이 없지만 제출만 하면 틀렸습니다, 런타임 에러가 뜬다.
# 그래서 찾아보니 내가 쓴 코드와 별반 다를게 없지만 그냥 아주 조금 미세하게 다른거 뿐
# 이상한거같다 이건 진짜..
