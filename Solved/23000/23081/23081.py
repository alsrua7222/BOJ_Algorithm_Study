import sys
input = sys.stdin.readline
N = int(input())

arr = []
for _ in range(N):
    arr.append(list(input()))
answer = [0, 0, 0]
# answer formatting = [value, x, y]


def getMaxlength(x, y, v, X, Y):
    if not (0 <= x < N and 0 <= y < N):
        return

    if arr[y][x] == '.':
        return
    elif arr[y][x] == 'B':
        global tmp
        if tmp < v:
            tmp = v
    else:
        getMaxlength(x + X, y + Y, v + 1, X, Y)
    return
# right, down, left, up, rightdown, leftdown, upleft, upright
X = [1, 0, -1, 0, 1, -1, -1, 1]
Y = [0, 1, 0, -1, 1, 1, -1, -1]
for col in range(N):
    for row in range(N):
        if arr[col][row] == '.':
            result = [0, row, col]
            for i in range(8):
                tmp = 0
                getMaxlength(row + X[i], col + Y[i], 0, X[i], Y[i])
                result[0] += tmp
            if answer[0] < result[0]:
                answer = result.copy()
            elif answer[0] == result[0]:
                if answer[2] > col:
                    answer = result.copy()
                elif answer[2] == col:
                    if answer[1] > row:
                        answer = result.copy()

if answer[0] == 0:
    print("PASS")
else:
    print(answer[1], answer[2])
    print(answer[0])
