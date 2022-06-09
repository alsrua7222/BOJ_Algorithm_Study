from collections import deque
M, N = map(int, input().split())

def makeBit(n):
    tmp = bin(n)[2:]
    if len(tmp) != 4:
        tmp = '0' * (4 - len(tmp)) + tmp
    return tmp

MAP = []
for _ in range(N):
    query = list(map(int, input().split()))
    tmp = []
    for v in query:
        tmp.append(list(makeBit(v)))
    MAP.append(tmp)

# print(MAP)
# 2진수 비트 성분 = 1 벽 있음, 0 벽 없음
# 1 = 서쪽, 2 = 북쪽, 4 = 동쪽, 8 = 남쪽
# [남, 동, 북, 서]
# 다 합쳐진 숫자 = 15 = 다 있음, 11 = 북쪽, 동쪽, 남쪽 있음

Points = [[0] * M for _ in range(N)]
Groups = [[-1] * M for _ in range(N)]

def getPoints():
    visited = [[False] * M for _ in range(N)]
    dxy = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    groupIdx = 0
    for i in range(N):
        for j in range(M):
            if visited[i][j]:
                continue

            visited[i][j] = True
            Queue = deque([(i, j)])
            Stack = [(i, j)]
            MAX = 1
            while Queue:
                x, y = Queue.popleft()
                for idx in range(4):
                    nx, ny = x + dxy[idx][0], y + dxy[idx][1]
                    if 0 <= nx < N and 0 <= ny < M:
                        if visited[nx][ny] or MAP[x][y][idx] == '1':
                            continue
                        visited[nx][ny] = True
                        MAX += 1
                        Queue.append((nx, ny))
                        Stack.append((nx, ny))
            
            for x, y in Stack:
                Points[x][y] = MAX
                Groups[x][y] = groupIdx
            groupIdx += 1
    return groupIdx

def getMax():
    MAX = [0, 0]
    dxy = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    for i in range(N):
        for j in range(M):
            MAX[0] = max(MAX[0], Points[i][j])
            for idx in range(4):
                nx, ny = i + dxy[idx][0], j + dxy[idx][1]
                if 0 <= nx < N and 0 <= ny < M:
                    if MAP[i][j][idx] == '1':
                        if Groups[i][j] == Groups[nx][ny]:
                            MAX[1] = max(MAX[1], Points[i][j])
                        else:
                            MAX[1] = max(MAX[1], Points[i][j] + Points[nx][ny])
    return MAX
                        
print(getPoints())
print(*getMax(), sep="\n")