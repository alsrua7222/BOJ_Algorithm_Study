from collections import deque
import sys
input = sys.stdin.readline
N, K = map(int, input().split())
arr = []
Queue = []
for col in range(N):
    arr.append(list(map(int, input().split())))
    for row in range(N):
        v = arr[col][row]
        if v != 0:
            Queue.append([v, col, row])

Queue.sort()
Queue = deque(Queue)

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
Queue2 = deque()
S, COL, ROW = map(int, input().split())
for i in range(S):
    if Queue:
        while Queue:
            n, col, row = Queue.popleft()

            for i in range(4):
                X = row + dx[i]
                Y = col + dy[i]
                if 0 <= X < N and 0 <= Y < N:
                    if arr[Y][X] == 0:
                        arr[Y][X] = n
                        Queue2.append([n, Y, X])
    else:
        while Queue2:
            n, col, row = Queue2.popleft()

            for i in range(4):
                X = row + dx[i]
                Y = col + dy[i]
                if 0 <= X < N and 0 <= Y < N:
                    if arr[Y][X] == 0:
                        arr[Y][X] = n
                        Queue.append([n, Y, X])
print(arr[COL - 1][ROW - 1])
