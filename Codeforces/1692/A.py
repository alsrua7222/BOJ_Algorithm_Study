import sys
input = sys.stdin.readline
for _ in range(int(input())):
    a, b, c, d = map(int, input().split())
    answer = 0
    if a < b:
        answer += 1
    if a < c:
        answer += 1
    if a < d:
        answer += 1
    print(answer)