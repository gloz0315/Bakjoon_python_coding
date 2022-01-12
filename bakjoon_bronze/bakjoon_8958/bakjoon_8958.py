N = int(input())

for i in range(N):
    questions = input()
    score = 0
    total = 0
    for j in questions:
        if j == "O":
            score += 1
            total += score
        else:
            score = 0
    print(total)
    
# OX퀴즈를 통해 연속된 O가 발생할 경우 점수를 1점씩 중복하여 올라가고
# 그렇지 않다면 다시 O가 나오면 1점부터 점수가 올라가는 형식
# 즉, OOXXOX 인 경우 점수의 합은 1+2+1 = 4
# OOOXXOOXOXOO 인 경우 점수의 합은 1+2+3+1+2+1+1+2=13 점이다
