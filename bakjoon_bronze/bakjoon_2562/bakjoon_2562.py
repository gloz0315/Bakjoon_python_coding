# 서로 다른 9개의 자연수 중에서 최대값을 찾고, 그 최대값이 몇 번째 수인지 구하는 프로그램을 짜는 것
lst = []
for i in range(9):
    lst.append(int(input()))

print(max(lst))
print(lst.index(max(lst))+1)

# lst라는 리스트를 만들어서 그 안에 차례대로 입력을 하여 최대값의 인덱스 번호를 찾는다.
# 다만 인덱스는 0부터 시작하므로 1을 더한다.
