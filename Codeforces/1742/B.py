import sys
input = sys.stdin.readline

def solve(a):
    pre = a[0]
    for i in range(1, len(a)):
        if pre < a[i]:
            pre = a[i]
        else:
            return "NO"
    return "YES"

for tc in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    print(solve(a))