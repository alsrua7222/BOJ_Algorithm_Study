N, M = map(int, input().split())
matrix1 = [list(map(int, input().split())) for _ in range(N)]
matrix2 = [list(map(int, input().split())) for _ in range(N)]

# matrix sum
matrix3 = [[0 for _ in range(M)] for _ in range(N)]
for i in range(N):
    for j in range(M):
        matrix3[i][j] = matrix1[i][j] + matrix2[i][j]

for v in matrix3:
    print(*v)