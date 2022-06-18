from collections import deque
N, M = map(int, input().split())
MAP = []
RED, BLUE = [], []
for x in range(N):
    MAP.append(list(input()))
    for y in range(M):
        if MAP[x][y] == 'R':
            RED = [x, y]
        elif MAP[x][y] == 'B':
            BLUE = [x, y]

def BFS():
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    visited = [[[[False] * 10 for _ in range(10)] for _ in range(10)] for _ in range(10)]
    Queue = deque()
    Queue.append([RED[0], RED[1], BLUE[0], BLUE[1], 0])
    visited[RED[0]][RED[1]][BLUE[0]][BLUE[1]] = True
    # 두 개 공이 겹치는 경우
    # 공 사이에 비어있는 자리가 꼭 2개 이상 되어 있다.
    
    while Queue:
        rx, ry, bx, by, cnt = Queue.popleft()
        
        if MAP[rx][ry] == 'O':
            return cnt
        
        for i in range(4):
            nrx, nry = rx, ry
            nbx, nby = bx, by
            rcnt, bcnt = 0, 0
            while MAP[nrx + dx[i]][nry + dy[i]] != '#' and MAP[nrx][nry] != 'O':
                nrx += dx[i]
                nry += dy[i]
                rcnt += 1
            
            while MAP[nbx + dx[i]][nby + dy[i]] != '#' and MAP[nbx][nby] != 'O':
                nbx += dx[i]
                nby += dy[i]
                bcnt += 1
            
            if MAP[nbx][nby] == 'O':
                continue

            if nrx == nbx and nry == nby:
                if rcnt > bcnt: # 빨간공이 더 많이 움직였을 때 뒤로 한칸 빼기
                    nrx -= dx[i]
                    nry -= dy[i]
                else: # 파란공
                    nbx -= dx[i]
                    nby -= dy[i]
            
            if visited[nrx][nry][nbx][nby]:
                continue
            
            if cnt < 10:
                visited[nrx][nry][nbx][nby] = True
                Queue.append([nrx, nry, nbx, nby, cnt + 1])
    return -1

print(BFS())