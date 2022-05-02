from collections import deque
N, M = map(int, input().split())
MAP = []
start = [0, 0]
goal = []
for i in range(N):
    MAP.append(list(input().rstrip()))
    for j in range(M):
        if MAP[i][j] == 'S':
            start = [i, j]
        elif MAP[i][j] == 'C':
            goal.append([i, j])            

def changeStatus(x, y, status):
    new_status = status
    if goal[0] == [x, y]:
        if new_status == 0:
            new_status = 1
        elif new_status == 2:
            new_status = 3
    elif goal[1] == [x, y]:
        if new_status == 0:
            new_status = 2
        elif new_status == 1:
            new_status = 3
    return new_status

def BFS():
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]

    Queue = deque()
    Queue.append([0, start[0], start[1], -1, 0]) # 0: 방문 횟수, 1: x, 2: y, 3: 방향, 4: 두 곳 방문 체크
    
    # 방문 체크
    visited = [[[[False] * 4 for _ in range(4)] for _ in range(M)] for _ in range(N)] # x, y, 방향, 두 곳 방문 체크
    for i in range(4):
        visited[start[0]][start[1]][i][0] = True

    while Queue:
        cnt, x, y, dir, status = Queue.popleft()

        for i in range(4):
            if dir == i: # 같은 방향이면 무시.
                continue

            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M and MAP[nx][ny] != '#':
                if not visited[nx][ny][i][status]:
                    next_status = status
                    if MAP[nx][ny] == 'C':
                        next_status = changeStatus(nx, ny, status)
                        if next_status == 3:
                            return cnt + 1
                    visited[nx][ny][i][status] = True
                    Queue.append([cnt + 1, nx, ny, i, next_status])
    return -1
print(BFS())