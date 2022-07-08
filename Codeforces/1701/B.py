import sys
input = sys.stdin.readline
for _ in range(int(input())):
    n = int(input())
    
    print(2)
    if n == 2:
        print(1, 2)
    else:
        choose = [False] * (n + 1)
        answer = []
        start = 1
        while start <= n:
            tmp = start
            while tmp <= n and not choose[tmp]:
                answer.append(tmp)
                choose[tmp] = True
                tmp *= 2
            start += 1
        print(*answer)