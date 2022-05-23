from collections import defaultdict
import sys
sys.setrecursionlimit(10**5)
n, x = map(int, input().split())
dp = defaultdict(int)
answer = float('inf')

def dfs(k, w):
    if k in dp and dp[k] <= w:
        return
    
    dp[k] = w

    if k >= n:
        global answer
        answer = min(answer, w)
        return
    
    visited = [0] * 15
    visited[0:2] = [1, 1]

    tmp = k
    while tmp:
        if visited[tmp % 10] == 0:
            visited[tmp % 10] = 1
            dfs(k * (tmp % 10), w + 1)
        tmp //= 10
    return 
n = 10 ** (n - 1)
dfs(x, 0)
print(answer if answer != float('inf') else -1)