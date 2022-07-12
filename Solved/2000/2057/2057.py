N = int(input())
fact = int("2,432,902,008,176,640,000".replace(',', ''))
if N == 0:
    print("NO")
else:
    for i in range(20, 0, -1):
        fact //= i
        if N >= fact:
            N -= fact
    print("YES" if N <= 0 else "NO")