from collections import deque
N = int(input())

matrix = [list() for _ in range(N + 1)]
InDegree = [0] * (N + 1)
cost = [0] * (N + 1)

for i in range(1, N + 1):
    query = list(map(int, input().split()))
    cost[i] = query[0]
    for v in query[1:-1]:
        matrix[v].append(i)
        InDegree[i] += 1

ret = [0] * (N + 1)
Queue = deque()
for i in range(1, N + 1):
    if InDegree[i] == 0:
        Queue.append(i)
    
while Queue:
    cur = Queue.popleft()
    ret[cur] += cost[cur]
    for v in matrix[cur]:
        InDegree[v] -= 1
        ret[v] = max(ret[v], ret[cur])
        if InDegree[v] == 0:
            Queue.append(v)

print(*ret[1:], sep="\n")