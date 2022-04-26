# 풀이 과정
# https://blog.naver.com/alsrua7222/222697964888

from collections import defaultdict
import sys
input = sys.stdin.readline

N = int(input())
arr = []
for i in range(N):
    tmp = list(map(int, input().split()))
    arr.append((i, tmp[0], tmp[1]))
arr.sort(key=lambda x: (x[2], x[1]))

info = defaultdict(int)
total = 0
answer = [0] * N
pre = arr[0][2]
stack = []
for idx, c, s in arr:
    if pre != s:
        pre = s
        while stack:
            c1, s1 = stack.pop()
            total += s1
            info[c1] += s1
    stack.append((c, s))
    answer[idx] += total - info[c]

print(*answer, sep="\n")