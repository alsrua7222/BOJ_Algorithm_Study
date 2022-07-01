X = int(input())
total = 0
for _ in range(int(input())):
    a, b = map(int, input().split())
    total += a * b

print("Yes" if X == total else "No")