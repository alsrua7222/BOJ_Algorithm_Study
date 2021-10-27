from collections import defaultdict, deque
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
V, E = map(int, input().split())

Graph = defaultdict(list)
R_Graph = defaultdict(list)
stack = deque()

for _ in range(E):
    u, v = map(int, input().split())
    Graph[u].append(v)
    R_Graph[v].append(u)

def DFS_SCC(cur, visited):
    for next in Graph[cur]:
        if visited[next]:
            continue
        visited[next] = True
        DFS_SCC(next, visited)
    stack.append(cur)

def DFS_R_SCC(cur, visited):
    global tmp
    for next in R_Graph[cur]:
        if visited[next]:
            continue
        visited[next] = True
        DFS_R_SCC(next, visited)
    tmp.append(cur)

# DFS_SCC 방문해서 stack에 쌓기 시작.
visited = [False] * (V + 1)
for i in range(1, V + 1):
    if not visited[i]:
        visited[i] = True
        DFS_SCC(i, visited)

# DFS_R_SCC 방문해서 stack에 있는 원소 뺀 후 방문처리 안되면 탐색하면서 SCC인지 체크.
visited = [False] * (V + 1)
answer = []
while stack:
    node = stack.pop()
    if visited[node]:
        continue
    visited[node] = True
    tmp = []
    DFS_R_SCC(node, visited)
    tmp.sort()
    answer.append(tmp)

# 출력.
print(len(answer))
answer.sort(key=lambda x: (x[0]))
for v in answer:
    for v2 in v:
        print(v2, end=" ")
    print(-1)
