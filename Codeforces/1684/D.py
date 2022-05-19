import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    a_point = list(enumerate(a))
    a_point.sort(key=lambda x: (-x[1], x[0]))
    
    if n <= k:
        print(0)
    else:
        s = []
        for i in range(k):
            s.append(a_point[i][0])
        s.sort()

        count = 0
        x = 0
        for i in range(k - 1):
            count += 1
            tmp = s[i + 1] - s[i] - 1
            x += count * tmp
            a[s[i]] = 0
        
        tmp = n - 1 - s[k - 1]
        count += 1
        x += tmp * count
        a[s[k - 1]] = 0

        print(sum(a) + x)