from collections import defaultdict, deque

N, M, R = map(int, input().split())
Graph = defaultdict(list)
for _ in range(M):
    u, v = map(int, input().split())
    Graph[u].append(v)
    Graph[v].append(u)

for key in Graph.keys():
    Graph[key].sort(reverse=True)

def BFS(start):
    Queue = deque([start])
    count = [0] * (N + 1)
    count[start] = 1
    cnt = 1
    while Queue:
        start = Queue.popleft()
        for s in Graph[start]:
            if count[s] != 0:
                continue
            Queue.append(s)
            cnt += 1
            count[s] = cnt
    return count[1:]

print(*BFS(R), sep="\n")