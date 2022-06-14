import sys
input = sys.stdin.readline
for _ in range(int(input())):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    MAX = -float('inf')
    cur = 0

    x, y = 0, 0
    while y < n:
        cur += a[y]

        if cur < k:
            y += 1
        
        if cur == k:
            MAX = max(MAX, y - x + 1)
            y += 1
        
        if cur > k:
            cur -= a[x]
            cur -= a[y]
            x += 1
    
    if MAX == -float('inf'):
        print(-1)
    else:
        print(n - MAX)