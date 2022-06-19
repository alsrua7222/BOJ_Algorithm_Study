N, L = map(int, input().split())
MAP = [list(map(int, input().split())) for _ in range(N)]
answer = 0

rowMAP = []
for x in range(N):
    tmp = []
    cnt = 1
    pre = MAP[x][0]
    for y in range(1, N):
        if pre == MAP[x][y]:
            cnt += 1
        else:
            tmp.append((pre, cnt))
            pre = MAP[x][y]
            cnt = 1
    tmp.append((pre, cnt))
    rowMAP.append(tmp)

colMAP = []
for y in range(N):
    tmp = []
    cnt = 1
    pre = MAP[0][y]
    for x in range(1, N):
        if pre == MAP[x][y]:
            cnt += 1
        else:
            tmp.append((pre, cnt))
            pre = MAP[x][y]
            cnt = 1
    tmp.append((pre, cnt))
    colMAP.append(tmp)

def Check(arr):
    success = True
    diff = arr[i][0] - arr[i + 1][0]
    for i in range(len(arr) - 1):
        diff = abs(arr[i][0] - arr[i+1][0])
        if diff >= 2:
            return False
        if arr[i + 1][1] < L 
    return True