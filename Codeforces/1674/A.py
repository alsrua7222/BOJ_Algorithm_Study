for _ in range(int(input())):
    x, y = map(int, input().split())
    if x > y:
        print("0 0")
    else:
        if y % x == 0:
            print(f"1 {y // x}")
        else:
            print("0 0")