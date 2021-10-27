from collections import deque, defaultdict
import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline
for _ in range(int(input())):
    N, M = map(int, input().split())
    Graph = defaultdict(list)
    stack = deque()
    for _ in range(M):
        A, B = map(int, input().split())
        Graph[A].append(B)

    def DFS_SCC(start, visited):
        for v in Graph[start]:
            if visited[v]:
                continue
            visited[v] = True
            DFS_SCC(v, visited)
        stack.append(start)
        return

    def DFS2_SCC(start, visited):
        for v in Graph[start]:
            if visited[v]:
                continue
            visited[v] = True
            DFS2_SCC(v, visited)
        return

    # SCC 위한 DFS 탐색.
    visited = [False] * (N + 1)
    for i in range(1, N + 1):
        if not visited[i]:
            visited[i] = True
            DFS_SCC(i, visited)

    # 분리된 스택 정리.
    visited = [False] * (N + 1)
    cnt = 0
    while stack:
        node = stack.pop()
        if not visited[node]:
            visited[node] = True
            cnt += 1
            DFS2_SCC(node, visited)
    print(cnt)
