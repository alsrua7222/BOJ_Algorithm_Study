import sys
input = sys.stdin.readline
for _ in range(int(input())):
    a = []
    answer = 0
    for _ in range(2):
        a.append(list(map(int, input().split())))
        answer += sum(a[-1])
    print(0 if answer == 0 else 2 if answer == 4 else 1)