import copy

def solution(places):
    answer = []
    for i in range(5):
        for j in range(5):
            places[i][j] = list(places[i][j])
    for i in range(5):
        IsCorona = False
        for j in range(5):
            for k in range(5):
                if places[i][j][k] == 'P':
                    Table = copy.deepcopy(places[i])
                    Table[j][k] = 'F'
                    if DFS(Table, j, k, 0):
                        IsCorona = True
                        break
            if IsCorona:
                break
        if not IsCorona:
            answer.append(1)
        else:
            answer.append(0)
            
    return answer

def DFS(places, y, x, cnt):
    if places[y][x] == 'P':
        return True
    elif places[y][x] == 'X':
        return False
    if cnt == 2:
        return False
    else:
        # right -> down -> left -> up
        X = [1, 0, -1, 0]
        Y = [0, 1, 0, -1]
        for i in range(4):
            if x + X[i] >= 5 or x + X[i] < 0:
                continue
            elif y + Y[i] >= 5 or y + Y[i] < 0:
                continue
            
            if DFS(places, y + Y[i], x + X[i], cnt + 1):
                return True
    return False