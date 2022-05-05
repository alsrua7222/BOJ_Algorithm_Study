def solve(n, a):
    cnt = 0
    cur_max = a[-1]
    for i in range(1, n):
        if a[i] == 0:
            return -1
    for i in range(n - 2, -1, -1):
        while (a[i] >= cur_max):
            cnt += 1
            a[i] //= 2
            if (a[i] == 0 and i >= 1):
                return -1
        cur_max = a[i]
    return cnt

for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    print(solve(n, a))