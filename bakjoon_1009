T = int(input())
a = []
b = []

for i in range(T):
    num1, num2 = input().split()
    a.append(int(num1))
    b.append(int(num2))

for x in range(T):
    base = a[x] % 10

    if base == 0:
        print(10)
    elif base in [1,5,6]:
        print(base)
    elif base in [4,9]:
        if b[x] % 2 == 0:
            print(base**2%10)
        else:
            print(base)
    else:
        if b[x]%4 == 0:
            print(base**4%10)
        else:
            print(base**(b[x]%4)%10)
