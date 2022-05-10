import sys
input = sys.stdin.readline

dx = [1, 1, -1, -1]
dy = [1, -1, 1, -1]
def process(MAP, n, m, x, y, direct):
    ret = 0
    x += dx[direct]
    y += dy[direct]
    while 0 <= x < n and 0 <= y < m:
        ret += MAP[x][y]
        x += dx[direct]
        y += dy[direct]
    return ret

for _ in range(int(input())):
    n, m = map(int, input().split())
    MAP = [list(map(int, input().split())) for _ in range(n)]
    MAX = 0
    for i in range(n):
        for j in range(m):
            SUM = MAP[i][j]
            SUM += process(MAP, n, m, i, j, 0)
            SUM += process(MAP, n, m, i, j, 1)
            SUM += process(MAP, n, m, i, j, 2)
            SUM += process(MAP, n, m, i, j, 3)
            MAX = max(MAX, SUM)
    print(MAX)