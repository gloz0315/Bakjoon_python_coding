T = int(input())

for i in range(T):
    a,b = input().split()
    num = int(a)**int(b)
    if num % 10 == 0:
        print(10)
    for j in range(1,10):
        if num % 10 == j:
            print(j)

# 이런 방식으로 해도 출력되는 결과 값은 같지만 백준에서는 틀렸다 라고 뜬다.. 왜일까 ?
