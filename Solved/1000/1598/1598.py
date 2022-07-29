a, b = map(int, input().split())
w = abs((a - 1) // 4 - (b - 1) // 4)
h = abs((a - 1) % 4 - (b - 1) % 4)
print(w + h)