# 원래 문제는 for문을 써서 9번을 돌려서 입력을 했다면
# 이번에는 그냥 한꺼번에 숫자를 입력하여 그 안의 최대값과 인덱스 번호를 뽑는 것

lst = list(map(int,input().split()))

print(max(lst))
print(lst.index(max(lst))+1)

# 더욱 쉽다.
