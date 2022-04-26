from collections import deque
import sys
input = sys.stdin.readline
N, M = map(int, input().split())
arr = []
for _ in range(N):
    arr.append(list(map(int, input().split())))

dx = [1, 0, -1, 0, 1, 1, -1, -1]
dy = [0, 1, 0, -1, 1, -1, 1, -1]
visited = [[False for row in range(M)] for col in range(N)]
def BFS(x, y, visited):
    Queue = deque([[x, y]])
    result = True
    while Queue:
        row, col = Queue.popleft()

        for i in range(8):
            ROW = row + dx[i]
            COL = col + dy[i]
            if 0 <= ROW < M and 0 <= COL < N:
                # 인접한 칸이 더 높으면 현재 탐색한 것이 높은 산봉우리가 아님을 알 수 있다.
                if arr[col][row] < arr[COL][ROW]:
                    result = False

                # 방문했거나 같은 값이 아닌 경우,
                if visited[COL][ROW] or arr[col][row] != arr[COL][ROW]:
                    continue

                visited[COL][ROW] = True
                Queue.append([ROW, COL])
    return result


answer = 0
for col in range(N):
    for row in range(M):
        if not visited[col][row]:
            visited[col][row] = True
            if BFS(row, col, visited):
                answer += 1
print(answer)
