from collections import deque
def BFS(MAP, H, W):
    dxy = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    ret = 0
    visited = [[False] * W for _ in range(H)]
    for i in range(H):
        for j in range(W):
            if not visited[i][j] and MAP[i][j] == '#':
                q = deque()
                q.append((i, j))
                visited[i][j] = True
                while q:
                    x, y = q.popleft()
                    for dx, dy in dxy:
                        nx, ny = x + dx, y + dy
                        if 0 <= nx < H and 0 <= ny < W and not visited[nx][ny] and MAP[nx][ny] == '#':
                            q.append((nx, ny))
                            visited[nx][ny] = True
                ret += 1
    return ret

for _ in range(int(input())):
    H, W = map(int, input().split())
    MAP = [list(input()) for _ in range(H)]

    print(BFS(MAP, H, W))