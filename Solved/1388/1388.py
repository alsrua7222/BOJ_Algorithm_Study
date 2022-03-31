# 풀이 과정
# https://blog.naver.com/alsrua7222/222688394812

from collections import deque
N, M = map(int, input().split())
arr = [list(input().rstrip()) for _ in range(N)]

answer = 0
visited = [[False] * M for _ in range(N)]
def BFS(char, x, y):
    visited[x][y] = True
    Queue = deque([(x, y)])
    dx = [1, -1] if char == '|' else [0, 0]
    dy = [1, -1] if char == '-' else [0, 0]
    while Queue:
        x, y = Queue.popleft()
        for i in range(2):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny] and arr[nx][ny] == char:
                Queue.append((nx, ny))
                visited[nx][ny] = True
    return

for i in range(N):
    for j in range(M):
        if visited[i][j]:
            continue
        answer += 1
        BFS(arr[i][j], i, j)
print(answer)