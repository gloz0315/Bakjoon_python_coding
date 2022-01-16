# 알파벳 소문자로 이루어진 N개의 단어 정렬
# 길이가 짧은 것부터, 길이가 같으면 사전 순으로 정렬

N = int(input())
lst = []

for words in range(N):
    words = input()
    if words not in lst:
        lst.append(words)
lst.sort()
lst.sort(key = len)

for i in range(len(lst)):
    print(lst[i])
    
# 이렇게 하면 input()의 속도가 겁나 느리는 단점이 발생
# import sys을 통해서 더 빠르게 만듬

import sys

N = int(sys.stdin.readline())
lst = []

for words in range(N):
    words = sys.stdin.readline().strip()
    if words not in lst:
        lst.append(words)
lst.sort()
lst.sort(key = len)

for i in range(len(lst)):
    print(lst[i])

# 기본적으로 sys.stdin.readline()은 \n\을 포함 하기 때문에 출력문에서 문제가 발생한다
# 따라서 words = sys.stdin.readline().strip()을 통해서 띄어쓰기가 나지 않도록 만들어준다
