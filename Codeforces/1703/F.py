import sys
input = sys.stdin.readline
from bisect import bisect_left
for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    really_a = []
    answer = 0
    for i, v in enumerate(a, 1):
        if v < i:
            answer += bisect_left(really_a, v)
            really_a.append(i)
    print(answer)