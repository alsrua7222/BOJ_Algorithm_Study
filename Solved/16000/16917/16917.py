a, b, c, x, y = map(int, input().split())
answer = float('inf')
for i in range(100000 + 1):
    C = 2 * c * i
    A = max(0, (x - i) * a)
    B = max(0, (y - i) * b)
    answer = min(answer, C + A + B)
print(answer)