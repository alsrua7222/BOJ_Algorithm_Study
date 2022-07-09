L, N, T = map(int, input().split())
balls = []
for _ in range(N):
    query = list(input().split())
    balls.append([int(query[0]), 1 if query[1] == 'R' else 0]) # 0 - left, 1 - right

def process():
    global balls
    tmp_L = [list() for _ in range(L + 1)]
    
    for i in range(N):
        pos, dir = balls[i]
        if dir == 1:
            tmp_L[pos + 1].append([pos + 1, dir])
        else:
            tmp_L[pos - 1].append([pos - 1, dir])
    
    new_balls = []
    if tmp_L[0]:
        new_balls.append([tmp_L[0][0][0], 1])
    if tmp_L[L]:
        new_balls.append([tmp_L[L][0][0], 0])

    ret = 0
    for i in range(1, L):
        if not tmp_L[i]:
            continue
        
        if len(tmp_L[i]) == 2:
            new_balls.append([tmp_L[i][0][0], 1])
            new_balls.append([tmp_L[i][0][0], 0])
            ret += 1
        else:
            new_balls.append(tmp_L[i][0])
    
    balls = new_balls.copy()
    return ret

answer = 0
for i in range(1, T + 1):
    answer += process()
print(answer)