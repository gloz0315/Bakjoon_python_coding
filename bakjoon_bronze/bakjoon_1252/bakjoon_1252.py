# 이진수 덧셈의 문제

A,B = map(str,input().split())

A = int(A,2)
B = int(B,2)

sum = A+B

print(bin(sum)[2:])

# 십진수를 이진수로 바꾸었을때, bin()함수를 통해서 변환이 가능하며
# 이진수에서는 0b부터 시작하기 때문에 2번째 인덱스에서부터 끝까지 글자를 출력하면 된다.
# 따라서 bin(sum)[2:] 를 쓴 것이다.
