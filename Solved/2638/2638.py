from collections import deque
import sys
input = sys.stdin.readline
N, M = map(int, input().split())
arr = []
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
for _ in range(N):
    arr.append(list(map(int, input().split())))

# 외부공기 분류. = 2
Queue = deque()
Queue.append([0, 0])
visited = [[False for row in range(M)] for col in range(N)]
visited[0][0] = True
arr[0][0] = 2
while Queue:
    y, x = Queue.popleft()

    for i in range(4):
        X = x + dx[i]
        Y = y + dy[i]
        if 0 <= X < M and 0 <= Y < N:
            if visited[Y][X]:
                continue
            if arr[Y][X] == 0:
                visited[Y][X] = True
                arr[Y][X] = 2
                Queue.append([Y, X])

# 시계열 특성있기에 2개의 데큐로 번갈아 사용.
Before = deque()
After = deque()

# 처음에 녹일 수 있는 치즈 위치 찾기.
for col in range(N):
    for row in range(M):
        if arr[col][row] == 1:
            Before.append([col, row])

def make_airs(row, col):
    Queue.append([col, row])
    visited[col][row] = True
    arr[col][row] = 2
    while Queue:
        y, x = Queue.popleft()
        for i in range(4):
            X = x + dx[i]
            Y = y + dy[i]
            if 0 <= X < M and 0 <= Y < N:
                if arr[Y][X] == 0 and not visited[Y][X]:
                    Queue.append([Y, X])
                    visited[Y][X] = True
                    arr[Y][X] = 2
    return


def meltingCheese(Input, Output):
    remove_cheese = deque()
    Airs = deque()
    while Input:
        y, x = Input.popleft()
        cnt = 0
        IsAir = []
        for i in range(4):
            X = x + dx[i]
            Y = y + dy[i]
            if 0 <= X < M and 0 <= Y < N:
                if arr[Y][X] == 2:
                    cnt += 1
                elif arr[Y][X] == 0:
                    # 녹은 치즈 주변에 있는 내부 공기.
                    IsAir.append([Y, X])

        if cnt >= 2:
            # 내부 공기를 외부 공기로 만들기.
            if IsAir:
                Airs.append(IsAir[0])
            remove_cheese.append([y, x])
        else:
            Output.append([y, x])
    # 사후 처리
    while Airs:
        y, x = Airs.popleft()
        make_airs(x, y)
    while remove_cheese:
        y, x = remove_cheese.popleft()
        arr[y][x] = 2
    return

# 치즈 다 녹을 때까지 반복 수행.
answer = 0
while Before or After:
    if Before:
        meltingCheese(Before, After)
    elif After:
        meltingCheese(After, Before)
    answer += 1

print(answer)
