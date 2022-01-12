# 세 개의 자연수를 입력하여서 세 자연수를 곱한 값을 통해
# 결과값이 0부터9까지의 숫자가 각각 몇번 나왔는지 출력하는 문제
A = int(input())
B = int(input())
C = int(input())

total = A*B*C

for i in range(10):
    print(str(total).count(str(i)))
    
# count()함수는 세는 것을 의미
# total이라는 숫자 int값을 str값으로 바꾸고, 그 안의 숫자를 세면 되는것
# count() 함수 안에는 int형이 들어갈 수 없는 것 같다, str 값을 넣으라고 오류가 떳다.
