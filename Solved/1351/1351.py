# 풀이 과정
# https://blog.naver.com/alsrua7222/222656814603

from collections import defaultdict

N, P, Q = map(int, input().split())
dp = defaultdict(int)
def backtracking(n):
    if n == 0:
        return 1
    if n in dp:
        return dp[n]
    
    res = 0
    left = n // P
    dp[left] = backtracking(left)
    right = n // Q
    dp[right] = backtracking(right)
    dp[n] = dp[left] + dp[right]
    return dp[n]

print(backtracking(N))