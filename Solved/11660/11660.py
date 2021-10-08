import sys
input = sys.stdin.readline
N, M = map(int, input().split())
arr = []
for _ in range(N):
    arr.append(list(map(int, input().split())))

dp = [[0 for row in range(N + 1)] for col in range(N + 1)]
dp[1][1] = arr[0][0]
for i in range(2, N + 1):
    dp[1][i] = arr[0][i - 1] + dp[1][i - 1]
    dp[i][1] = arr[i - 1][0] + dp[i - 1][1]

for col in range(2, N + 1):
    for row in range(2, N + 1):
        dp[col][row] = dp[col - 1][row] + dp[col][row - 1] - dp[col - 1][row - 1] + arr[col - 1][row - 1]

for _ in range(M):
    list1 = list(map(int, input().split()))
    y1 = list1[0] - 1
    x1 = list1[1] - 1
    y2 = list1[2]
    x2 = list1[3]
    print(dp[y2][x2] - dp[y1][x2] - dp[y2][x1] + dp[y1][x1])
