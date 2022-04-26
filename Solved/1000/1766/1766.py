from collections import defaultdict
import heapq, sys
input = sys.stdin.readline

N, M = map(int, input().split())

Graph = defaultdict(list)
InDegree = [0] * (N + 1)
for _ in range(M):
    A, B = map(int, input().split())
    Graph[A].append(B)
    InDegree[B] += 1

Queue = []

cnt = 0
for i in range(1, N + 1):
    if InDegree[i] == 0:
        heapq.heappush(Queue, [cnt, i])
        cnt += 1

for i in range(1, N + 1):

    now = heapq.heappop(Queue)
    print(now[1], end=" ")
    for key in Graph[now[1]]:
        InDegree[key] -= 1
        if InDegree[key] == 0:
            heapq.heappush(Queue, [now[0], key])
