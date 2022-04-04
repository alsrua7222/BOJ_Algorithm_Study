# 풀이 과정
# https://blog.naver.com/alsrua7222/222691783001

N, M = map(int, input().split())
arr = [[0] * (N + 1) for _ in range(N + 1)]

for _ in range(M):
    a, b = map(int, input().split())
    arr[a][b] = 1
    arr[b][a] = 1

# 플로이드 와샬
for k in range(1, N + 1):
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            if i == j or j == k or i == k or arr[i][k] == 0 or arr[k][j] == 0:
                continue
            if arr[i][j] == 0:
                arr[i][j] = arr[i][k] + arr[k][j]
            else:
                arr[i][j] = min(arr[i][j], arr[i][k] + arr[k][j])

MIN = float('inf')
answer = 0
for i in range(1, N + 1):
    tmp = sum(arr[i])
    if MIN > tmp:
        MIN = tmp
        answer = i
print(answer)