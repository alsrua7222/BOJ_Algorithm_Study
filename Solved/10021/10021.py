import sys
input = sys.stdin.readline
from heapq import *
N, C = map(int, input().split())
parents = [i for i in range(N + 1)]
def getDistance(arr1, arr2):
    return (arr1[0] - arr2[0]) ** 2 + (arr1[1] - arr2[1]) ** 2
arr = []
for _ in range(N):
    arr.append(list(map(int, input().split())))
def find(x):
    if parents[x] == x:
        return x
    else:
        p = find(parents[x])
        parents[x] = p
        return p

def union(x, y):
    if x != y:
        parents[x] = y
HQ = []

for i in range(N):
    for j in range(i + 1, N):
        tmp = getDistance(arr[i], arr[j])
        if C <= tmp:
            heappush(HQ, [tmp, i, j])

cnt = 0
answer = 0
while HQ:
    w, a, b = heappop(HQ)
    ar = find(a)
    br = find(b)
    if ar != br:
        union(ar, br)
        cnt += 1
        answer += w
        if cnt == N - 1:
            break

if cnt == N- 1:
    print(answer)
else:
    print(-1)
