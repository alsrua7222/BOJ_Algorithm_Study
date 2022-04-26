str1 = input()
str2 = input()
dp = [[0 for _ in range(len(str1) + 1)] for _ in range(len(str2) + 1)]

# (1, 1)부터 (N, M)까지 시행
for col in range(1, len(str2) + 1):
    for row in range(1, len(str1) + 1):
        if str2[col - 1] == str1[row - 1]:
            dp[col][row] = dp[col - 1][row - 1] + 1
        else:
            dp[col][row] = max(dp[col - 1][row], dp[col][row - 1])

# 역추적을 이용해서 출력하기.
x, y = len(str1), len(str2)
answer = ""
while x > 0 and y > 0:
    if dp[y][x] == dp[y - 1][x]:
        # 위, 아래 같으면
        y -= 1
    elif dp[y][x] == dp[y][x - 1]:
        # 왼, 오른 같으면
        x -= 1
    else:
        # 왼쪽 대각선으로 옮기면서 정답 출력.
        answer += str2[y - 1]
        x -= 1
        y -= 1
print(dp[-1][-1])
print(answer[::-1])
