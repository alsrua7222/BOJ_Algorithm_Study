N = int(input())
def checkVisited(x, y, visited, cnt):
    visited = priority_visited(x, y, visited, cnt)
    for col in range(N):
        if col == y:
            continue
        visited = priority_visited(x, col, visited, cnt)
    for row in range(N):
        if row == x:
            continue
        visited = priority_visited(row, y, visited, cnt)
    for i in range(1, N):
        if 0 <= x + i < N and 0 <= y + i < N:
            visited = priority_visited(x + i, y + i, visited, cnt)
        if 0 <= x - i < N and 0 <= y - i < N:
            visited = priority_visited(x - i, y - i, visited, cnt)
        if 0 <= x + i < N and 0 <= y - i < N:
            visited = priority_visited(x + i, y - i, visited, cnt)
        if 0 <= x - i < N and 0 <= y + i < N:
            visited = priority_visited(x - i, y + i, visited, cnt)
    return visited

def priority_visited(x, y, visited, cnt):
    if visited[y][x] == cnt:
        visited[y][x] = 0
    elif visited[y][x] == 0:
        visited[y][x] = cnt
    return visited

def DFS(x, y, visited, cnt):
    if cnt == N:
        global answer
        answer += 1
        return
    for row in range(x, N):
        if not visited[y][row] != 0:
            visited = checkVisited(row, y, visited, cnt + 1)
            DFS(row, y, visited, cnt + 1)
            visited = checkVisited(row, y, visited, cnt + 1)
    x = 0
    y += 1
    for col in range(y, N):
        for row in range(x, N):
            if visited[col][row] != 0:
                continue
            visited = checkVisited(row, col, visited, cnt + 1)
            DFS(row, col, visited, cnt + 1)
            visited = checkVisited(row, col, visited, cnt + 1)

answer = 0
visited = [[0 for i in range(N)] for j in range(N)]
DFS(0, 0, visited, 0)
print(answer)
