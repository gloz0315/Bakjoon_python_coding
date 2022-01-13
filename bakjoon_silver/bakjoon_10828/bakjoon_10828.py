# 자료 구조의 문제이다.
# push X : 정수 X를 스택에 넣는 연산
# pop : 스택에서 가장 위에 있는 정수를 빼고, 그 수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.
# size : 스택에 들어있는 정수의 개수를 출력한다.
# empty : 스택에 비어있으면 1, 아니면 0을 출력한다.
# top : 스택의 가장 위에 있는 정수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.

import sys

C = int(sys.stdin.readline())
temp = []
for i in range(C):
    lst = sys.stdin.readline().split()

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
