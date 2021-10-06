from collections import defaultdict
import heapq, sys
input = sys.stdin.readline

N = int(input())
M = int(input())
Graph = defaultdict(list)
for _ in range(M):
    cur, pov, w = map(int, input().split())
    Graph[cur].append([pov, w])
    # Graph[pov].append([cur, w])

def BFS():
    Queue = []
    dist = [987654321] * (N + 1)
    dist[start] = 0
    heapq.heappush(Queue, [0, start])
    while Queue:
        w, cur = heapq.heappop(Queue)
        if w > dist[cur]:
            continue
        for i, v in Graph[cur]:
            tmp = v + w
            if dist[i] > tmp:
                dist[i] = tmp
                heapq.heappush(Queue, [v + w, i])

    return dist[end]

start, end = map(int, input().split())
print(BFS())
