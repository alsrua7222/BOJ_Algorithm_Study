import sys
input = sys.stdin.readline
for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    M, m = -float('inf'), float('inf')
    for v in a:
        M, m = max(M, v), min(m, v)
    print((M - m) * 2)