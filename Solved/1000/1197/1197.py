import heapq
V, E = map(int, input().split())
parents = [0] + [i for i in range(1, V + 1)]
HQ = []
for _ in range(E):
    A, B, C = map(int, input().split())
    heapq.heappush(HQ, [C, A, B])

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
cnt = 0
answer = 0
while cnt != V - 1:
    w, a, b = heapq.heappop(HQ)
    ar = find(a)
    br = find(b)
    if ar != br:
        union(ar, br)
        cnt += 1
        answer += w
print(answer)
