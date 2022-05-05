for _ in range(int(input())):
    s = input()
    n = len(s)
    if n == 1:
        print(1)
        continue

    left = n - 1
    right = 0
    for i in range(n):
        if s[i] == '0':
            left = i
            break
    
    for i in range(n - 1, -1, -1):
        if s[i] == '1':
            right = i
            break
    
    print(abs(left - right) + 1)