# 풀이 과정
# https://blog.naver.com/alsrua7222/222614979398
import sys
from collections import defaultdict
input = sys.stdin.readline

N, M = map(int, input().split())
dx = [-1, 0, 1, -1, 0, 1, -1, 0, 1]
dy = [1, 1, 1, 0, 0, 0, -1, -1, -1]

I = []
arr = []
Points = defaultdict(int)
for i in range(N):
    arr.append(list(input().rstrip()))
    for j in range(M):
        if arr[-1][j] == 'I':
            I = [i, j]
        elif arr[-1][j] == 'R':
            Points[(i, j)] = 1
        arr[-1][j] = '.'
query = list(map(int, list(input().rstrip())))

def moveNcheck(n):
    I[1] += dx[n - 1]
    I[0] += dy[n - 1]
    if tuple(I) in Points:
        return False
    return True

def IsAlive():
    result = defaultdict(int)

    # R의 위치들을 처리.
    for key in Points.keys():
        Ry, Rx = key
        choice = [987654321, 4]
        for i in range(9):
            dist = abs(I[1] - (Rx + dx[i])) + abs(I[0] - (Ry + dy[i]))
            # 상대 거리가 0이라면 겹쳤다는 신호. 즉, 종료.
            if dist == 0:
                return False
            if choice[0] > dist:
                choice = [dist, i]

        Ry += dy[choice[1]]
        Rx += dx[choice[1]]
        result[(Ry, Rx)] += 1

    # Points맵 새롭게 바꾸고 바인딩.
    # 겹친 위치에 2개이상은 파괴하므로, 추가하지 않음.
    Points.clear()
    for key, value in result.items():
        if value < 2:
            Points[key] = 1

    return True

# 쿼리 실행
for i in range(len(query)):
    if not moveNcheck(query[i]) or not IsAlive():
        print("kraj", i + 1)
        exit(0)

# 맵 정보 갱신
arr[I[0]][I[1]] = 'I'
for Ry, Rx in Points.keys():
    arr[Ry][Rx] = 'R'
for v in arr:
    print(''.join(v))
