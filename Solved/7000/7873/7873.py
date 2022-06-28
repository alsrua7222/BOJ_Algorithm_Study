from collections import deque
import sys
input = sys.stdin.readline

for _ in range(int(input())):
    N, M = map(int, input().split())
    MAP = [list(input().rstrip()) for _ in range(N)]

    visited = [[False] * M for _ in range(N)]
    def IsScope(x, y):
        return 0 <= x < N and 0 <= y < M
    def IsCorrect(x, y, alpha, dx, dy):
        if alpha != 'A' and MAP[x][y] == 'F':
            return True
        
        if alpha == 'B':
            if dy == -1:
                return MAP[x][y] in "DE"
            if dx == 1:
                return MAP[x][y] in "CD"
        elif alpha == 'C':
            if dy == -1:
                return MAP[x][y] in "DE"
            if dx == -1:
                return MAP[x][y] in "BE"
        elif alpha == 'D':
            if dy == 1:
                return MAP[x][y] in "BC"
            if dx == -1:
                return MAP[x][y] in "BE"
        elif alpha == 'E':
            if dy == 1:
                return MAP[x][y] in "BC"
            if dx == 1:
                return MAP[x][y] in "CD"
        elif alpha == 'F':
            if dy == -1:
                return MAP[x][y] in "DE"
            if dy == 1:
                return MAP[x][y] in "BC"
            if dx == -1:
                return MAP[x][y] in "BE"
            if dx == 1:
                return MAP[x][y] in "CD"
        return False
    def BFS(x, y):
        Queue = deque()
        Queue.append([x, y])
        visited[x][y] = True
        while Queue:
            x, y = Queue.popleft()
            
            if MAP[x][y] == 'B':
                if IsScope(x + 1, y) and not visited[x + 1][y]:
                    if IsCorrect(x + 1, y, MAP[x][y], 1, 0):
                        visited[x + 1][y] = True
                        Queue.append([x + 1, y])
                if IsScope(x, y - 1) and not visited[x][y - 1]:
                    if IsCorrect(x, y - 1, MAP[x][y], 0, -1):
                        visited[x][y - 1] = True
                        Queue.append([x, y - 1])
            elif MAP[x][y] == 'C':
                if IsScope(x, y - 1) and not visited[x][y - 1]:
                    if IsCorrect(x, y - 1, MAP[x][y], 0, -1):
                        visited[x][y - 1] = True
                        Queue.append([x, y - 1])
                if IsScope(x - 1, y) and not visited[x - 1][y]:
                    if IsCorrect(x - 1, y, MAP[x][y], -1, 0):
                        visited[x - 1][y] = True
                        Queue.append([x - 1, y])
            elif MAP[x][y] == 'D':
                if IsScope(x - 1, y) and not visited[x - 1][y]:
                    if IsCorrect(x - 1, y, MAP[x][y], -1, 0):
                        visited[x - 1][y] = True
                        Queue.append([x - 1, y])
                if IsScope(x, y + 1) and not visited[x][y + 1]:
                    if IsCorrect(x, y + 1, MAP[x][y], 0, 1):
                        visited[x][y + 1] = True
                        Queue.append([x, y + 1])
            elif MAP[x][y] == 'E':
                if IsScope(x, y + 1) and not visited[x][y + 1]:
                    if IsCorrect(x, y + 1, MAP[x][y], 0, 1):
                        visited[x][y + 1] = True
                        Queue.append([x, y + 1])
                if IsScope(x + 1, y) and not visited[x + 1][y]:
                    if IsCorrect(x + 1, y, MAP[x][y], 1, 0):
                        visited[x + 1][y] = True
                        Queue.append([x + 1, y])
            elif MAP[x][y] == 'F':
                if IsScope(x, y - 1) and not visited[x][y - 1]:
                    if IsCorrect(x, y - 1, MAP[x][y], 0, -1):
                        visited[x][y - 1] = True
                        Queue.append([x, y - 1])
                if IsScope(x - 1, y) and not visited[x - 1][y]:
                    if IsCorrect(x - 1, y, MAP[x][y], -1, 0):
                        visited[x - 1][y] = True
                        Queue.append([x - 1, y])
                if IsScope(x, y + 1) and not visited[x][y + 1]:
                    if IsCorrect(x, y + 1, MAP[x][y], 0, 1):
                        visited[x][y + 1] = True
                        Queue.append([x, y + 1])
                if IsScope(x + 1, y) and not visited[x + 1][y]:
                    if IsCorrect(x + 1, y, MAP[x][y], 1, 0):
                        visited[x + 1][y] = True
                        Queue.append([x + 1, y])
        return
    
    answer = 0
    for i in range(N):
        for j in range(M):
            if MAP[i][j] != 'A' and not visited[i][j]:
                BFS(i, j)
                answer += 1
    print(answer)