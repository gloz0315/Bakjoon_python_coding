# 단어공부
# 알파벳 대소문자로 이루어진 단어에서 가장 많이 사용되는 알파벳을 알아내는 프로그램
# 대소문자 구별하지 않고, 출력은 대문자로만 출력
# 가장 많이 사용 되는 단어의 수가 2개 이상일 경우 ? 출력이 나오도록 함

words = input().upper()
unique_words = list(set(words))
cnt = []

for i in unique_words:
    count = words.count(i) 
    cnt.append(count)

if cnt.count(max(cnt)) > 1:
    print("?")
else:
    print(unique_words[cnt.index(max(cnt))])
    
# 문제에 대한 코드를 주어졌을 때
# 만약 words = baaa 로 입력하면
# unique_words = ['b','a']가 입력됨 ( 여기서는 중복되는 단어를 없애는 set을 썻음 )
# for문을 통해 unique_words안의 단어들을 words에 찾아봄
# count라는 변수에 얼마나 단어가 써져 있는지 넣어보며
# cnt라는 리스트에 count를 넣는다. 그렇다면 b는 1번, a는 3번이므로
# cnt = [1,3] 이 넣어진다.
# unique_words의 인덱스 번호와 cnt의 인덱스 번호가 서로 일치하면서 각자의 인덱스 번호끼리 단어와 단어의 쓰인 숫자를 포함하므로
# unique_words안의 인덱스 번호를 찾아내면 되는 문제

# 처음에 어떻게 해야할지 몰라서 찾아봤다.
