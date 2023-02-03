# 금고털이
# https://softeer.ai/practice/info.do?idx=1&eid=395

import sys
input = sys.stdin.readline

W, N = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
arr.sort(key=lambda x: (-x[1]))
answer = 0
i = 0
while W > 0 and i < N:
    M, P = arr[i]
    if W >= M:
        W -= M
        answer += M * P
    else:
        answer += W * P
        W = 0
    i += 1
print(answer)