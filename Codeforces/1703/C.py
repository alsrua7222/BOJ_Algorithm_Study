import sys
input = sys.stdin.readline
for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    for i in range(n):
        query = list(input().split())
        for v in query[1]:
            if v == 'D':
                a[i] = (a[i] + 1) % 10
            else:
                a[i] = (a[i] - 1) % 10
    print(*a)