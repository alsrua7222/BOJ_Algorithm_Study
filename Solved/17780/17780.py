# 풀이 과정
# https://blog.naver.com/alsrua7222/222668861876

import sys
input = sys.stdin.readline

# right -> left -> up -> down
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

N, K = map(int, input().split())
arr = [[2] + list(map(int, input().split())) + [2] for _ in range(N)]
arr.insert(0, [2] * (N + 2))
arr.append([2] * (N + 2))

stack_2d = [[list() for _ in range(N + 2)] for _ in range(N + 2)]
info = [] # x, y, direction, number
for i in range(K):
    info.append(list(map(int, input().split())) + [i])
    stack_2d[info[i][0]][info[i][1]].append(info[i][3])

def directionReverse(direction):
    if direction == 1:
        return 2
    elif direction == 2:
        return 1
    elif direction == 3:
        return 4
    elif direction == 4:
        return 3
    else:
        return direction

def move(x, y, cur):
    """
    x, y: 좌표
    cur: 현재 번호
    return: True(스택 4개 이상) or False(나머지)
    """
    # 스택 맨 바닥이 현재 번호랑 일치하면,
    if stack_2d[x][y][0] == cur:
        X = x + dx[info[cur][2] - 1]
        Y = y + dy[info[cur][2] - 1]
        
        # 먼저 경계선 밖 or 파랑 타일 일 경우
        if arr[X][Y] == 2:
            tmpX = x - dx[info[cur][2] - 1]
            tmpY = y - dy[info[cur][2] - 1]
            
            # 거꾸로 바꿔도 파랑 타일일 경우 방향만 바꾸고 종료
            info[cur][2] = directionReverse(info[cur][2])
            if arr[tmpX][tmpY] == 2:
                return
            # 아닐 경우 거꾸로 가는 값으로 바꿔줌
            X = tmpX
            Y = tmpY
        
        if arr[X][Y] == 1: # 레드 타일
            for v in stack_2d[x][y][::-1]:
                info[v][0:2] = [X, Y]
                stack_2d[X][Y].append(v)
            stack_2d[x][y] = []
        else: # 하양 타일
            for v in stack_2d[x][y]:
                info[v][0:2] = [X, Y]
                stack_2d[X][Y].append(v)
            stack_2d[x][y] = []
        
        # 만약 스택이 4개 이상이면, 스택을 제거하고 종료
        if len(stack_2d[X][Y]) >= 4:
            return True
    return False
                
def solve():
    answer = 0
    success = False
    while answer <= 1000:
        for i in range(K):
            if move(info[i][0], info[i][1], i):
                success = True
                break
        answer += 1
        if success:
            break
    return answer if answer <= 1000 else -1

print(solve())