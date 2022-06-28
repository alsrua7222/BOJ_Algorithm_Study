from collections import deque
N = int(input())
MAP = []
start, end = [], []
for i in range(N):
    MAP.append(list(input()))
    for j in range(N):
        if MAP[i][j] == '#':
            if start:
                end = [i, j]
            else:
                start = [i, j]
                MAP[i][j] = '.'

def BFS(x, y):
    dxy = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    Queue = deque()
    visited = [[[0] * 4 for _ in range(N)] for _ in range(N)]
    
    for i in range(4):
        Queue.append([x, y, i])
        visited[x][y][i] = 1
    
    while Queue:
        x, y, dir = Queue.popleft()
        dx, dy = dxy[dir]
        nx, ny = x, y
        while True:
            nx += dx
            ny += dy

            if 0 <= nx < N and 0 <= ny < N:
                if MAP[nx][ny] == '*':
                    break
                if MAP[nx][ny] == '!':
                    if visited[nx][ny][dir] == 0:
                        Queue.append([nx, ny, dir])
                        visited[nx][ny][dir] = visited[x][y][dir]
                    if visited[nx][ny][(dir + 1) % 4] == 0:
                        Queue.append([nx, ny, (dir + 1) % 4])
                        visited[nx][ny][(dir + 1) % 4] = visited[x][y][dir] + 1
                    if visited[nx][ny][(dir - 1) % 4] == 0:
                        Queue.append([nx, ny, (dir - 1) % 4])
                        visited[nx][ny][(dir - 1) % 4] = visited[x][y][dir] + 1
                if MAP[nx][ny] == '#':
                    return visited[x][y][dir] - 1
            else:
                break
    # 무조건 정답을 주어져서 대충 반환
    return -1

print(BFS(*start))