R, C, W = map(int, input().split())
dp = []
dp.append([1])
dp.append([1, 1])

for i in range(2, R + W):
    dp.append([1])
    for j in range(1, i):
        dp[i].append(dp[i - 1][j - 1] + dp[i - 1][j])
    dp[i].append(1)

# print(*dp, sep="\n")
answer = 0
cnt = 0
for i in range(R - 1, R + W - 1):
    for j in range(C - 1, C + cnt):
        answer += dp[i][j]
    cnt += 1
print(answer)
