import sys
input = sys.stdin.readline

for _ in range(int(input())):
    vector = []
    SX = 0
    SY = 0

    def process(left, cur, x, y):
        if left == 0:
            return (SX - x * 2) ** 2 + (SY - y * 2) ** 2
        
        ret = float('inf')
        for i in range(cur, N):
            ret = min(ret, process(left - 1, i + 1, x + vector[i][0], y + vector[i][1]))
        return ret

    N = int(input())
    for _ in range(N):
        x, y = map(int, input().split())
        vector.append((x, y))
        SX += x
        SY += y
    print(process(N // 2, 0, 0, 0) ** 0.5)