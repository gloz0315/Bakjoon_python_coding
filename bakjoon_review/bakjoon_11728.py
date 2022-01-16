# 다시 한번 풀어보기

import sys
a,b = map(int,sys.stdin.readline().split())
a_list = list(map(int,sys.stdin.readline().split()))
b_list = list(map(int,sys.stdin.readline().split()))
answer_list =sorted(a_list + b_list)
print(" ".join(map(str,answer_list)))
