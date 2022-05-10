for _ in range(int(input())):
    number, unit = input().split()
    number = float(number)
    if unit == 'kg':
        print(format(round(number * 2.2046, 4), ".4f"), 'lb')
    elif unit == 'lb':
        print(format(round(number * 0.4536, 4), ".4f"), 'kg')
    elif unit == 'g':
        print(format(round(number * 3.7854, 4), ".4f"), 'l')
    else:
        print(format(round(number * 0.2642, 4), ".4f"), 'g')