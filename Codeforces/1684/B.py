import sys
input = sys.stdin.readline

for _ in range(int(input())):
    a, b, c = map(int, input().split())
    Z = c
    Y = Z + b
    X = Y + a
    print(X, Y, Z)