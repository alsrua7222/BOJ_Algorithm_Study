# 풀이 과정
# https://blog.naver.com/alsrua7222/222634634258
import sys
sys.setrecursionlimit(10 ** 6)

arr = [list(map(int, input().split())) for _ in range(9)]
blank = []
for i in range(9):
    for j in range(9):
        if arr[i][j] == 0:
            blank.append([i, j])

def IsSameInRow(numbers, x):
    for i in range(9):
        if arr[x][i] in numbers:
            numbers.remove(arr[x][i])
    return numbers


def IsSameInCol(numbers, y):
    for i in range(9):
        if arr[i][y] in numbers:
            numbers.remove(arr[i][y])
    return numbers


def IsSameIn3x3(numbers, x, y):
    x = x - x % 3
    y = y - y % 3
    for i in range(x, x + 3):
        for j in range(y, y + 3):
            if arr[i][j] in numbers:
                numbers.remove(arr[i][j])
    return numbers


def Check(x, y):
    numbers = set(list(range(1, 10)))
    numbers = IsSameInRow(numbers, x)
    numbers = IsSameInCol(numbers, y)
    numbers = IsSameIn3x3(numbers, x, y)
    return numbers

def backtracking(cur):
    if cur == len(blank):
        return True
    x, y = blank[cur]

    for v in Check(x, y):
        arr[x][y] = v
        if backtracking(cur + 1):
            return True
        arr[x][y] = 0
    return False

backtracking(0)
for v in arr:
    print(*v)
