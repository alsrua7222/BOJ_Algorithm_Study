# 풀이 과정
# https://blog.naver.com/alsrua7222/222665623117

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = [int(input()) for _ in range(M)]
arr.sort(reverse=True)

answer = 0
cost = 0
for i in range(min(N, M)):
    if answer < (i + 1) * arr[i]:
        answer = (i + 1) * arr[i]
        cost = arr[i]
    answer = max(answer, (i + 1) * arr[i])
print(cost, answer)