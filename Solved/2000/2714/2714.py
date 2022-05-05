for _ in range(int(input())):
    query = list(input().split())
    R = int(query[0])
    C = int(query[1])
    S = query[2]

    row, col = 0, 0
    MAP = [[0 for _ in range(C)] for _ in range(R)]
    for i in range(len(S)):
        MAP[row][col] = S[i]
        col += 1
        if col == C:
            col = 0
            row += 1
    
    moves = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    visited = [[False for _ in range(C)] for _ in range(R)]
    status = 0
    r, c = 0, 0
    string = ""
    answer = []
    while True:
        if 0 > r or r >= R or 0 > c or c >= C or visited[r][c]:
            r -= moves[status][0]
            c -= moves[status][1]
            status = (status + 1) % 4
            r += moves[status][0]
            c += moves[status][1]
            if 0 > r or r >= R or 0 > c or c >= C or visited[r][c]:
                break
        string += MAP[r][c]
        visited[r][c] = True
        if len(string) == 5:
            if '1' not in string:
                answer.append(' ')
                string = ""
            else:
                answer.append(chr(ord('A') + int("0b" + string, 2) - 1))
                string = ""
        r += moves[status][0]
        c += moves[status][1]
    
    if '1' in string:
        while len(string) < 5:
            string += "0"
        answer.append(chr(ord('A') + int("0b" + string, 2)))
    print("".join(answer).rstrip())