MOD = 10**9 + 9
dp = [0, 1, 2, 4]

for _ in range(int(input())):
    N = int(input())
    while len(dp) <= N:
        dp.append((dp[-1] + dp[-2] + dp[-3]) % MOD)
    print(dp[N])