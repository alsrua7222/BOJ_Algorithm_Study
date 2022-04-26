from collections import defaultdict
import heapq, sys
input = sys.stdin.readline

N = int(input())
M = int(input())
Graph = defaultdict(list)
for _ in range(M):
    u, v, c = map(int, input().split())
    Graph[u].append((v, c))

start, end = map(int, input().split())

# make dijkstra
def dijkstra(start, end):
    dist = [float('inf')] * (N + 1)
    dist[start] = 0
    que = [[0, start, [start]]]
    path = []
    while que:
        d, v, paths = heapq.heappop(que)
        if dist[v] < d:
            continue
        for nv, nc in Graph[v]:
            if dist[nv] > dist[v] + nc:
                dist[nv] = dist[v] + nc
                if nv == end:
                    path = paths + [nv]
                heapq.heappush(que, [dist[nv], nv, paths + [nv]])
    return (dist[end], len(path), path)

answer = dijkstra(start, end)
print(answer[0])
print(answer[1])
print(*answer[2])