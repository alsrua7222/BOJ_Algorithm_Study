import sys
from collections import defaultdict
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
V, E = map(int, input().split())
Graph = defaultdict(list)

for _ in range(E):
    u, v = map(int, input().split())
    Graph[u].append(v)
    Graph[v].append(u)

visited = [0] * (V + 1)
idx = 1
cuts = [False] * (V + 1)

def MST_DFS(cur, isRoot, visited):
    global idx
    # 최소 스패닝 트리 DFS를 적용하여 각 정점의 방문 처리에 최소 번호를 부여한다.
    visited[cur] = idx
    idx += 1
    res = visited[cur]

    # 현재 정점의 자식 노드 개수 알아보기.
    child = 0

    for next in Graph[cur]:
        if visited[next] > 0:
            # 현재 번호의 최소 번호보다 다음 번호의 최소 번호가 낮은 순간, 단절점이 아니게 된다.
            res = min(res, visited[next])
            continue

        child += 1
        prev = MST_DFS(next, False, visited)

        # 첫 방문 DFS가 아닌 다음 정점들이고, 현재 번호의 최소 번호가 다음 번호의 최소 번호보다 크지 않으면 단절점이다.
        if not isRoot and prev >= visited[cur]:
            cuts[cur] = True
        res = min(res, prev)

    # 첫 DFS 방문하기 시작한 루트 정점에 자식노드 2개 이상 있으면 무조건 단절점이다.
    if isRoot:
        cuts[cur] = child >= 2

    return res

for i in range(1, V + 1):
    if visited[i] == 0:
        MST_DFS(i, True, visited)

print(sum(cuts))
for i in range(1, V + 1):
    if cuts[i]:
        print(i, end=" ")
