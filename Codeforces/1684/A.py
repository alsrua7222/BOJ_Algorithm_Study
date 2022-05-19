import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n = input().rstrip()
    if len(n) == 2:
        print(n[-1])
    else:
        n = int(n)
        answer = 99
        while n > 0:
            answer = min(answer, n % 10)
            n //= 10
        print(answer)