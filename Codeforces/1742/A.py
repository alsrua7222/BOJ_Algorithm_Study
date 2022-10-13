import sys
input = sys.stdin.readline

for tc in range(int(input())):
    a, b, c = map(int, input().split())
    if a + b == c or a + c == b or b + c == a:
        print("YES")
    else:
        print("NO")