# 풀이 과정
# https://blog.naver.com/alsrua7222/222632432832

from collections import defaultdict
str1 = input()
if len(str1) == 1:
    print(str1)
    exit(0)

info = defaultdict(int)
sorry = "I'm Sorry Hansoo"
for v in str1:
    info[v] += 1

even, odd = 0, 0
items = sorted(info.items(), key=lambda x: (x[0], -x[1]))
for key, value in items:
    if value & 1 == 0:
        even += 1
    else:
        odd += 1

if len(str1) & 1 == 0:
    if odd != 0:
        print(sorry)
    else:
        answer = ""
        for key, value in items:
            answer += key * (value // 2)
        answer += answer[::-1]
        print(answer)
else:
    if odd != 1:
        print(sorry)
    else:
        answer = ""
        mid = ''
        for key, value in items:
            if value & 1 == 1:
                mid = key
            answer += key * (value // 2)
        answer += mid + answer[::-1]
        print(answer)