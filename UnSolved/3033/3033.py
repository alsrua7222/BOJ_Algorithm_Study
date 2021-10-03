from collections import defaultdict

N = int(input())
str1 = input()
answer = 0
i = N
while i > 1:
    dict1 = defaultdict(int)
    cnt = 0
    while cnt < N - i + 1:
        tmp = str1[cnt: cnt + i]
        dict1[tmp] += 1
        if dict1[tmp] > 1:
            answer = len(tmp)
        cnt += 1
    if answer >= 2:
        break
    i -= 1

print(answer)
