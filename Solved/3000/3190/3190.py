from collections import deque
import sys
input = sys.stdin.readline
N = int(input())
# 빈 땅 = 0, 사과 = 1
maps = [[0 for _ in range(N)] for _ in range(N)]
# 뱀
K = int(input())
for _ in range(K):
    col, row = map(int, input().split())
    maps[col - 1][row - 1] = 1

L = int(input())
querys = []
for _ in range(L):
    query = list(input().split())
    querys.append([int(query[0]), query[1]])
head = [0, 0]
# 조건
# 1. 시간 업데이트.
answer = 0
# 2. 다음 위치에 있을 정보로 패스 판단.

# 3. 몸통 출동 여부에 따라 종료 or 데큐에 적재.
body = deque()
body.append([0, 0])
# 4. 다음 위치에 사과 여부에 따라 꼬리 늘리고 제거 or 꼬리 그대로.

# 5. 조건된 방향 패턴 수정.
# 오른쪽, 아래쪽, 왼쪽, 위쪽
arrow = 0
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
X, Y = 0, 0
current = 0
while 0 <= X < N and 0 <= Y < N:
    # 1. 시간 업데이트.
    answer += 1

    # 2. 다음 위치에 있을 정보로 패스 판단.
    X, Y = X + dx[arrow], Y + dy[arrow]
    if 0 <= X < N and 0 <= Y < N:
        next_head = [Y, X]
    else:
        break

    # 3. 몸통 출동 여부에 따라 종료 or 데큐에 적재.
    if next_head in body:
        break
    body.append(next_head)
    # 4. 다음 위치에 사과 여부에 따라 꼬리 늘리기 or 오래된 꼬리 제거.
    if maps[Y][X] == 0:
        body.popleft()
    else:
        maps[Y][X] = 0

    # 5. 조건된 방향 패턴 수정.
    if L > current:
        if querys[current][0] == answer:
            if querys[current][1] == 'D':
                arrow = (arrow + 1) % 4
            else:
                arrow = (arrow - 1) % 4 if arrow != 0 else 3
            current += 1

print(answer)
