from collections import defaultdict
from heapq import *
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
Graph = defaultdict(list)
for _ in range(M):
    u, v = map(int, input().split())
    Graph[u].append(v)
    Graph[v].append(u)

for k in Graph.keys():
    Graph[k].sort()

start, end = map(int, input().split())
visited = [False] * (N + 1)

def dijkstra(s):
    HQ = []
    dist = [987654321] * (N + 1)
    dist[s] = 0
    heappush(HQ, (0, s))
    while HQ:
        w, cur = heappop(HQ)
        if dist[cur] < w:
            continue
        for next in Graph[cur]:
            if not visited[next] and dist[next] > w + 1:
                dist[next] = w + 1
                heappush(HQ, (dist[next], next))
    return dist

dist = dijkstra(end)

cur = start
length = 0
while end != cur:
    for next in Graph[cur]:
        if length + 1 + dist[next] == dist[start]:
            visited[next] = True
            length += 1
            cur = next
            break

visited[end] = False

print(dist[start] + dijkstra(start)[end])
