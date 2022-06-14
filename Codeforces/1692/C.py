import sys
input = sys.stdin.readline
for _ in range(int(input())):
    input()
    MAP = [list(input().rstrip()) for _ in range(8)]

    dxy = [(1, 1), (1, -1), (-1, 1), (-1, -1)]

    def solve():
        for i in range(1, 7):
            for j in range(1, 7):
                success = True
                for idx in range(4):
                    if MAP[i + dxy[idx][0]][j + dxy[idx][1]] == '.':
                        success = False
                        break
                if success:
                    return [i + 1, j + 1]
        return [-1, -1]
    print(*solve())