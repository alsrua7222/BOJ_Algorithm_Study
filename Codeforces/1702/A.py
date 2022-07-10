import sys
input = sys.stdin.readline
for _ in range(int(input())):
    m = input().rstrip()
    if m == "1":
        print(0)
        continue
    print(int(m) - pow(10, len(m) - 1))