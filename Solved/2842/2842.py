# 풀이 과정
# https://blog.naver.com/alsrua7222/222599620136

from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
dx = [1, 0, -1, 0, 1, 1, -1, -1]
dy = [0, 1, 0, -1, 1, -1, 1, -1]
MAP = []
K_COUNT = 0
P = [0, 0]
for i in range(N):
    info = list(input().rstrip())
    for j in range(N):
        if info[j] == 'K':
            K_COUNT += 1
        elif info[j] == 'P':
            P = [i, j]
    MAP.append(info)

HEIGHT_MAP = []
RANGE_HEIGHT_SET = set()
for _ in range(N):
    heights = list(map(int, input().split()))
    RANGE_HEIGHT_SET.update(heights)
    HEIGHT_MAP.append(heights)

RANGE_HEIGHT_LIST = sorted(RANGE_HEIGHT_SET)

def BFS(low, high):
    answer = 0
    if low > HEIGHT_MAP[P[0]][P[1]] or high < HEIGHT_MAP[P[0]][P[1]]:
        return False

    Queue = deque([P])
    visited = [[False for _ in range(N)] for _ in range(N)]
    visited[P[0]][P[1]] = True
    while Queue:
        y, x = Queue.popleft()
        for i in range(8):
            X = x + dx[i]
            Y = y + dy[i]
            if 0 <= X < N and 0 <= Y < N and not visited[Y][X]:
                visited[Y][X] = True
                if low <= HEIGHT_MAP[Y][X] <= high:
                    if MAP[Y][X] == 'K':
                        answer += 1
                        if answer == K_COUNT:
                            return True
                    Queue.append([Y, X])
    return False

def getMinAnswer():
    x, y = 0, 0
    result = 987654321
    while x < len(RANGE_HEIGHT_LIST) and y < len(RANGE_HEIGHT_LIST):
        if BFS(RANGE_HEIGHT_LIST[x], RANGE_HEIGHT_LIST[y]):
            result = min(RANGE_HEIGHT_LIST[y] - RANGE_HEIGHT_LIST[x], result)
            x += 1
        else:
            y += 1
    return result


print(getMinAnswer())
