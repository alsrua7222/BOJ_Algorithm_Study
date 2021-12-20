# 풀이 과정
# https://blog.naver.com/alsrua7222/222600525785

import sys
input = sys.stdin.readline

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

N, K = map(int, input().split())

arr = [[0 for _ in range(N)] for _ in range(N)]
parents = [i for i in range(K + 1)]
PreStack = []

for i in range(1, K + 1):
    x, y = map(int, input().split())
    arr[y - 1][x - 1] = i
    PreStack.append([x - 1, y - 1])

def find(x):
    if parents[x] == x:
        return x
    else:
        p = find(parents[x])
        parents[x] = p
        return p

def union(x, y):
    if x == y:
        return
    if x > y:
        parents[x] = y
    else:
        parents[y] = x

def BFS():
    answer = 0
    count = K
    while count != 1:
        PostStack = PreStack.copy()
        while PreStack:
            x, y = PreStack.pop()
            for i in range(4):
                X = x + dx[i]
                Y = y + dy[i]
                if 0 <= X < N and 0 <= Y < N and arr[Y][X] > 0:
                    next = find(arr[Y][X])
                    cur = find(arr[y][x])
                    if next != cur:
                        union(cur, next)
                        count -= 1
        if count == 1:
            break
        answer += 1
        while PostStack:
            x, y = PostStack.pop()
            for i in range(4):
                X = x + dx[i]
                Y = y + dy[i]
                if 0 <= X < N and 0 <= Y < N and arr[Y][X] == 0:
                    arr[Y][X] = arr[y][x]
                    PreStack.append([X, Y])
    return answer

print(BFS())
