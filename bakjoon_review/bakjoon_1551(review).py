N,K = map(int,input().split())
lst = list(map(int,input().split(",")))
temp = []

for i in range(K):
    for j in range(len(lst)-1):
        temp.append(lst[j+1] - lst[j])
    lst = temp
    temp = []

lst = list(map(str,lst))
print(','.join(lst))

# 문제에 대하여 수열의 문제이다.
# 약간의 알고리즘을 다시 복습할 필요가 있으며
# 마지막 출력문장에서 리스트의 대괄호를 빼고 출력하는 부분을 다시 학습해보자.
