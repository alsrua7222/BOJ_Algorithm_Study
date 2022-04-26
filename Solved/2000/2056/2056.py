from collections import defaultdict
import heapq
N = int(input())
Graph = defaultdict(list)
InDegree = [0] * (N + 1)
Times = [0]
for i in range(1, N + 1):
    query = list(map(int, input().split()))
    Times.append(query[0])
    for v in query[2:]:
        Graph[v].append(i)
    InDegree[i] += len(query[2:])

# 본 문제에서는 항상 1번 작업이 시작점이다. 그렇지만, 하나만 있는게 아니라 둘 이상 있을 수도 있으므로 반드시 검사해서 큐에 적재시킨다.
HQ = []
answer = [987654321] * (N + 1)
for i in range(1, N + 1):
    if InDegree[i] == 0:
        heapq.heappush(HQ, [Times[i], i])
        answer[i] = Times[i]

while HQ:
    times, cur = heapq.heappop(HQ)

    for v in Graph[cur]:
        InDegree[v] -= 1
        if InDegree[v] == 0:
            heapq.heappush(HQ, [times + Times[v], v])
        answer[v] = times + Times[v]

print(max(answer[1:]))
