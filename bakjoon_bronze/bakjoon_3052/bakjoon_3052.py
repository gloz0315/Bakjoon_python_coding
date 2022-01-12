# 나머지의 값들이 얼마나 있는지 알아보는 것

lst = []

for i in range(10):
    first = int(input())
    num = first % 42
    lst.append(num)

new_lst = set(lst)
print(len(new_lst))

# 42로 나누었을때, 나머지의 값
# 10개의 입력값을 넣어서 중복된 것을 뺀 나머지의 값들의 몇개있는지 보는 문제였다.
