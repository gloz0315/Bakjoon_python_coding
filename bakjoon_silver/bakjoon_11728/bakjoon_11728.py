# 배열 합치기
# 처음에 두 개의 배열의 크기를 쓰고
# 각 배열에 들어가는 숫자를 넣음

import sys
a,b = map(int,sys.stdin.readline().split())
a_list = list(map(int,sys.stdin.readline().split()))
b_list = list(map(int,sys.stdin.readline().split()))
answer_list =sorted(a_list + b_list)
print(" ".join(map(str,answer_list)))
