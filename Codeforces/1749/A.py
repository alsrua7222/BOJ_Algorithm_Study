import sys
input = sys.stdin.readline

for tc in range(int(input())):
    n, m = map(int, input().split())
    success = True
    if m >= n:
        success = False
    MAP = [[False] * 8 for i in range(n)]
    for i in range(m):
        col, row = map(int, input().split())
        MAP[col - 1][row - 1] = True
        for c in range(n):
            if col - 1 == c:
                continue
            if MAP[c][row - 1]:
                success = False

        for r in range(n):
            if row - 1 == r:
                continue
            if MAP[col - 1][r]:
                success = False
    print("YES" if success else "NO")