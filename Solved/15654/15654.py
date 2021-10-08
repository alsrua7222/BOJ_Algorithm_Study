N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
arr = list(map(str, arr))
def DFS(visited, cnt, items):
    if cnt == M:
        print(' '.join(items))
        return
    for i in range(N):
        if not visited[i]:
            visited[i] = True
            DFS(visited, cnt + 1, items + [arr[i]])
            visited[i] = False
visited = [False] * (N + 1)
DFS(visited, 0, [])
