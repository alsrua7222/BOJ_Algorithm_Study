while True:
    A, B = map(int, input().split())
    if A == 0 == B:
        break
    AWin = True
    while A != 0 and B != 0:
        if A < B:
            A, B = B, A
        if A % B == 0:
            break
        else:
            if A - B < B:
                A, B = A - B, B
                AWin = not AWin
            else:
                break
    print("A wins" if AWin else "B wins")