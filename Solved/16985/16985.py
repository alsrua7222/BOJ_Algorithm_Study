# 풀이 과정
# https://blog.naver.com/alsrua7222/222640647231

from heapq import *
from collections import deque

def getInfoMap(MAP):
    left90 = [[0] * 5 for _ in range(5)]
    right90 = [[0] * 5 for _ in range(5)]
    oppsite180 = [[0] * 5 for _ in range(5)]
    for i in range(5):
        for j in range(5):
            left90[4 - j][i] = MAP[i][j]
            right90[j][4 - i] = MAP[i][j]
            oppsite180[4 - i][4 - j] = MAP[i][j]
    return [left90, right90, oppsite180]

arr = []
answer = 987654321
set_collect = set()
for _ in range(5):
    tmp = []
    for _ in range(5):
        tmp.append(list(map(int, input().split())))
    arr.append([tmp] + getInfoMap(tmp))

def A_Pointer(MAP_3D):
    global answer
    dx = [1, 0, -1, 0, 0, 0]
    dy = [0, -1, 0, 1, 0, 0]
    dz = [0, 0, 0, 0, 1, -1]

    dist = [[[256 for _ in range(5)] for _ in range(5)] for _ in range(5)]
    dist[0][0][0] = 0
    HQ = []
    heappush(HQ, [12, 0, 0, 0, 0])

    while HQ:
        d, w, x, y, z = heappop(HQ)

        for i in range(6):
            X = x + dx[i]
            Y = y + dy[i]
            Z = z + dz[i]
            if 0 <= X < 5 and 0 <= Y < 5 and 0 <= Z < 5:
                if MAP_3D[Z][X][Y] == 0 or dist[Z][X][Y] <= w + 1:
                    continue
                if Z == X == Y == 4:
                    answer = min(answer, w + 1)
                    return
                dist[Z][X][Y] = w + 1
                heappush(HQ, [12 - Z - X - Y, w + 1, X, Y, Z])
    return

def BFS(MAP_3D):
    global answer
    dx = [1, 0, -1, 0, 0, 0]
    dy = [0, -1, 0, 1, 0, 0]
    dz = [0, 0, 0, 0, 1, -1]

    visited = [[[False for _ in range(5)] for _ in range(5)] for _ in range(5)]
    visited[0][0][0] = True
    # Queue formatting => x, y, z, weight
    Queue = deque([[0, 0, 0, 0]])

    while Queue:
        x, y, z, w = Queue.popleft()
        for i in range(6):
            X = x + dx[i]
            Y = y + dy[i]
            Z = z + dz[i]
            if 0 <= X < 5 and 0 <= Y < 5 and 0 <= Z < 5:
                if visited[Z][X][Y] or MAP_3D[Z][X][Y] == 0:
                    continue
                elif answer <= w + 1:
                    return
                if X == Y == Z == 4:
                    answer = w + 1
                    return
                visited[Z][X][Y] = True
                Queue.append([X, Y, Z, w + 1])
    return

def solve(collect):
    # 4 * 4 * 4 * 4 * 4
    for a in range(4):
        if arr[collect[0]][a][0][0] == 0:
            continue
        for b in range(4):
            for c in range(4):
                for d in range(4):
                    for e in range(4):
                        if arr[collect[4]][e][4][4] == 0:
                            continue
                        MAP_3D = [arr[collect[0]][a], arr[collect[1]][b], arr[collect[2]][c], arr[collect[3]][d], arr[collect[4]][e]]
                        A_Pointer(MAP_3D)
                        # BFS(MAP_3D)
    return

def permutations(cur, collect):
    if cur == 5:
        if tuple(collect[::-1]) in set_collect:
            return
        set_collect.add(tuple(collect))
        solve(collect)
        return
    for i in range(5):
        if i in collect:
            continue
        permutations(cur + 1, collect + [i])
    return

permutations(0, [])
print(answer if answer != 987654321 else -1)