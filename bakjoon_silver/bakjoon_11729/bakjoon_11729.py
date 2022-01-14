# 하노이 탑 이동 순서 문제
# 수학적인 센스와 이를 통한 코딩을 하기. ( 현재로써 수학적으로는 생각하기 쉬웠으나 코딩을 짜는 것에 어려움을 느꼇음, 다시 한번 풀어보기 )

import sys

n = int(sys.stdin.readline())
lst = [1]
def hanoi(n,a,b,c):
    if n == 1:
        print(a,c)
    else:
        hanoi(n-1,a,c,b)
        print(a,c)
        hanoi(n-1,b,a,c)
for i in range(n-1):
    lst.append(2*lst[i]+1)
print(lst[n-1])
hanoi(n,1,2,3)

# 리스트 형식으로 이용을 해보았을때, 시간이 덜 걸렸다.
