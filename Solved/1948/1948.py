import sys
input = sys.stdin.readline
from collections import defaultdict, deque
N = int(input())
Graph = defaultdict(list)
Reverse_Graph = defaultdict(list)
InDegree = [0] * (N + 1)
for _ in range(int(input())):
    A, B, C = map(int, input().split())
    Graph[A].append([B, C])
    Reverse_Graph[B].append([A, C])
    # Graph[B].append([A, C])
    InDegree[B] += 1

start, end = map(int, input().split())
Queue = deque()
Queue.append([start, 0])

arr = [0] * (N + 1)
while Queue:
    node, w = Queue.pop()

    for next, W in Graph[node]:
        InDegree[next] -= 1
        total = max(arr[next], w + W)
        if InDegree[next] == 0:
            Queue.append([next, total])
        arr[next] = total

print(arr[end])

# 역추적
Queue.append(end)
visited = [False for i in range(N + 1)]
answer = 0
while Queue:
    node = Queue.popleft()
    for next, w in Reverse_Graph[node]:
        if arr[node] - w == arr[next]:
            answer += 1
            if not visited[next]:
                visited[next] = True
                Queue.append(next)
print(answer)
