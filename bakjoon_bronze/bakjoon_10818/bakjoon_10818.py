# 최대, 최소 값 구하기

N = int(input())
lst = list(map(int,input().split()))
print(min(lst),max(lst))

-------------------------------

N = int(input())
lst = list(map(int,input().split()))
lst.sort()
print(lst[0],lst[-1])

# 총 2가지 코드를 써 보았다.
# 첫번째 예시를 통해 정말 간단하게 min,max를 통해 lst에 있는 값들의 최소 최대 값을 찾는 것이고
# 두번째 예시는 lst의 값들을 정렬하여 sort()는 오름차순 정렬이므로 0번째 인덱스는 최소값 마지막 인덱스는 최대값으로 찾을 수 있다.
