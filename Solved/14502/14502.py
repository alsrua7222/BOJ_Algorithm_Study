import copy, sys
input = sys.stdin.readline
from collections import deque
from itertools import combinations
N, M = map(int, input().split())
arr = []
for _ in range(N):
    arr.append(list(map(int, input().split())))

# 초기셋팅 - 0의 위치들 좌표계로 반환해서 적재시킨다.
# 또한, 0의 개수를 구한 다음에 벽 3개로 자리 매꿔지므로 -3로 계산한다.
# 또한, 바이러스의 좌표계를 구해서 적재시킨다.
# 또한, 바이러스의 좌표계들로 방문 처리 해놓는다.
positions = []
virus = []
total = 0
for col in range(N):
    for row in range(M):
        if arr[col][row] == 0:
            positions.append([col, row])
            total += 1
        elif arr[col][row] == 2:
            virus.append([col, row])
total -= 3
visited = [[False for _ in range(M)] for _ in range(N)]
for col, row in virus:
    visited[col][row] = True
# 초기셋팅 - 0의 위치들 담긴 좌표계 배열을 벽 3개로 무조건 세워야 하는 경우의 수들을 구해놓음. - 조합론
comb = list(combinations(positions, 3))

# 각 경우의 수에 따라서 바이러스 확산 시뮬레이션을 돌리고 난 다음에 남아있는 0의 개수를 구한다.
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
def BFS():
    Queue = deque(copy.deepcopy(virus))
    visited2 = copy.deepcopy(visited)
    cnt = 0
    while Queue:
        y, x = Queue.popleft()
        for i in range(4):
            X = x + dx[i]
            Y = y + dy[i]
            if 0 <= X < M and 0 <= Y < N:
                if not visited2[Y][X] and arr[Y][X] == 0:
                    visited2[Y][X] = True
                    Queue.append([Y, X])
                    cnt += 1
    return total - cnt

# 모든 경우의 수 중 최댓값을 뽑아내서 출력한다.
answer = 0
for v in comb:
    for col, row in v:
        arr[col][row] = 1
    answer = max(answer, BFS())
    for col, row in v:
        arr[col][row] = 0

print(answer)
