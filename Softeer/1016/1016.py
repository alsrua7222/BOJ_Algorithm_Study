import sys
input = sys.stdin.readline

A, B = map(int, input().split())
print('A' if A > B else 'B' if A < B else "same")