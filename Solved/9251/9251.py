str1 = input()
str2 = input()

dp = [[0 for _ in range(len(str1))] for _ in range(len(str2) + 1)]

# 가로 초기화 배열 선언.
cnt = 0
for i in range(len(str1)):
    if cnt == 0 and str1[i] == str2[0]:
        cnt += 1
    dp[1][i] = cnt

# 세로 초기화 배열 선언.
cnt = 0
for i in range(len(str2)):
    if cnt == 0 and str2[i] == str1[0]:
        cnt += 1
    dp[i + 1][0] = cnt

for col in range(1, len(str2)):
    for row in range(1, len(str1)):
        if str2[col] == str1[row]:
            # 왼쪽 대각선 + 1
            dp[col + 1][row] = dp[col][row - 1] + 1
        else:
            # 왼쪽, 위쪽 중 큰 값.
            dp[col + 1][row] = max(dp[col][row], dp[col + 1][row - 1])

print(dp[-1][-1])
