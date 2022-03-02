# 풀이 과정
# https://blog.naver.com/alsrua7222/222662334337

import sys
input = sys.stdin.readline
from collections import deque
N, L, R = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]


def BFS(x, y, visited, date):
    Queue = deque()
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]

    visited[x][y] = date
    Queue.append([x, y])
    collect = [[x, y]]
    SUM = arr[x][y]
    while Queue:
        x, y = Queue.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N:
                if visited[nx][ny] != date and L <= abs(arr[nx][ny] - arr[x][y]) <= R:
                    visited[nx][ny] = date
                    Queue.append([nx, ny])
                    collect.append([nx, ny])
                    SUM += arr[nx][ny]
    
    if len(collect) > 1:
        SUM //= len(collect)
        while collect:
            x, y = collect.pop()
            arr[x][y] = SUM
            query.append([x, y])
        return True
    
    return False

answer = 0
visited = [[-1 for _ in range(N)] for _ in range(N)]
query = deque([(i, j) for i in range(N) for j in range(N)])

while True:
    success = True
    for _ in range(len(query)):
        x, y = query.popleft()
        if visited[x][y] != answer:
            if BFS(x, y, visited, answer):
                success = False
    if success:
        break
    else:
        answer += 1
print(answer)