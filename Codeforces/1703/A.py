import sys
input = sys.stdin.readline
for _ in range(int(input())):
    string = input().rstrip().upper()
    print("YES" if string == "YES" else "NO")