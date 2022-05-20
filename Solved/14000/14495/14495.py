n = int(input())
dp = [1, 1, 1, 2]
while len(dp) <= n:
    dp.append(dp[-1] + dp[-3])
print(dp[n - 1])