import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n, m = map(int, input().split())
    strings = [input().rstrip() for _ in range(n)]

    answer = float('inf')
    for i in range(n):
        for j in range(i + 1, n):
            SUM = 0
            for k in range(m):
                SUM += abs(ord(strings[i][k]) - ord(strings[j][k]))
            if answer > SUM:
                answer = SUM
    print(answer)