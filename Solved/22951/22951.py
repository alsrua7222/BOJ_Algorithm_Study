N, K = map(int, input().split())
arr = []
for _ in range(N):
    arr.append(list(map(int, input().split())))
visited = [[False for _ in range(K)] for _ in range(N)]

x, y = 0, 0
visited[y][x] = True
cnt = 1
while cnt != N * K:
    num = arr[y][x]
    i = 0
    while i < num:
        x += 1
        if x == K:
            x = 0
            y += 1
        if y == N:
            y = 0
        if not visited[y][x]:
            i += 1
    visited[y][x] = True
    cnt += 1
print(y + 1, arr[y][x])
