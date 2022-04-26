from collections import defaultdict
N = int(input())
arr = list(map(int, input().split()))
cut = int(input())
Graph = defaultdict(list)
for i in range(N):
    Graph[arr[i]].append(i)
visited = [False] * (N + 1)
visited[cut] = True

def DFS(start, visited):
    global answer

    # 단말 노드라면,
    if start not in Graph:
        answer += 1
        return

    # 경로가 하나밖에 없는 간선이고, 그 앞 노드가 방문 처리 되어 있다면,
    if len(Graph[start]) == 1 and visited[Graph[start][0]]:
        answer += 1
        return

    # DFS 탐색.
    for v in Graph[start]:
        if visited[v]:
            continue
        visited[v] = True
        DFS(v, visited)
    return

answer = 0
for v in Graph[-1]:
    if visited[v]:
        continue
    visited[v] = True
    DFS(v, visited)

print(answer)