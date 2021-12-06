from collections import defaultdict, deque
import sys
input = sys.stdin.readline

N, R, D, X, Y = map(int, input().split())
Graph = defaultdict(list)
arr = [[X, Y]]

# 데이터 전처리 - 모든 점에 대해서 주어진 거리 안에 포괄되는 점만 추가하기.
for i in range(1, N + 1):
    x, y = map(int, input().split())
    arr.append([x, y])
    for j in range(i):
        if ((arr[i][0] - arr[j][0]) ** 2 + (arr[i][1] - arr[j][1]) ** 2) ** .5 <= R:
            Graph[i].append(j)
            Graph[j].append(i)

answer, size = 0, 1
Queue = deque([0])
visited = [False] * (N + 1)
visited[0] = True
while Queue:
    Qsize = len(Queue)
    for i in range(Qsize):
        cur = Queue.popleft()
        for next in Graph[cur]:
            if not visited[next]:
                visited[next] = True
                Queue.append(next)
                answer += D * size
    size /= 2

print(round(answer, 2))
