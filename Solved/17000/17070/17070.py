N = int(input())
MAP = [list(map(int, input().split())) for _ in range(N)]
dp = [[[0] * N for _ in range(N)] for _ in range(3)]

def memoization():
    dp[0][0][1] = 1 # 0: 가로, 1:세로, 2:대각

    for i in range(2, N):
        if MAP[0][i] == 0:
            dp[0][0][i] = dp[0][0][i - 1]
    
    for x in range(1, N):
        for y in range(1, N):
            if MAP[x][y] == 0:
                dp[0][x][y] = dp[0][x][y - 1] + dp[2][x][y - 1]
                dp[1][x][y] = dp[1][x - 1][y] + dp[2][x - 1][y]
                if MAP[x][y - 1] == 0 and MAP[x - 1][y] == 0:
                    dp[2][x][y] = dp[0][x - 1][y - 1] + dp[1][x - 1][y - 1] + dp[2][x - 1][y - 1]
    return sum([dp[i][-1][-1] for i in range(3)])

print(memoization())
            