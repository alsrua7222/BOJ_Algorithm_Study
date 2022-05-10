import sys
input = sys.stdin.readline

for _ in range(int(input())):
    s = input().rstrip()
    left, right = 0, 0
    for v in s[:3]:
        left += int(v)
    for v in s[3:]:
        right += int(v)
    print("YES" if left == right else "NO")