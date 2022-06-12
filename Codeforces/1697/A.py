import sys
input = sys.stdin.readline
for _ in range(int(input())):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))

    answer = 0
    for i in range(n):
        if m >= a[i]:
            m -= a[i]
        else:
            if m == 0:
                answer += a[i]
            else:
                answer += a[i] - m
                m = 0
    print(answer)