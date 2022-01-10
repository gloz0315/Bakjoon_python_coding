T = int(input())

for i in range(T):
    a,b = input().split()
    num = int(a)**int(b)
    if num % 10 == 0:
        print(10)
    for j in range(1,10):
        if num % 10 == j:
            print(j)
