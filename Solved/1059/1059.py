# 풀이 과정
# https://blog.naver.com/alsrua7222/222639881377

L = int(input())
S = sorted(list(map(int, input().split())))
n = int(input())
MIN, MAX = 0, 1001
for v in S:
    if n > v:
        MIN = max(MIN, v)
    elif n < v:
        MAX = min(MAX, v)
    else:
        print(0)
        exit(0)
left = MIN + 1
right = MAX - 1

print((n - left + 1) * (right - n + 1) - 1)