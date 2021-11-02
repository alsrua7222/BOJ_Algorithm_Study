from collections import deque
import sys
input = sys.stdin.readline
dx = [1, 0, -1, 0, -1, -1, 1, 1]
dy = [0, 1, 0, -1, 1, -1, 1, -1]

while True:
    M, H = map(int, input().split())
    if M == H == 0:
        break
    maps = []
    for _ in range(H):
        maps.append(list(map(int, input().split())))

    def BFS(col, row, visited):
        Queue = deque()
        Queue.append([col, row])
        while Queue:
            y, x = Queue.popleft()
            for i in range(8):
                X = x + dx[i]
                Y = y + dy[i]
                if 0 <= X < M and 0 <= Y < H:
                    if visited[Y][X] or maps[Y][X] == 0:
                        continue
                    visited[Y][X] = True
                    Queue.append([Y, X])

    Queue = deque()
    visited = [[False for _ in range(M)] for _ in range(H)]
    answer = 0
    for col in range(H):
        for row in range(M):
            if visited[col][row] or maps[col][row] == 0:
                continue
            visited[col][row] = True
            answer += 1
            BFS(col, row, visited)
    print(answer)
