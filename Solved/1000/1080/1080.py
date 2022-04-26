# 풀이 과정
# https://blog.naver.com/alsrua7222/222702693596

N, M = map(int, input().split())
A = [list(map(int, list(input()))) for _ in range(N)]
B = [list(map(int, list(input()))) for _ in range(N)]

answer = 0
for x in range(N - 3 + 1):
    for y in range(M - 3 + 1):
        if A[x][y] != B[x][y]:
            answer += 1
            for i in range(x, x + 3):
                for j in range(y, y + 3):
                    A[i][j] ^= 1

success = True
for x in range(N):
    for y in range(M):
        if A[x][y] != B[x][y]:
            success = False
            break
print(-1 if not success else answer)