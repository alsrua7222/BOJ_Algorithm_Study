from collections import defaultdict
import sys, heapq
input = sys.stdin.readline
N, M, T = map(int, input().split())
Graph = defaultdict(list)
MAX = 987654321
for _ in range(M):
    u, v, h = map(int, input().split())
    Graph[u].append([v, h])
def dijkstra(start):
    HQ = []
    for v in Graph[start]:
        heapq.heappush(HQ, [v[1], v[0]])
    result = [MAX] * (N + 1)
    result[start] = 0
    while HQ:
        h, node = heapq.heappop(HQ)

        if result[node] <= h:
            continue
        else:
            result[node] = h
        for v in Graph[node]:
            H = max(h, v[1])
            if result[v[0]] > H:
                heapq.heappush(HQ, [H, v[0]])
    return result

dp = []
for i in range(N + 1):
    dp.append(dijkstra(i))

for _ in range(T):
    start, end = map(int, input().split())
    print(dp[start][end] if dp[start][end] != MAX else -1)
