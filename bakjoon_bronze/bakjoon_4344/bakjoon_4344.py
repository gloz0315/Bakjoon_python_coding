# 첫번째 내가 혼자서 한 문제
# 평균을 넘는 학생들의 퍼센트를 구하는 것이다.
# 첫번째 입력값은 몇번 테스트를 돌리는 것인지
# 두번째 입력값부터는 총 학생수, 그리고 학생들의 점수들을 띄어쓰기 별로 나눠서 쓰면 된다.

C = int(input())

for i in range(C):
    lst = list(map(int,input().split()))
    for j in range(1,len(lst)):
        sum += lst[j]
    avg = sum/lst[0]
    for k in range(1,len(lst)):
        if lst[k] > avg:
            count += 1
    total = count/lst[0]*100
    print(f"{total:.3f}%")
    count,sum,avg,total = 0,0,0,0
    lst = []
    
# 보다 더 효율적으로 짧게 짠 코드 (아래)

C = int(input())
for i in range(C):
    lst = list(map(int,input().split()))
    avg = sum(lst[1:])/lst[0]
    cnt = 0
    for j in lst[1:]:
        if j > avg:
            cnt += 1
    rate = cnt/lst[0]*100
    print(f"{rate:.3f}%")
 
# sum()함수를 이용해서 lst안에 있는 list값들을 다 더하면 바로 평균을 낼 수 있다.
