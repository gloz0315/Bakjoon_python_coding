# 문제에 대해서 수열의 변화를 주는 문제이다.
# 이중 for문을 이용해서 값을 입력하고
# 보다 더 효율적으로 알고리즘을 다시 한번 학습할 필요가 있는 문제이다.

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

# 이 문제에 대해서 틀렸으므로 한번 다시 review 해야겠다.
