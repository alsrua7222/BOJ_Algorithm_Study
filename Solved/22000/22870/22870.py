from collections import defaultdict
from heapq import *
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
Graph = defaultdict(list)
for _ in range(M):
    u, v, w = map(int, input().split())
    Graph[u].append([v, w])
    Graph[v].append([u, w])
start, end = map(int, input().split())

# 일단 데이크스트라로 구현해서 최단 거리를 구한다.
# S에서 E로 갈 때, 한 방향만 설정하도록 해야 한다. -> S에서 E까지, E에서 S까지 구한 최단거리로 구할 수 있다.
# SE[cur] + weight + ES[next]가 SE[end]랑 같으면 S에서 E까지 한번에 가는 최적 경로를 구해진다.
# 본 문제에서 S -> E -> S 가는 경로가 다양하다고 하면, 이 중에서 사전 순으로 앞서는 경로를 구한다. 즉, 다음 노드를 결정할 때, 결정할 노드 중에서 가장 작은 노드를 구하면 된다.

def dijkstra(s):
    HQ = []
    dist = [987654321] * (N + 1)
    dist[s] = 0
    heappush(HQ, [0, s])
    while HQ:
        w, cur = heappop(HQ)
        if dist[cur] < w:
            continue
        for next, v in Graph[cur]:
            if dist[next] > w + v:
                dist[next] = w + v
                heappush(HQ, [dist[next], next])
    return dist

# 시작에서 끝까지, 끝에서 시작까지 최단 거리를 모두 구한다.
dist_start = dijkstra(start)
dist_end = dijkstra(end)

# S에서 E까지 한번에 가는 최적 경로 셋팅.
visited = [False] * (N + 1)
pre = cur = start
finish = end
while cur != finish:
    MinNode = N + 1
    for next, v in Graph[cur]:
        if next != pre and dist_start[cur] + v + dist_end[next] == dist_start[finish]:
            MinNode = min(MinNode, next)
    pre = cur
    cur = MinNode
    visited[cur] = True

# 한번에 가는 최적 경로를 구했기 때문에 도착 지점에 TRUE 되어 있을 것, FALSE로 수정.
visited[end] = False

# S에서 E까지 사용한 경로를 포함해서 E에서 S까지 최단 거리를 구한다.
def dijkstra_with_visited(s):
    HQ = []
    dist = [987654321] * (N + 1)
    dist[s] = 0
    heappush(HQ, [0, s])
    while HQ:
        w, cur = heappop(HQ)
        if dist[cur] < w:
            continue
        for next, v in Graph[cur]:
            if not visited[next] and dist[next] > w + v:
                dist[next] = w + v
                heappush(HQ, [dist[next], next])
    return dist

print(dist_start[end] + dijkstra_with_visited(end)[start])
