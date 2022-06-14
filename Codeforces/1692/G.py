import sys
input = sys.stdin.readline
for _ in range(int(input())):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))

    cnt_a = [0] * n
    for i in range(n - 1):
        if a[i] >= a[i + 1] * 2:
            cnt_a[i] = -1
        else:
            cnt_a[i] = 1

    x, y = 0, 0
    total = 0
    answer = 0
    while y < n:
        if y - x >= k:
            if total == k:
                answer += 1
            total -= cnt_a[x]
            x += 1
        else:
            total += cnt_a[y]
            y += 1
    
    if y - x > k:
        if total > 0 and total == k:
            answer += 1

    print(answer)