# 풀이 과정
# https://blog.naver.com/alsrua7222/222634199468

import sys
from collections import deque
input = sys.stdin.readline

def solve(arrow, cnt):
    for i in range(cnt):
        if arrow == 1:
            mid.append(left.popleft())
        else:
            mid.append(right.popleft())
    return

def init():
    for i in range(13):
        left.append(mid.popleft())
    for i in range(14):
        right.append(mid.popleft())
    return

left = deque()
right = deque()
mid = deque([i for i in range(27)])

for _ in range(int(input())):
    A = [*map(int, input().split())]
    init()
    for i in range(len(A)):
        solve(i & 1, A[i])

for i in range(27):
    if mid[i] == 0:
        print(i + 1)
        break
