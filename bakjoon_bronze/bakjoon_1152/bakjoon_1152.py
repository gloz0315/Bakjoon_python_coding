# 단어의 개수
# 여러가지 문자열이 주어진다면 그 문자열에서의 단어가 몇개인지 구하기.

word = input().split()
print(len(word))

# 첫번째 코드. ( " " 띄어쓰기를 통해서 단어를 처리하는 것 )

word = input()
print(word.count(" ")+1)

#  두번째 내가 생각했던 코드, ( 이것은 제출했을때 오류라고 뜬다. ) 
# word라는 변수에 입력값을 넣어서 그 안의 " " 띄어쓰기의 숫자를 세고 +1을 하면 문자열에서의 단어가 몇개인지 구할 수 있다.
# 결과 값은 똑같지만 왜 틀렷는지 모르겠다..
