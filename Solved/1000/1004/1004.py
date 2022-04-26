for _ in range(int(input())):
    cnt = 0
    sx, sy, ax, ay = map(int, input().split())
    N = int(input())
    for i in range(N):
        x, y, r = map(int, input().split())
        first, second = False, False
        if (x - sx)**2 + (y - sy)**2 > r**2:
            first = True
        if (x - ax) ** 2 + (y - ay) ** 2 > r ** 2:
            second = True

        if first and not second:
            cnt += 1
        elif not first and second:
            cnt += 1
    print(cnt)
