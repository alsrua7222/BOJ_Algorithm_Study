import math
y1, m1, d1 = map(int, input().split())
y2, m2, d2 = map(int, input().split())

def convert(y, m, d):
    return y * 365 + m * 30 + d
c1, c2 = convert(y1, m1, d1), convert(y2, m2, d2)
print((c2 - c1) // 365)

print(y2 - y1 + 1)
print(y2 - y1)