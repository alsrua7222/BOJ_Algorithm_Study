for _ in range(int(input())):
    s = input()
    t = input()

    a_count = 0
    for v in t:
        if v == 'a':
            a_count += 1
    
    if a_count == 0:
        print(2 ** len(s))
    else:
        if a_count == 1 and len(t) == 1:
            print(1)
        else:
            print(-1)