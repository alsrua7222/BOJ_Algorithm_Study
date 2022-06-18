N, M, x, y, K = map(int, input().split())
MAP = [list(map(int, input().split())) for _ in range(N)]
querys = list(map(int, input().split()))
dx = [0, 0, 0, -1, 1]
dy = [0, 1, -1, 0, 0]
dice = [0] * 7
dirDice = [0, 1, 2, 3, 4, 5, 6] # 1이 아랫면, 3이 윗면
def setDirDice(dir):
    if dir == 1: # 동
        dirDice[5], dirDice[1], dirDice[6], dirDice[3] = dirDice[1], dirDice[6], dirDice[3], dirDice[5]
    elif dir == 2: # 남
        dirDice[3], dirDice[6], dirDice[1], dirDice[5] = dirDice[6], dirDice[1], dirDice[5], dirDice[3]
    elif dir == 3: # 서
        dirDice[4], dirDice[3], dirDice[2], dirDice[1] = dirDice[3], dirDice[2], dirDice[1], dirDice[4]
    elif dir == 4: # 북
        dirDice[1], dirDice[2], dirDice[3], dirDice[4] = dirDice[2], dirDice[3], dirDice[4], dirDice[1]
    return

for v in querys:
    nx, ny = x + dx[v], y + dy[v]
    if 0 <= nx < N and 0 <= ny < M:
        setDirDice(v)
        if MAP[nx][ny] == 0: # 복사
            MAP[nx][ny] = dice[dirDice[3]]
        else:
            dice[dirDice[3]] = MAP[nx][ny]
            MAP[nx][ny] = 0
        print(dice[dirDice[1]]) # 윗면 출력
        x = nx
        y = ny