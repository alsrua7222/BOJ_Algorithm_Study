from collections import deque, defaultdict
import sys
input = sys.stdin.readline
N = int(input())
Graph = defaultdict(list)
while True:
    u, v = map(int, input().split())
    if u == -1:
        break
    Graph[u].append(v)
    Graph[v].append(u)

def BFS(start):
    Queue = deque([[start, 0]])
    visited = [False] * (N + 1)
    visited[start] = True
    answer = 0
    while Queue:
        cur, dist = Queue.popleft()
        for next in Graph[cur]:
            if visited[next]:
                continue
            visited[next] = True
            Queue.append([next, dist + 1])
            if answer < dist + 1:
                answer = dist + 1
    return answer

answer = 987654231
collect = []

for i in range(1, N + 1):
    tmp = BFS(i)
    if answer > tmp:
        answer = tmp
        collect = [i]
    elif answer == tmp:
        collect.append(i)

print(answer, len(collect))
print(*collect)
