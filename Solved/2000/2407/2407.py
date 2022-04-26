n, m = map(int, input().split())
dp = [[0 for _ in range(m + 1)] for _ in range(n + 1)]

for i in range(n + 1):
    for j in range(i + 1):
        if j > m:
            break
        if i == j or j == 0:
            dp[i][j] = 1
        else:
            dp[i][j] = dp[i - 1][j] + dp[i - 1][j - 1]

print(dp[n][m])
