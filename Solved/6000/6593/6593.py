from collections import deque
while True:
    L, R, C = map(int, input().split())
    if L == R == C == 0:
        break

    start = []
    MAP = []
    for z in range(L):
        layer = []
        for y in range(R):
            layer.append(list(input()))
            for x in range(C):
                if layer[y][x] == 'S':
                    start = [z, y, x]
        input()
        MAP.append(layer)
    
    def bfs():
        dxy = [(-1, 0, 0), (1, 0, 0), (0, -1, 0), (0, 1, 0), (0, 0, -1), (0, 0, 1)]
        q = deque([start + [0]])
        visited = [[[False] * C for _ in range(R)] for _ in range(L)]
        visited[start[0]][start[1]][start[2]] = True
        while q:
            z, y, x, d = q.popleft()
            for dx, dy, dz in dxy:
                nz, ny, nx = z + dx, y + dy, x + dz
                if 0 <= nz < L and 0 <= ny < R and 0 <= nx < C:
                    if MAP[nz][ny][nx] != '#' and not visited[nz][ny][nx]:
                        if MAP[nz][ny][nx] == 'E':
                            return f"Escaped in {d + 1} minute(s)."
                        visited[nz][ny][nx] = True
                        q.append([nz, ny, nx, d + 1])
        return "Trapped!"
    print(bfs())