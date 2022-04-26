# 풀이 과정
# https://blog.naver.com/alsrua7222/222672666502

import sys
input = sys.stdin.readline
N, K = map(int, input().split())
arr = []
for _  in range(N):
    arr.append(list(map(int, input().split())))


for k in range(N):
    for i in range(N):
        for j in range(N):
            if arr[i][k] + arr[k][j] < arr[i][j]:
                arr[i][j] = arr[i][k] + arr[k][j]

answer = float('inf')
visited = [False] * (N + 1)
def DFS(index, dist, cnt):
    global answer
    if dist > answer:
        return
    
    if cnt == N:
        answer = min(answer, dist)
        return
    
    for i in range(N):
        if not visited[i]:
            visited[i] = True
            DFS(i, dist + arr[index][i], cnt + 1)
            visited[i] = False
    return

visited[K] = True
DFS(K, 0, 1)
print(answer)