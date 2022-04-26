from collections import deque, defaultdict
import sys
input = sys.stdin.readline
N = int(input())
Graph = defaultdict(list)
for _ in range(N - 1):
    A, B = map(int, input().split())
    Graph[A].append(B)
    Graph[B].append(A)

Queue = deque()
Queue.append(1)
visited = [False] * (N + 1)
visited[1] = True
parents = [0] * (N + 1)
while Queue:
    cur = Queue.popleft()
    for v in Graph[cur]:
        if not visited[v]:
            visited[v] = True
            parents[v] = cur
            Queue.append(v)

for v in parents[2:]:
    print(v)
