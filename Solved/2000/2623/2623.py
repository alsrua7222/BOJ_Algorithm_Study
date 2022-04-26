from collections import defaultdict, deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())

# 위상정렬 위한 그래프.
Graph = defaultdict(list)
# 차수
Indegree = [0] * (1 + N)

for _ in range(M):
    tmp = list(map(int, input().split()))[1:]
    for i in range(len(tmp) - 1):
        Graph[tmp[i]].append(tmp[i + 1])
        Indegree[tmp[i + 1]] += 1

Queue = deque()
for i in range(1, N + 1):
    if Indegree[i] == 0:
        Queue.append(i)

# 차수가 0인 스택이 없으면 나가
if not Queue:
    print(0)
    exit(0)

# 위상정렬 반복.
answer = []
while Queue:
    now = Queue.popleft()
    answer.append(now)

    for next in Graph[now]:
        Indegree[next] -= 1
        if Indegree[next] == 0:
            Queue.append(next)

# 길이가 안 맞으면 나가
# 맞으면 하나씩 출력.
if len(answer) != N:
    print(0)
else:
    for v in answer:
        print(v)
