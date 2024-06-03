import sys
input = sys.stdin.readline

for t in range(int(input())):
    n, m = map(int, input().split())

    a_matrix = []
    b_matrix = []

    for _ in range(n):
        a_matrix.append(list(map(int, input().split())))
    for _ in range(n):
        b_matrix.append(list(map(int, input().split())))

    def reverse_transe(matrix):
        n = len(matrix)
        temp_matrix = []
        for _ in range(n):
            temp_matrix.append([0] * n)

        for x in range(n):
            for y in range(n):
                temp_matrix[y][x] = matrix[x][y]
        return temp_matrix

    flag = True

    flag_set = set()
    for v in a_matrix:
        flag_set.add(frozenset(v))
        
    for v in b_matrix:
        tmp = frozenset(v)
        if tmp not in flag_set:
            flag = False
            break

    if not flag:
        print("NO")
        continue

    if n == m:
        flag_set = set()
        a_matrix = reverse_transe(a_matrix)
        b_matrix = reverse_transe(b_matrix)

        for v in a_matrix:
            flag_set.add(frozenset(v))
        
        for v in b_matrix:
            tmp = frozenset(v)
            if tmp not in flag_set:
                flag = False
                break
    else:
        flag_set = set()
        for y in range(m):
            tmp = set()
            for x in range(n):
                tmp.add(a_matrix[x][y])
            flag_set.add(frozenset(tmp))
        
        for y in range(m):
            tmp = set()
            for x in range(n):
                tmp.add(b_matrix[x][y])
            
            if frozenset(tmp) not in flag_set:
                flag = False
                break
        
    if flag:
        print("YES")
    else:
        print("NO")
        