import sys
input = sys.stdin.readline

for tc in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    print(sum(a) + sum(b) - max(b))