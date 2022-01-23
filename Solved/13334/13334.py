# 풀이 과정
# https://blog.naver.com/alsrua7222/222629527969

import sys
from heapq import *
input = sys.stdin.readline
arr = sorted([sorted(list(map(int, input().split()))) for _ in range(int(input()))], key=lambda x: (x[1], x[0]))
L = int(input())
answer = 0
HQ = []
for s, e in arr:
    if e - s > L:
        continue
    while HQ and e - HQ[0] > L:
        heappop(HQ)
    heappush(HQ, s)
    answer = max(answer, len(HQ))
print(answer)