x, y, w, h = map(int, input().split())
X = w - x if w - x <= w // 2 else x
Y = h - y if h - y <= h // 2 else y
print(min(X, Y))
