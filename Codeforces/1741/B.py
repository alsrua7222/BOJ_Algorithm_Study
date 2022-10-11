import sys
input = sys.stdin.readline

for tc in range(int(input())):
    n = int(input())
    if n == 3:
        print(-1)
    else:
        answer = list(i for i in range(n, 0, -1))
        if n % 2 == 0:
            print(*answer)
        else:
            if n == 1:
                answer = [1]
            elif n == 5:
                answer = [5, 4, 1, 2, 3]
            else:
                answer[n // 2], answer[n // 2 - 1] = answer[n // 2 - 1], answer[n // 2]
            print(*answer)
