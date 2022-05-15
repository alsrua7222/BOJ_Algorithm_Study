import copy
N, M = map(int, input().split())
MAP = [list(map(int, input().split())) for _ in range(N)]
rowSums, colSums = [0] * N, [0] * M
row_min, col_min = float('inf'), float('inf')
row_min_idx, col_min_idx = -1, -1

def calc(matrix):
    ret = 0
    for row in range(N - 1):
        for col in range(M - 1):
            ret += matrix[row][col] + matrix[row][col + 1] + matrix[row + 1][col] + matrix[row + 1][col + 1]
    return ret

def getMatrix(idx1, idx2, rc):
    ret = copy.deepcopy(MAP)
    
    if rc:
        for col in range(M):
            ret[idx1][col], ret[idx2][col] = ret[idx2][col], ret[idx1][col]
    else:
        for row in range(N):
            ret[row][idx1], ret[row][idx2] = ret[row][idx2], ret[row][idx1]

    return ret

answer = calc(MAP)

# prefix Sum
for row in range(N):
    for col in range(M):
        rowSums[row] += MAP[row][col]
        colSums[col] += MAP[row][col]

# get min row, col
for row in range(1, N - 1):
    total = rowSums[row] * 4
    total -= 2 * (MAP[row][0] + MAP[row][M - 1])
    if row_min > total:
        row_min = total
        row_min_idx = row

for col in range(1, M - 1):
    total = colSums[col] * 4
    total -= 2 * (MAP[0][col] + MAP[N - 1][col])
    if col_min > total:
        col_min = total
        col_min_idx = col

answer = max(answer, calc(getMatrix(0, col_min_idx, False))) # [0, 최솟값 있는 열 인덱스]
answer = max(answer, calc(getMatrix(M - 1, col_min_idx, False))) # [M - 1, 최솟값 있는 열 인덱스]
answer = max(answer, calc(getMatrix(row_min_idx, 0, True))) # [최솟값 있는 행 인덱스, 0]
answer = max(answer, calc(getMatrix(row_min_idx, N - 1, True))) # [최솟값 있는 행 인덱스, N - 1]

print(answer)