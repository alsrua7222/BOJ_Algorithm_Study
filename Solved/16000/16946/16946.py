from collections import deque
import sys
input = sys.stdin.readline
N, M = map(int, input().split())

# input initialize base map.
arr = []
# groups map for dp map.
group_arr = [[0 for row in range(M)] for col in range(N)]
group_index_arr = [[0 for row in range(M)] for col in range(N)]
group_cnt = 2
# result map
result_map = []

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

for _ in range(N):
    arr.append(input().rstrip())

def setDP(x, y, visited):
    global group_cnt
    global group_arr

    Queue = deque()
    Queue.append([x, y])
    group_index_arr[y][x] = group_cnt
    answer = 1
    visited[y][x] = True

    # 지나간 자리에 지날 수 있는 최대 길이 값을 부여하기.
    index_q = deque()
    index_q.append([x, y])
    while Queue:
        tmpx, tmpy = Queue.popleft()
        for i in range(4):
            X = tmpx + dx[i]
            Y = tmpy + dy[i]
            if 0 <= X < M and 0 <= Y < N:
                if not visited[Y][X] and arr[Y][X] == '0' and group_arr[Y][X] == 0:
                    answer += 1
                    visited[Y][X] = True
                    group_index_arr[Y][X] = group_cnt
                    index_q.append([X, Y])
                    Queue.append([X, Y])

    while index_q:
        tmpx, tmpy = index_q.popleft()
        group_arr[tmpy][tmpx] = answer

    # 그룹 묶어주고 나서 1씩 증가해서 다음 그룹에 사용하도록 한다.
    group_cnt += 1
    return


def getCount(x, y):
    answer = 1

    # 0의 그룹 번호가 일치하면 카운트 못 세도록 함.
    group = set()

    for i in range(4):
        X = x + dx[i]
        Y = y + dy[i]
        if 0 <= X < M and 0 <= Y < N:
            if arr[Y][X] == '0' and group_index_arr[Y][X] not in group:
                answer += group_arr[Y][X]
                group.add(group_index_arr[Y][X])
    return answer % 10

visited = [[False for row in range(M)] for col in range(N)]
for col in range(N):
    for row in range(M):
        if not visited[col][row] and arr[col][row] == '0':
            setDP(row, col, visited)


for col in range(N):
    tmp = ""
    for row in range(M):
        if arr[col][row] == '1':
            tmp += str(getCount(row, col))
        else:
            tmp += '0'
    result_map.append(tmp)

for v in result_map:
    print(v)
