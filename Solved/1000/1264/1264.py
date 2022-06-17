while True:
    s = input()
    if s == '#':
        break
    moum = list('aeiou')
    s = s.lower()
    print(sum([s.count(moum[i]) for i in range(5)]))