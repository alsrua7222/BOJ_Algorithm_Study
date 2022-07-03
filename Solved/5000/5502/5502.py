n = int(input())
s = input()
sr = s[::-1]
# 맨 뒤에 추가하는 식으로 하면 최소가 아닐 수도 있음.
# dp로 결국 양쪽 비교 조건 식으로 추가.

dp = [[0] * (n + 1) for _ in range(n + 1)]
for i in range(n):
    if (s[i] == sr[0]) or (i > 0 and dp[0][i - 1]):
        dp[0][i] = 1
    if (s[0] == sr[i]) or (i > 0 and dp[i - 1][0]):
        dp[i][0] = 1

MAX = 0
for i in range(1, n):
    for j in range(1, n):
        if s[j] == sr[i]:
            dp[i][j] = dp[i - 1][j - 1] + 1
        dp[i][j] = max(dp[i][j], max(dp[i - 1][j], dp[i][j - 1]))
        MAX = max(MAX, dp[i][j])
print(n - MAX)