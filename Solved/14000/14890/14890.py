N, L = map(int, input().split())
MAP = [list(map(int, input().split())) for _ in range(N)]

def IsAble(arr):
    visited = [False] * (N + 1)
    for i in range(1, N):
        if arr[i - 1] != arr[i]:
            diff = abs(arr[i] - arr[i - 1])
            if diff != 1:
                return False
                
            if arr[i - 1] < arr[i]:
                for j in range(1, L + 1):
                    if i - j < 0:
                        return False
                    if arr[i - 1] != arr[i - j]:
                        return False
                    if visited[i - j]:
                        return False
                    visited[i - j] = True
            else:
                for j in range(L):
                    if i + j >= N:
                        return False
                    if arr[i] != arr[i + j]:
                        return False
                    if visited[i + j]:
                        return False
                    visited[i + j] = True
    return True
answer = 0
for x in range(N):
    if IsAble(MAP[x]):
        answer += 1

for y in range(N):
    col = []
    for x in range(N):
        col.append(MAP[x][y])
    if IsAble(col):
        answer += 1

print(answer)