import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    cnt = a[0]
    answer = 0
    for v in a[1:]:
        answer += (v - cnt)
    print(answer)