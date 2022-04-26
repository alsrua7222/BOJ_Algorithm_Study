# 풀이 과정
# https://blog.naver.com/alsrua7222/222664110493

from collections import defaultdict

N, P, Q, X, Y = map(int, input().split())
dp = defaultdict(int)

def backtracking(n):
    if n <= 0:
        return 1
    if n in dp:
        return dp[n]
    
    left = n // P - X
    left2 = backtracking(left)
    if left >= 0:
        dp[left] = left2
    
    right = n // Q - Y
    right2 = backtracking(right)
    if right >= 0:
        dp[right] = right2
    dp[n] = left2 + right2
    return dp[n]

print(backtracking(N))