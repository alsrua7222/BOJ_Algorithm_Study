M, N = map(int, input().split())
dp = [True] * (N + 1)
dp[0] = dp[1] = False
for i in range(2, int(N**.5) + 1):
    if dp[i]:
        for j in range(i * 2, N + 1, i):
            dp[j] = False
for i in range(M, N + 1):
    if dp[i]:
        print(i)
