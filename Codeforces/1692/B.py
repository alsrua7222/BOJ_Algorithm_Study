import sys
input = sys.stdin.readline
for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    set_a = set(a)
    if (n - len(set_a)) % 2 == 0:
        print(len(set_a))
    else:
        print(len(set_a) - 1)