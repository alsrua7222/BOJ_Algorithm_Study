# 풀이 과정
# https://blog.naver.com/alsrua7222/222610508436

import sys
input = sys.stdin.readline

N = int(input())
dp = [0] * (N + 1)
arr = [0]
for _ in range(N):
    arr.append(int(input()))

if N <= 2:
    print(sum(v for v in arr))
    exit(0)

dp[1] = arr[1]
dp[2] = arr[1] + arr[2]
dp[3] = max(arr[1], arr[2]) + arr[3]

for i in range(4, N + 1):
    dp[i] = max(dp[i - 2], dp[i - 3] + arr[i - 1]) + arr[i]
print(dp[N])
