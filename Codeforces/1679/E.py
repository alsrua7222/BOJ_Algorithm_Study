import sys, bisect
input = sys.stdin.readline

for _ in range(int(input())):
    n, q = map(int, input().split())
    a = list(map(int, input().split()))
    x = [int(input()) for _ in range(q)]
    
    a.sort(reverse=True)
    aa = [a[0]]
    for v in a[1:]:
        aa.append(v + aa[-1])
    
    for goal in x:
        index = bisect.bisect_left(aa, goal) + 1
        print(index if index <= n else -1)