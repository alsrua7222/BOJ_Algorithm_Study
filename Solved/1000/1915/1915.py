R, C = map(int, input().split())
grid = [list(map(int, list(input()))) for _ in range(R)]

dp = [[0] * C for _ in range(R)]

for col in range(C):
    dp[0][col] = grid[0][col]
for row in range(1, R):
    dp[row][0] = grid[row][0]

for row in range(1, R):
    for col in range(1, C):
        if grid[row][col] == 1:
            dp[row][col] = min(dp[row - 1][col - 1], dp[row - 1][col], dp[row][col - 1]) + 1

answer = 0
for row in range(R):
    answer = max(answer, max(dp[row]))
print(answer ** 2)