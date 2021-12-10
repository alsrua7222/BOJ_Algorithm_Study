N = int(input())
dp = [0, 1]
for i in range(N):
    dp[0], dp[1] = dp[1], dp[1] + dp[0]
print(dp[1] % 10007)
