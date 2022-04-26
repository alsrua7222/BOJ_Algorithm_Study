from collections import deque
import sys, copy
input = sys.stdin.readline

def left(maps, N):
    Stack = deque()
    arr = copy.deepcopy(maps)
    for col in range(N):
        for row in range(N):
            if arr[col][row] != 0:
                Stack.append(arr[col][row])
        row = 0
        while len(Stack) > 1:
            if Stack[0] == Stack[1]:
                arr[col][row] = Stack.popleft() + Stack.popleft()
            else:
                arr[col][row] = Stack.popleft()
            row += 1
        if Stack:
            arr[col][row] = Stack.popleft()
            row += 1

        # 마감 처리.
        while row < N:
            arr[col][row] = 0
            row += 1
    return arr

def right(maps, N):
    Stack = deque()
    arr = copy.deepcopy(maps)
    for col in range(N):
        for row in range(N - 1, -1, -1):
            if arr[col][row] != 0:
                Stack.append(arr[col][row])
        row = N - 1
        while len(Stack) > 1:
            if Stack[0] == Stack[1]:
                arr[col][row] = Stack.popleft() + Stack.popleft()
            else:
                arr[col][row] = Stack.popleft()
            row -= 1
        if Stack:
            arr[col][row] = Stack.popleft()
            row -= 1

        # 마감 처리.
        while row > -1:
            arr[col][row] = 0
            row -= 1
    return arr

def up(maps, N):
    Stack = deque()
    arr = copy.deepcopy(maps)
    for row in range(N):
        for col in range(N - 1, -1, -1):
            if arr[col][row] != 0:
                Stack.append(arr[col][row])
        col = N - 1
        while len(Stack) > 1:
            if Stack[0] == Stack[1]:
                arr[col][row] = Stack.popleft() + Stack.popleft()
            else:
                arr[col][row] = Stack.popleft()
            col -= 1
        if Stack:
            arr[col][row] = Stack.popleft()
            col -= 1
        while col > -1:
            arr[col][row] = 0
            col -= 1
    return arr


def down(maps, N):
    Stack = deque()
    arr = copy.deepcopy(maps)
    for row in range(N):
        for col in range(N):
            if arr[col][row] != 0:
                Stack.append(arr[col][row])
        col = 0
        while len(Stack) > 1:
            if Stack[0] == Stack[1]:
                arr[col][row] = Stack.popleft() + Stack.popleft()
            else:
                arr[col][row] = Stack.popleft()
            col += 1
        if Stack:
            arr[col][row] = Stack.popleft()
            col += 1
        while col < N:
            arr[col][row] = 0
            col += 1
    return arr

def getMax(maps, N):
    tmp = 0
    for col in range(N):
        for row in range(N):
            if tmp < maps[col][row]:
                tmp = maps[col][row]
    return tmp

N = int(input())
arr = []
for _ in range(N):
    arr.append(list(map(int, input().split())))

if N == 1:
    print(arr[0][0])
    exit(0)
Queue = deque()
Queue.append([arr.copy(), 0])
answer = 0
while Queue:
    maps, v = Queue.popleft()

    if v + 1 != 6:
        Queue.append([left(maps, N), v + 1])
        Queue.append([right(maps, N), v + 1])
        Queue.append([up(maps, N), v + 1])
        Queue.append([down(maps, N), v + 1])
    else:
        answer = max(getMax(maps, N), answer)
print(answer)
