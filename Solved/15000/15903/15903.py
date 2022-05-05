from heapq import *
n, m = map(int, input().split())
a = list(map(int, input().split()))
heapify(a)
for i in range(m):
    tmp = heappop(a) + heappop(a)
    heappush(a, tmp)
    heappush(a, tmp)
print(sum(a))