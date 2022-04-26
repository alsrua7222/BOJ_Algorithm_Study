import sys
sys.setrecursionlimit(10**6)
from collections import defaultdict
input = sys.stdin.readline
N, M = map(int, input().split())
Graph = defaultdict(list)
for _ in range(M):
    u, v = map(int, input().split())
    Graph[u].append(v)
    Graph[v].append(u)

def DFS(start, visited):
    for node in Graph[start]:
        if not visited[node]:
            visited[node] = True
            DFS(node, visited)
    return

# 셋팅
answer = 0
visited = [False] * (N + 1)

for i in range(1, N + 1):
    if not visited[i]:
        # 방문 하지 않은 인덱스라면
        DFS(i, visited)
        answer += 1

# # 사후 처리 1번째 부터 체크
# for v in visited[1:]:
#     if not v:
#         answer += 1
print(answer)
