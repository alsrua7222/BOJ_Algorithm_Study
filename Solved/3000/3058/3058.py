for _ in range(int(input())):
    A = list(map(int, input().split()))
    SUM, MIN = 0, float('inf')
    for v in A:
        if v & 1 == 0:
            SUM += v
            MIN = min(MIN, v)
    print(SUM, MIN)