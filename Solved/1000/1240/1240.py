from collections import deque, defaultdict
import sys
input = sys.stdin.readline
N, M = map(int, input().split())
Graph = defaultdict(list)
for _ in range(N - 1):
    u, v, w = map(int, input().split())
    Graph[u].append([v, w])
    Graph[v].append([u, w])

def BFS(start, end):
    Queue = deque([[start, 0]])
    visited = [False] * (N + 1)
    visited[start] = True
    while Queue:
        cur, w = Queue.popleft()

        for next, dist in Graph[cur]:
            if not visited[next]:
                if next == end:
                    return w + dist
                visited[next] = True
                Queue.append([next, w + dist])
    return 0

for _ in range(M):
    s, e = map(int, input().split())
    print(BFS(s, e))
