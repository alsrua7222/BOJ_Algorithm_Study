for _ in range(int(input())):
    d, n, s, p = list(map(int, input().split()))
    p = n * p + d
    np = n * s
    if p > np:
        print("do not parallelize")
    elif p < np:
        print("parallelize")
    else:
        print("does not matter")