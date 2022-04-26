from collections import deque
import sys
input = sys.stdin.readline
N, M, H = map(int, input().split())
MAPS = [0] * H
MAX = -1
for h in range(H):
    inputlist = []
    for _ in range(M):
        inputlist.append(list(map(int, input().split())))
    MAPS[h] = inputlist
def IsAllNotZero(MAPS):
    global MAX
    for h in range(H):
        for m in range(M):
            for n in range(N):
                if MAPS[h][m][n] == 0:
                    return False
                else:
                    MAX = max(MAPS[h][m][n], MAX)
    return True

if IsAllNotZero(MAPS):
    print(0)
    exit(0)

def initFindOnes(MAPS):
    result = deque()
    for h in range(H):
        for m in range(M):
            for n in range(N):
                if MAPS[h][m][n] == 1:
                    result.append([h, m, n, 1])
    return result


visited = [[[False for n in range(N)] for m in range(M)] for h in range(H)]
Queue = initFindOnes(MAPS)
# right -> down -> left -> up -> top up -> bottom down
query = [(1, 0, 0), (0, 1, 0), (-1, 0, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]

while Queue:
    h, m, n, s = Queue.popleft()

    for x, y, z in query:
        if 0 <= x + n < N and 0 <= y + m < M and 0 <= z + h < H:
            if visited[z + h][y + m][x + n]:
                continue
            if MAPS[z + h][y + m][x + n] != -1:
                visited[z + h][y + m][x + n] = True
                MAPS[z + h][y + m][x + n] = s + 1
                Queue.append([z + h, y + m, x + n, s + 1])

if IsAllNotZero(MAPS):
    print(MAX - 1)
else:
    print(-1)
