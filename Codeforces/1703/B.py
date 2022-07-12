import sys
input = sys.stdin.readline
for _ in range(int(input())):
    n = int(input())
    s = input().rstrip()
    used = set()
    pre = ""
    answer = 0
    for v in s:
        if v not in used:
            used.add(v)
            answer += 2
        else:
            answer += 1
    print(answer)