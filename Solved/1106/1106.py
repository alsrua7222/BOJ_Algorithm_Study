# 풀이 과정
# https://blog.naver.com/alsrua7222/222684282882

import sys
input = sys.stdin.readline
C, N = map(int, input().split())
dp = [float('inf')] * (C + 101)
dp[0] = 0
for _ in range(N):
    a, b = map(int, input().split())
    for j in range(b, C + 101):
        dp[j] = min(dp[j], dp[j - b] + a)

answer = min(dp[C:])
print(answer)