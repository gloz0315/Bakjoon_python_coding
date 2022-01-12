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
    
# 이 문제는 한번 틀렸으므로 여기에 있으며, 다시 review 한다.
