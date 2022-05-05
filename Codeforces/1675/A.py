for _ in range(int(input())):
    a, b, c, x, y = map(int, input().split())
    x -= a
    if x < 0:
        x = 0
    y -= b
    if y < 0:
        y = 0
    if c - (x + y) < 0:
        print('NO')
    else:
        print('YES')