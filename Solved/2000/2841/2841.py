# 풀이 과정
# https://blog.naver.com/alsrua7222/222660366965

import sys
input = sys.stdin.readline

N, P = map(int, input().split())
stack = [[] for _ in range(7)]
answer = 0
for _ in range(N):
    number, plat = map(int, input().split())
    while stack[number] and stack[number][-1] > plat:
        stack[number].pop()
        answer += 1

    if stack[number] and stack[number][-1] == plat:
        continue
    stack[number].append(plat)
    answer += 1
print(answer)