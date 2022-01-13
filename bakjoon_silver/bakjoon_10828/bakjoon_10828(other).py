C = int(input())
temp = []
for i in range(C):
    lst = list(map(str,input().split()))

    if lst[0] == "push":
        temp.append(lst[-1])
    elif lst[0] == "top":
        if len(temp) == 0:
            print("-1")
        else:
            print(temp[-1])
    elif lst[0] == "size":
        print(len(temp))
    elif lst[0] == "empty":
        if len(temp) == 0:
            print("1")
        else:
            print("0")
    elif lst[0] == "pop":
        if len(temp) == 0:
            print(-1)
        else:
            print(temp[-1])
            temp.pop(-1)

# 이 코드는 실행을 돌리면 시간초과로 인하여 돌려지지 않는다
# input() 함수가 아닌 import sys 를 통해 sys.stdin.readline()의 함수를 많이 써야겠다. 
