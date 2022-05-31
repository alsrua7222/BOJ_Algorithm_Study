while True:
    a, b = map(int, input().split())
    if a == 0 and b == 0:
        break
    
    carry_cnt = 0
    tmp = 0
    while a > 0 or b > 0:
        tmp = a % 10 + b % 10 + (1 if tmp >= 10 else 0)
        if tmp >= 10:
            carry_cnt += 1
        a //= 10
        b //= 10
    print(carry_cnt)